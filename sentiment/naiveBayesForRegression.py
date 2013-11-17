'''
Created on Nov 16, 2013

@author: ibogun2010
'''
import csv;
import re;

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from process.NaturalLanguageProcessing import nlpPreProcessing;
import ast;

def ifDate(line):
    p = re.compile("\d{4}-\d{1,2}-\d{1,2}");
    a = p.match(line);
    
    if (a is None):
        return False;
    else:
        return True;
    
def getDate(line):
    '''
    If line contains the date return it.
    '''
    
    p = re.compile("\d{4}-\d{1,2}-\d{1,2}");
    
    a = p.match(line);
    return a.group();




def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
allNegfeats=len(negfeats); 
 
trainfeats = negfeats + posfeats;
#print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats);

f=open('../data/CaptainPhillips.txt');

countPositive=0;
countNegative=0;
d=dict();
total=0;
for line in f:
    
    if ifDate(line):
        date=getDate(line);
        d[date]=[0,0];
    else:
        try:
            a = ast.literal_eval(line);
        except SyntaxError:
            continue;
        # get tweet text
        tweetText = a.get("text");
        # print text;
        words = nlpPreProcessing(tweetText);
        
        total=total+1;
        
        feature=word_feats(words);
        label=classifier.classify(feature);
        
        if label=='pos':
            countPositive=countPositive+1;
            d[date][0]=d[date][0]+1;
            
        if label=='neg':
            #print line;
            countNegative=countNegative+1;
            d[date][1]=d[date][1]+1;
 
writer = csv.writer(open('timeDataForRegression.csv', 'wb'))
for key, value in d.items():
    writer.writerow([key, value[0],value[1]]);
        
print 'Total number tweets: '+str(total);
print 'Positive tweets: '+str(countPositive/(total*1.0));
print 'Negative tweets: '+str(countNegative/(total*1.0));
