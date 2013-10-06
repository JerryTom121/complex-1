'''
Created on Sep 22, 2013

@author: Ivan Bogun
'''
import twitterstream as twitterStream;
import json
from filters import *;
import time;

class Twitter:
    '''
    A class to define connection with the twitter API and start downloading
    tweets etc.
    '''
    url = "https://stream.twitter.com/1/statuses/sample.json";
    
    
    def filter(self):
        return True;
    
    def __init__(self,function=filter,*args):
        '''
        Add constructor to filter by hash tag, topic
        '''
        self.filter=function;
        self.args=args;
        
        
    def downloadTweet(self,filename,numOfTweets=10):
        '''
        Function will download tweets with the number specified by numOfTweets
        '''
        
        
        counter=0;
        tweets=[];
        parameters = [];
        response = twitterStream.twitterreq(self.url, "GET", parameters)
        
        keywords={"Cloudy2":{"cloudy","meatballs"},
              "Runner":{"runner movie"},
              "Metallica":{"metallica","through","never"},
              "ACOD":{"a.c.o.d"},
              "RushMovie":{"rush movie"},
              "Parkland":{"parkland"},
              "DonJon":{"donjon","don jon"},
              "Bad Milo":{"bad milo"}         
              }
        
        movieSet={"_RunnerRunner","MetallicaMovie","ACODmovie",
                  "rushthemovie","ParklandFilm","CloudyMovie","DonJon",
                  "RushMovieUK","ParklandMov","ParklandUK"};
        hashTagSet={"Gravity","MetallicaThroughTheNever","RunnerRunner",
                    "ACOD","Parkland","BadMilo","Cloudy2","RUSHMovie"};
        file = open(filename,'a');
        
        
        startTime=time.time();
        for line in response:
            tweet=json.loads(line);
            
            currentTime=time.time();
            # if tweet is not empty
            if (ifTweetMentionsOneOfMovies(tweet,movieSet,hashTagSet,keywords)):
                print tweet.get("text");
                file.write(str(tweet)+"\n");  
                tweets.append(tweet);
                counter=counter+1;
                print "Number of tweets downloaded: "+str(counter);
            if (counter>=numOfTweets):
                break;
        return tweets;
    
    
    
twitter=Twitter();
tweets=twitter.downloadTweet("out1.txt",100000);



