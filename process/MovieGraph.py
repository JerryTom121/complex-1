'''
Created on Oct 19, 2013

@author: ivan
'''
import re;
from igraph import *
import json
import ast
import enchant
import string

dictionaryUS = enchant.Dict("en_US");

p=re.compile("\d{4}-\d{1,2}-\d{1,2}");

def findIndex(graph,vertexName):
    '''
    From Vertex Object get it's ID
    '''
    result=0;
    try:
        result=graph.vs.find(name=vertexName).index;
    except:
        pass;
        result=-1;
    return result;

def deletePunctuation(sentence):
    '''
    Function deletes all punctuation from the sentence.
    '''
    out = sentence.translate(string.maketrans("",""), string.punctuation);
    return out;

def processTweet(graph,words):
    
    for index in range(len(words)):
        
        word1=words[index];
        
        word1=re.sub('\W', '', word1);
        # find vertex ID
        id1=findIndex(graph, word1);
        
        # if the word is not in the graph, add a new vertex
        if (id1 == -1):
            graph.add_vertex(word1);
            id1=findIndex(graph, word1);
        
        index2=index+1;
        while (index2<len(words)):
            word2=words[index2];
            index2=index2+1;
            word2=re.sub('\W', '', word2);
            # find vertex ID
            id2=findIndex(graph, word2);
        
            # if the word is not in the graph, add a new vertex
            if (id2 == -1):
                graph.add_vertex(word2);
                id2=findIndex(graph, word2);
            
            if (word1==word2):
                continue;
            
#             eid = graph.get_eid(id1, id2);
#             edge = graph.es[eid]
            
            
            try:
                eid = graph.get_eid(id1, id2)
            except InternalError:
                eid = graph.ecount()
                graph.add_edge(id1, id2, weight=1)
            edge = graph.es[eid];
            edge["weight"] += 1
            
            
        #return graph;
            
            

def ifDate(line):
    a=p.match(line);
    
    if (a is None):
        return False;
    else:
        return True;
    
def getDate(line):
    '''
    If line contains the date return it.
    '''
    
    a=p.match(line);
    return a.group();

f = open('CaptainPhillips.txt');

graphDate="2013-10-12";
date="";
c=0;


# create a graph
g = Graph(0);
#g.es["weight"]=0;
for line in f:
    
    if (line =="\n"):
        print "hello there";
    
    c=c+1;
    isDate=ifDate(line);
    if isDate:
        date=getDate(line);
        
        # only one graph now
        if (graphDate != date):
            break;
    else:
        # do Graph staff here
#         p1=re.compile("{.*}");
#         line=p1.match(line);
#         line=line.group();


        a=ast.literal_eval(line);
        text=a.get("text");
        
        #print text;
        words=text.split();
        processTweet(g,words);
#         summary(g);
        #print words;
        a=1;

print("Number of tweets: "+str(c));
g.write_graphml("10-12.graphml");