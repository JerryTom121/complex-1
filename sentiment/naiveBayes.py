'''
Created on Nov 11, 2013

@author: ivan
'''
import csv;




import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
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

f=open('../data/sentiment/allWeeksTweetTextForSentimentAnalysis.txt','r');

countPositive=0;
countNegative=0;
total=0;

csvFilename='sentimentProcessed.csv';

with open(csvFilename, 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for line in f:
        total=total+1;
        feature=word_feats(line.split());
        
        label=classifier.classify(feature);
        
        if label=='pos':
            countPositive=countPositive+1;
            polarity=1;
            
        if label=='neg':
            #print line;
            countNegative=countNegative+1;
            polarity=-1;
            
        writer.writerow([line]  + [polarity])





        
print 'Total number tweets: '+str(total);
print 'Positive tweets: '+str(countPositive/(total*1.0));
print 'Negative tweets: '+str(countNegative/(total*1.0));
# print 'accuracy:', nltk.cla'ssify.util.accuracy(classifier, t/toestfeats)
# classifier.show_most_informative_features()