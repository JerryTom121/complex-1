'''
Created on Nov 9, 2013

@author: ivan
'''
import re;

import numpy as np;
import matplotlib as plt
import pylab;



p = re.compile("\d{4}-\d{1,2}-\d{1,2}");

def ifDate(line):
    a = p.match(line);
    
    if (a is None):
        return False;
    else:
        return True;
    
def getDate(line):
    '''
    If line contains the date return it.
    '''
    
    a = p.match(line);
    return a.group();

f = open('../data/CaptainPhillips.txt');

d=dict();
d
# d['2013-10-12']=1;
# 
# for key, value in d.iteritems():
#     print key, value;
# print d['2013-10-132']
data=np.zeros(28);
np.array
c=0;
lastDate='';
for line in f:
    if (ifDate(line)):
        
        if lastDate!=getDate(line):
            c=c+1;
            
            #nothing
            d[getDate(line)]=0;
            lastDate=getDate(line);
        print getDate(line);
    else:
        d[lastDate]=d[lastDate]+1;
        data[c-1]=data[c-1]+1;
print data;
y=np.arange(28);

plt.pylab.plot(y,data);
pylab.show();
#print d.__len__();
# for key,value in d.iteritems():
#     print key,value;        
f.close();