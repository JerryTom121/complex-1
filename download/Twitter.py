'''
Created on Sep 22, 2013

@author: Ivan Bogun
'''
import twitterstream as twitterStream;
import json
from filters import *;

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
        
        
    def downloadTweet(self,numOfTweets=10):
        '''
        Function will download tweets with the number specified by numOfTweets
        '''
        
        
        counter=0;
        tweets=[];
        parameters = [];
        response = twitterStream.twitterreq(self.url, "GET", parameters)
        
        movieSet={"_RunnerRunner","MetallicaMovie","ACODmovie","ParklandFilm"};
        hashTagSet={"Gravity","MetallicaThroughTheNever","RunnerRunner","ACOD","Parkland","BadMilo"};
        for line in response:
            tweet=json.loads(line);
            # if tweet is not empty
            if (ifTweetMentionsOneOfMovies(tweet,movieSet,hashTagSet)):
                print tweet;
                tweets.append(tweet);
                counter=counter+1;
            if (counter>=numOfTweets):
                break;
        return tweets;
    
    
    
twitter=Twitter();
tweets=twitter.downloadTweet(10000);

