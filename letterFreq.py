#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:04:13 2019

@author: lu
"""

import string

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def letterFreq(wholeString,yLabel="Letter Frequencies",title="title"):
    alphabeltString=string.ascii_lowercase
    alphabetList=[]
    for letter in alphabeltString:
        alphabetList.append(letter)
    letterCntDict=dict()
    for letter in alphabeltString:
        letterCntDict[letter]=wholeString.count(letter)
    sorted_x = sorted(letterCntDict.items(), key=lambda x: x[1])
    keyList=[]
    cntList=[]

    for tup in sorted_x:

        keyList.append(tup[0])
        cntList.append(int(tup[1]))

    
    objects = keyList
    y_pos = np.arange(len(objects))
    performance = cntList
    plt.figure()
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel(yLabel)
    plt.title(title)
#    plt.show()
    return letterCntDict
    
wordList=[]

def getStringFromFile(fname):
    global wordList
    f=open(fname,"r+")
    lines=f.readlines()
    f.close()
    
    wordList=[]
    for line in lines:
        wordList.append(line.rstrip())
        
    wholeString=""
    for word in wordList:
        wholeString+=word
    return wholeString.lower()

text_10000= getStringFromFile("wiki-100k.txt")
letterFreq(text_10000)

for i in [100,200,400,800,1600,3200,6400,12800,25600,51200,1000000]:
    print "Top %d"%i
    partList=wordList[:i]
    testString=""
    for word in partList:
        testString+=word
    letterCntDict = letterFreq(testString)
    print letterCntDict







#
#grim= getStringFromFile("10000.txt")
#letterFreq(grim,title="Letter Usage in Grim's Fairy Tail")
#
#grim= getStringFromFile("pp.txt")
#letterFreq(grim,title="Letter Usage in Pride and Prejudice")
#
#
#grim= getStringFromFile("paper.txt")
#letterFreq(grim,title="Letter Usage in Acdemic Paper Collection")
#
#grim= getStringFromFile("copyRightLaw.txt")
#letterFreq(grim,title="Letter Usage in Copy Right Law")
#
#grim= getStringFromFile("wiki-100k.txt")
#letterFreq(grim,title="Letter Usage in Acdemic Paper Collection")





#print wholeString