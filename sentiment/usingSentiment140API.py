'''
Created on Nov 12, 2013

@author: ibogun2010
'''

import requests;
import json;
import re;
from csvWriting import writeToCsvFile;
from wx._misc import Sleep
import time;

def isDate(line):
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

def addFix(tweetText):
    prefix='{"text": "';
    postfix='", "query": "Captain Phillips", "topic": "movies"}';
    
    return prefix+tweetText+postfix;

def processResultOfRequest(csvFile,requestFromAPI):
    resp=json.loads(requestFromAPI.text);

    # reponse is a json file with only a 'data' field
    data=resp["data"];
    
    for index in range(len(data)):
        
        d=data[index];
        
        polarity=d["polarity"];
        text=d["text"];
        
        if polarity==4:
            polarity=1;
        elif polarity==2:
            polarity=0;
        elif polarity==0:
            polarity=-1;
        
        #print d["text"],d["polarity"];
        
        writeToCsvFile(csvFile, text, polarity);
        
    
movie='{"data": [{"text": "I love Titanic.", "query": "Captain Phillips", "topic": "movies"},{"text": "I hate Titanic.", "query": "Captain Phillips", "topic": "movies"}]}';

#r=requests.post("http://www.sentiment140.com/api/bulkClassifyJson?appid=ibogun2010@my.fit.edu",data=movie);


movieRequestPrefix='{"data": [';
movieRequestPostfix=']}';

f=open('../data/sentiment/allWeeksTweetTextForSentimentAnalysisWithTime.txt','r');

# skip the first date
line=f.readline();
param=movieRequestPrefix;

isFirst=True;

csvFile='sentimentsAll.csv';

# param=movieRequestPrefix+addFix(line)+movieRequestPostfix;
# print param;
# print movie;
# movie='{"data": [{"text": "I best Titanic.", "query": "CaptainPhillips", "topic": "movies"},{"text": "I hate Titanic.", "query": "CaptainPhillips", "topic": "movies"}]}';
# 
# r=requests.post("http://www.sentiment140.com/api/bulkClassifyJson?appid=ibogun2010@my.fit.edu",data=movie);
# processResultOfRequest(csvFile,r);
c=0;
times=0;
for line in f:
    if (isDate(line)):
        continue;
    if c>100:

        # send request and start new string
        param=param+movieRequestPostfix;
        #print data;
        print param;
        #print param;
        r=requests.post("http://www.sentiment140.com/api/bulkClassifyJson?appid=ibogun2010@my.fit.edu",data=param);
        processResultOfRequest(csvFile,r);
        time.sleep(2);
        param=movieRequestPrefix;
        
        c=0;
        isFirst=True;
    else:
        
        line=re.sub('\n',' ',line);
        if isFirst:
            param=param+addFix(line);
            isFirst=False;
        else:
            param=param+','+addFix(line);
        c=c+1;
        #print str;


# for line in f:
#     if (isDate(line)):
#         # send request and start new string
#         param=param+movieRequestPostfix;
#         #print data;
#         print line;
#         print param;
#         r=requests.post("http://www.sentiment140.com/api/bulkClassifyJson?appid=ibogun2010@my.fit.edu",data=param);
#         processResultOfRequest(csvFile,r);
#           
#         param=movieRequestPrefix;
#           
#         isFirst=True;
#     else:
#         
#         line=re.sub('\n',' ',line);
#         if isFirst:
#             param=param+addFix(line);
#             isFirst=False;
#         else:
#             param=param+','+addFix(line);
#         #print str;
    
    


f.close()




#processResultOfRequest('aa.csv', r);
    
# send 1000 requests and write everything into one big file without any dates