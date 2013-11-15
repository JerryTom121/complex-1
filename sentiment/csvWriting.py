'''
Created on Nov 13, 2013

@author: ibogun2010
'''


import csv


def writeToCsvFile(csvFilename,tweetText,polarity):

    with open(csvFilename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([tweetText]  + [polarity])


f=open('../data/sentiment/allWeeksTweetTextForSentimentAnalysis.txt','r');
out=open('forStanfordSentimentAnalysis','a');
for line in f:
    splitStr=line.split();
    
    for index in range(len(splitStr)):
        out.write(splitStr[index]+'\n\n');


f.close();
out.close();
    