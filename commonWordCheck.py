#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:36:51 2019

@author: lu
"""
import re
import nltk


f=open("500.txt","r+")
lines=f.readlines()
commonWordSet=set()
for line in lines:
    word=line.rstrip()
    
    commonWordSet.add(word.lower())  

#import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def cleanWord (w):
    # r in r'[.,"\']' tells to treat \ as a regular character 
    # but we need to escape ' with \'
    # any character between the brackets [] is to be removed 
    wn = re.sub('[,"\.\'&\|:@>*;/=]', "", w)
    nw=re.sub('^[0-9\.]*$', "", wn)# get rid of numbers
    nw=re.sub(r'[^\w\s]','',nw)
    word=WordNetLemmatizer().lemmatize(nw,'v')
    return word

def processFile(fname):
    f=open(fname,"r+")
    wordList=[]
    lines=f.readlines()
    for line in lines:
        line=line.rstrip()
        splitList=line.split(" ")
        for item in splitList:
            word=cleanWord(item)
            if len(word)==0:
                continue
            wordList.append(word)
    return wordList

def checkCommonWordRate(wordList,commonWordSet):
    cnt=0
    for word in wordList:
        if word in commonWordSet or (word+"s") in commonWordSet:
            cnt+=1
    return cnt/float(len(wordList))
            

wordList=processFile("pp.txt")
print checkCommonWordRate(wordList,commonWordSet)    

wordList=processFile("500.txt")
print checkCommonWordRate(wordList,commonWordSet)    

wordList=processFile("grim.txt")
print checkCommonWordRate(wordList,commonWordSet)    

wordList=processFile("paper.txt")
print checkCommonWordRate(wordList,commonWordSet)   

wordList=processFile("copyRightLaw.txt")
print checkCommonWordRate(wordList,commonWordSet)   
