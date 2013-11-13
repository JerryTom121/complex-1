'''
Created on Oct 19, 2013

@author: ivan
'''
import re;
import ast
import enchant
from igraph import *
import json
import string

from NaturalLanguageProcessing import *;


import nltk;


dictionaryUS = enchant.Dict("en_US");



def findIndex(graph, vertexName):
    '''
    From Vertex Object get it's ID
    '''
    result = 0;
    try:
        result = graph.vs.find(name=vertexName).index;
    except:
        pass;
        result = -1;
    return result;

def deletePunctuation(sentence):
    '''
    Function deletes all punctuation from the sentence.
    '''
    out = sentence.translate(string.maketrans("", ""), string.punctuation);
    return out;

def processTweet(graph, words):
    
    # for every word in the word list
    for index in range(len(words)):
        
        # get the word
        word1 = words[index];
        
        # replace everything non alphabetical-numerical with nothing.
        word1 = re.sub('\W', '', word1);
        
        # find vertex ID
        id1 = findIndex(graph, word1);
        
        # if the word is not in the graph, add a new vertex
        if (id1 == -1):
            graph.add_vertex(word1);
            id1 = findIndex(graph, word1);
        
        # the index of the next word in the sentence
        index2 = index + 1;
        
        # for all words coming after this one do
        while (index2 < len(words)):
            word2 = words[index2];
            index2 = index2 + 1;
            word2 = re.sub('\W', '', word2);
            # find vertex ID
            id2 = findIndex(graph, word2);
        
            # if the word is not in the graph, add a new vertex
            if (id2 == -1):
                graph.add_vertex(word2);
                id2 = findIndex(graph, word2);
            
            if (word1 == word2):
                continue;
            
#             eid = graph.get_eid(id1, id2);
#             edge = graph.es[eid]
            
            
            try:
                eid = graph.get_eid(id1, id2)
            except:
                eid = graph.ecount()
                graph.add_edge(id1, id2, weight=1)
            edge = graph.es[eid];
            edge["weight"] += 1
            
            
        # return graph;
            
            

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

f = open('../data/CaptainPhillips.txt');

graphDate = "2013-10-12";
date = "";
c = 0;


# create a graph
g = Graph(0);
# g.es["weight"]=0;

dateFrom='2013-11-02';
dateUpTo='2013-11-09';

outFile = open('allWeeksTweetTextForSentimentAnalysisWithoutTime.txt','w')
#f.write('hi there\n') # python will convert \n to os.linesep



startGettingTweets=True;

# for line in the text do
for line in f:
    
  
    
    # check if the line contains the date (special line where the time of the tweets is saved)
    isDate = ifDate(line);
    if isDate:
        
        if (getDate(line)!=date):
            a=1;
            #outFile.write(getDate(line)+'\n');
#         
#         date = getDate(line);
#         
#         if (date==dateUpTo):
#             break;
#         
#         if (dateFrom==date):
#             startGettingTweets=True;
        #print date;
        
        # only one graph now, if the date changed -> create new graph* (not implemented yet)
#         if (graphDate != date):
#             break;
    else:
        # do Graph staff here
#         p1=re.compile("{.*}");
#         line=p1.match(line);
#         line=line.group();

#         if not startGettingTweets:
#             continue;
        #parse string into the dictionary
        try:
            a = ast.literal_eval(line);
        except SyntaxError:
            continue;
        # get tweet text
        tweetText = a.get("text");
        c = c + 1;
        # print text;
        #words = nlpPreProcessing(tweetText);
        outFile.write(tweetText+'\n');
        
        #processTweet(g, words);


outFile.close();    
print("Number of tweets: " + str(c));
#g.write_graphml("weak4.graphml");
