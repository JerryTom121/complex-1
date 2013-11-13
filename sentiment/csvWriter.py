'''
Created on Nov 13, 2013

@author: ibogun2010
'''
import csv;

total=0;
positive=0;
neutral=0;
negative=0;
tot=0;
with open('../data/sentiment/processedAllWeeksTweetsWithoutTime.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        x=int(row[0]);
        
        if x==4:
            positive=positive+1;
            tot=tot+1;
        elif x==2:
            neutral=neutral+1;
        elif x==0:
            negative=negative+1;
            tot=tot+1;
        total=total+1;

total=total*1.0;
tot=tot*1.0;
print "total: "+str(total);
print "positive: "+str(positive/tot);
print "negative: "+str(negative/tot);
print "neutral: "+str(neutral/total);    


print negative;