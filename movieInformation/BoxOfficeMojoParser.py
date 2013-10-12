'''
Created on Oct 9, 2013

@author: ibogun2010
'''
import urllib2
import urllib
from pyparsing import *
import re;
from decimal import Decimal
from re import sub

class BoxOfficeMojoParser:
    '''
    Class to get information from RottenTomatoes.com regarding
    how much money the movies got etc.
    '''
    movieName="";
    currentDate=[];
    currentBoxOffice=[];
    boxOfficeHistory=dict();
    
    
    def __init__(self,movie):
        '''
        Constructor
        '''
        self.key="22nbwp2b2xszz3pkqcchwd73";
        self.movieName=movie;
        
    @staticmethod
    def checkIfMoney(str):
        p=re.compile("(.*)\$\d(.*)")
        a=p.match(str);
        
        result=False;
        if a is not None:
            result=True;
        return result;
    
    @staticmethod   
    def getMoney(str):
        p1=re.compile("\$(((\d+),(\d+),(\d+))|((\d+),(\d+))|(\d+))");
        res=p1.search(str);
        
        if res is None:
            return None;
        else:
            return res.group();
        
    @staticmethod
    def getDate(str):
        p1=re.compile("(Oct(\s*).|Nov(\s*).|Dec(\s*).|Jan(\s*).|Feb(\s*).|Mar(\s*).|Apr(\s*).|May|June|July|Aug(\s*).(\s*)|Sep(\s*).)(\s+)\d+,(\s+)(2013|2014)");
        res=p1.search(str);
        
        if res is None:
            return None;
        else:
            return res.group();

    @staticmethod
    def parseTag(str,tag):
        anchorStart,anchorEnd = makeHTMLTags(tag)
        
        anchor = anchorStart + SkipTo(anchorEnd).setResultsName("body") + anchorEnd
        
        generator=anchor.scanString(str);
        
        
        result='';
        
        for tokens,start,end in generator:
            result+=tokens.body;
            #result=result+ str(tokens.body)
            
        return result;
        
    @staticmethod
    def moneyFromStrToDecimal(str):
        return Decimal(sub(r'[^\d.]', '', str));
    
    def getBoxOffice(self):
        
        #url=requestNamePart1+str(numOfMovies)+requestNamePart2+self.key;
        
        url2="http://www.boxofficemojo.com/movies/?page=daily&view=chart&id="+self.movieName+".htm";
        
        
        
        response = urllib2.urlopen(url2)
        html = response.read();
        
        anchorStart,anchorEnd = makeHTMLTags("table")
        # read HTML from a web page
        serverListPage = urllib.urlopen( url2 )
        htmlText = serverListPage.read()
        serverListPage.close()
        
        
        table=self.parseTag(htmlText,"table");
        
        tr=self.parseTag(table,"tr");
        trLines=tr.splitlines();
        
        isFirst=True;
        lastDate="";
        
        c=0;
        
        for line in trLines:
            # given a line try to parse Date, money
            moneyFlag=self.checkIfMoney(line);
            date=self.getDate(line)
            
            #print line;
            
            # if there is date
            if (date is not None):
                #print date;
                # the first date on the web page is the most current date of the data
                if(isFirst):
                    self.currentDate=date;
                else:
                    #print lastDate;
                    lastDate=date;
                
                if (c%3 is 0):
                   
                    l=list();
            
            # if there is money - get them
            if moneyFlag:
                money=self.getMoney(line);
                
                if (isFirst):
                    self.currentBoxOffice=money;
                    isFirst=False;
                else:
                    l.append(self.moneyFromStrToDecimal(money));
                    c+=1;
                    if (c%3 is 0):
                        self.boxOfficeHistory[lastDate]=l; 
                
                # add all results to the dictionary

                #print money;
movie="prisoners";
rt=BoxOfficeMojoParser(movie);
rt.getBoxOffice();
boxOffice=rt.boxOfficeHistory;
cd=rt.currentDate;
cbo=rt.currentBoxOffice;
print cd;
print cbo;