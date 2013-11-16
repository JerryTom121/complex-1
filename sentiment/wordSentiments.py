'''
Created on Nov 16, 2013

@author: ivan
'''

import csv;
import nltk;
from download.filters import deletePunctuation;


dict=dict()



with open('../data/sentiment/sentimentProcessed.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for row in spamreader:
        #print row[0],row[1];
        
        text=deletePunctuation(row[0]);
        score=int(row[1]);
        textTokens = nltk.word_tokenize(row[0]);
        
        # for every word in the list
        for index in range(len(textTokens)):
            word=textTokens[index];
            
            # check if it is already in the dictionary
            if not word in dict:
                # create new entry in the dictionary
                dict[word]=[0,0];
                # if it is, increment respective counter ( positive or negative)
            counters=dict[word];
            if score==1:
                # positive counter
                counters[0]=counters[0]+1;
            else:
                # negative counter
                counters[1]=counters[1]+1;
                
               
writer = csv.writer(open('wordSentiments.csv', 'wb'))
for key, value in dict.items():
    writer.writerow([key, value[0],value[1]]);