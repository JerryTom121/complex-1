'''
Created on Oct 12, 2013

@author: ivan
'''
import json;
import urllib2
import datetime

class RottenTomatoes(object):
    '''
    Parse movie and critique ratings from rotten tomatoes
    '''


    def __init__(self,theatersFile,boxOfficeFile):
        '''
        Constructor
        '''
        currentTime=datetime.datetime.now();
        f1 = open(theatersFile,'a+');
        f2 = open(boxOfficeFile,'a+');
        
        in1=self.getInformationInTheaters();
        in2=self.getInformationBoxOffice();
        
        
        f1.write(str(currentTime)+"\n");
        f2.write(str(currentTime)+"\n");
        f1.write(in1+"\n");
        f2.write(in2+"\n");
        
        f1.close();
        f2.close();
        
    def getInformationInTheaters(self):
        
        url="http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=50&page=1&country=us&apikey=22nbwp2b2xszz3pkqcchwd73";
        
        response = urllib2.urlopen(url)
        html = response.read()
        dict=json.loads(html);
        return str(dict);
    
    def getInformationBoxOffice(self):
        
        url="http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?limit=50&country=us&apikey=22nbwp2b2xszz3pkqcchwd73";
        
        response = urllib2.urlopen(url)
        html = response.read()
        
        dict=json.loads(html);
        
        
        return str(dict);
        
rt=RottenTomatoes("t1.txt","t2.txt");
d=rt.getInformationInTheaters();       

    
    
    
    
    
    
    
    
    
    
    
    