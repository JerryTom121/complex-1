'''
Created on Oct 9, 2013

@author: ibogun2010
'''
import urllib2
import json;

class RottenTomatoes:
    '''
    Class to get information from RottenTomatoes.com regarding
    how much money the movies got etc.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.key="22nbwp2b2xszz3pkqcchwd73";
    
    def getBoxOffice(self,numOfMovies=16):
        
        requestNamePart1="http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?limit=";
        requestNamePart2="&country=us&apikey=";
        
        url=requestNamePart1+str(numOfMovies)+requestNamePart2+self.key;
        
        response = urllib2.urlopen(url)
        html = response.read()
        
        dict=json.loads(html);
        
        
rt=RottenTomatoes();
rt.getBoxOffice();