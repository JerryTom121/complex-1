'''
Created on Sep 25, 2013

@author: Ivan Bogun

'''

import enchant
import string

dictionaryUS = enchant.Dict("en_US");


def ifTweetMentionsOneOfMovies(tweet,movieNames,hashtagSet,keywords):
    
    if (ifTweetContainsText(tweet) is False):
        return False;
    
    text=tweet.get("text");
    
    if (ifSentenceIsEnglish(text)is False):
        return False;
    
    entities=tweet.get("entities");
    
    
    if(isTextIsSubset(text, keywords)):
        return True;
     
     
    # if there are no entities
#     if (len(entities) is 0):
#         return False;
    
    #print tweet.get("text");
    
    user_mentions=entities.get("user_mentions");
    hashTags=entities.get("hashtags");
   
    
    for mention in user_mentions:
        screen_name=mention.get("screen_name");
        
        # if at least one of movies is mentioned
        for movie in movieNames:
            if (screen_name.lower()==movie.lower()):
                return True;
        
    # at least one of hashtags is mentioned
    for hashtag in hashTags:
        hashtagText=hashtag.get("text");
        
        for ht in hashtagSet:
            if (ht.lower()==hashtagText.lower()):
                return True;
    
    
    
    return False;


def ifTweetContainsText(tweet):
    
    tweetHasText=True;
    if (tweet.get("text") is None):
        tweetHasText=False;
        
    return tweetHasText; 

def ifWordIsEnglish(word):
    '''
    check if the word belongs to English
    '''
    
    return dictionaryUS.check(word);

def ifSentenceIsEnglish(sentence):
    '''
    Classifies the sentence as 'English' if more than half of the words are
    correctly written.
    '''
    words=sentence.split();
    totalWords=0;
    wordsNotInEnglish=0;
    for word in words:
        totalWords=totalWords+1;
        if (ifWordIsEnglish(word) is not True):
            wordsNotInEnglish=wordsNotInEnglish+1;
           
    if (wordsNotInEnglish>0.5*totalWords):
        return False;
     
    return True;
    
    
def isTextIsSubset(text,keywords):
    
    text=text.lower();
    strArray=text.split();
    textSet=set(strArray);
    
    for key,value in keywords.iteritems():
        
        valueSet=set(value);        
        if (valueSet<=textSet):
            return True;
        
    return False;
        
    
def isASCII(character):
    '''
    checks if the character is the ASCII character between 0-128
    '''
    ascii=ord(character);
    if (ascii>=0 and ascii<=128):
        return True;
    return False;

def isSentenceEnglishUsingASCII(sentence):
    '''
    Iterates through each character checking if each character is 
    an English one.    
    '''
    characters=list(sentence);
    
    isEnglish=True;
    
    for char in characters:
        if (isASCII(char)==False):
            isEnglish=False;
            
    return isEnglish;

def deletePunctuation(sentence):
    '''
    Function deletes all punctuation from the sentence.
    '''
    out = sentence.translate(string.maketrans("",""), string.punctuation);
    return out;
