'''
Created on Sep 22, 2013

@author: Ivan Bogun
'''
import twitterstream as twitterStream;
import json
from filters import *;
import time;
import datetime;
#from movieInformation import *;

class Twitter:
    '''
    A class to define connection with the twitter API and start downloading
    tweets etc.
    '''
    url = "https://stream.twitter.com/1/statuses/filter.json";
    
    
    def filter(self):
        return True;
    
    def __init__(self,function=filter,*args):
        '''
        Add constructor to filter by hash tag, topic
        '''
        self.filter=function;
        self.args=args;
        
        
    def downloadTweet(self,filename):
        '''
        Function will download tweets with the number specified by numOfTweets
        '''
        
        
        counter=0;
        tweets=[];
        parameters = {'track':"CaptainPhillips,Captain Phillips,captain Phillips,Captain phillips, captaion phillips"};
        response = twitterStream.twitterreq(self.url, "GET", parameters)
        
        keywords={"CaptainPhillips":{"Captain","Phillips"}        
              }
        
        movieSet={"CaptainPhillips"};
        hashTagSet={"CaptainPhillips"};
        file = open(filename,'a+');
        
        currentDate=datetime.datetime.now();
        file.write(str(currentDate)+"\n");
        startTime=time.time();
        hours=6;
        for line in response:
            tweet=json.loads(line);
            
            currentTime=time.time();
            # if tweet is not empty
            if (ifTweetMentionsOneOfMovies(tweet, movieSet, hashTagSet, keywords)):
                file.write(str(tweet)+"\n");
                #print tweet.get("text");
                tweets.append(tweet);
                counter=counter+1;
                #print "Number of tweets downloaded: "+str(counter);
            if ((currentTime-startTime)/(60*60*hours)>1):
                break;
        file.close();
        return tweets;
    
    
    
twitter=Twitter();
tweets=twitter.downloadTweet("CaptainPhillips.txt");
rt=RottenTomatoes("rottenOpenTheaters.txt","rottenBoxOffice.txt");
d=rt.getInformationInTheaters(); 


