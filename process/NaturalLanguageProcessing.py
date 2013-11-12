'''
Created on Nov 2, 2013

@author: Ivan Bogun
'''

import nltk;
import ast
from download.filters import ifWordIsEnglish
import re;


def nlpPreProcessing(tweetText):
    
    # delete captains mention
    tweetText=re.sub('captain|phillips','',tweetText,flags=re.IGNORECASE);
    tweetText=re.sub('RT','',tweetText);
    #print tweetText;
    
    # split into seperate tokens
    textTokens = nltk.word_tokenize(tweetText);
    
    posTokens=nltk.pos_tag(textTokens);
    
    outputList=[];
    for index in range(len(posTokens)):
        posToken=posTokens[index];
        
        if isInformativePartOfTheSpeech(posToken[1]) and ifWordIsEnglish(posToken[0]):
            outputList.append(posToken[0]);
            
    return outputList;

def fromListGetString(nlpProcessedText):
    str=' '.join(nlpProcessedText);
    return str;
    
def isInformativePartOfTheSpeech(w):
    if w=='JJ' or w=='NN' or w=='VBP' or w=='NNP' or w=='VB' or w=='RB' or w=='VBG':
        
        return True;
    return False;