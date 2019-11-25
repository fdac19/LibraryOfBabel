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
    wholeString= filter(str.isalpha, wholeString) 
    for letter in alphabeltString:
        alphabetList.append(letter)
    letterCntDict=dict()
    letterFreqDict=dict()
    for letter in alphabeltString:
        letterCntDict[letter]=wholeString.count(letter)
        letterFreqDict[letter]=float(wholeString.count(letter))/len(wholeString)
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
    plt.show()
    return letterFreqDict
    
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

#text_10000= getStringFromFile("wiki-100k.txt")
#letterFreq(text_10000)
#
#collectionList=[]
#plotMatrix=[]
#
#samples=[]
#for i in range(1,100):
#    samples.append(i*100)
#
##samples=[100,200,400,800,1600,3200,6400,12800,]
#for i in samples:
#    print "Top %d"%i
#    partList=wordList[:i]
#    testString=""
#    for word in partList:
#        testString+=word
#    letterCntDict = letterFreq(testString)
#    letterFreqDict=dict()
#    plotList=[]
#    for key in letterCntDict:
#        cnt=letterCntDict[key]
#        freq=cnt/float(i)
#        letterFreqDict[key]=freq
##    print letterFreqDict
#    collectionList.append(letterFreqDict)
    
#freqMatrix=[] #each item in freqMatrix is character, going from a to z    
#plt.figure()
#alphabeltString="abcdefghijklmnopqrstuvwxyz"
#for letter in alphabeltString:
#    letterFreq=[]
#    for freqDict in collectionList:
#        letterFreq.append(freqDict[letter])
##    print letterFreq
#    plt.plot(samples[:100],letterFreq[:100],label=letter)
#ax = plt.gca()
#plt.xlabel("Most Common Words")
#plt.ylabel("Letter Frequency")
#plt.legend(bbox_to_anchor=(1.2, 1.1), bbox_transform=ax.transAxes) 
#plt.show()
#
#plt.figure()
#
#alphabeltString="eh"
#for letter in alphabeltString:
#    letterFreq=[]
#    for freqDict in collectionList:
#        letterFreq.append(freqDict[letter])
##    print letterFreq
#    plt.plot(samples,letterFreq,label=letter)
#ax = plt.gca()
#plt.xlabel("Most Common Words")
#plt.ylabel("Letter Frequency")
#plt.legend(bbox_to_anchor=(1.2, 0.5), bbox_transform=ax.transAxes) 
#plt.show()
#

#
#grim= getStringFromFile("10000.txt")
#newDict= letterFreq(grim,title="Letter Usage in Grim's Fairy Tail")
#print newDict['h']
#print newDict['e']
#print
#
#grim= getStringFromFile("pp.txt")
#newDict= letterFreq(grim,title="Letter Usage in Pride and Prejudice")
#print newDict['h']
#print newDict['e']
#print
#
#grim= getStringFromFile("paper.txt")
#newDict= letterFreq(grim,title="Letter Usage in Acdemic Paper Collection")
#print newDict['h']
#print newDict['e']
#print 
#
#grim= getStringFromFile("copyRightLaw.txt")
#newDict= letterFreq(grim,title="Letter Usage in Copy Right Law")
#print newDict['h']
#print newDict['e']
#print 
#
#grim= getStringFromFile("grim.txt")
#newDict= letterFreq(grim,title="Letter Usage in Acdemic Paper Collection")

grim= getStringFromFile("bab1.txt")
newDict= letterFreq(grim,title="Letter Usage in a random babel page")

grim= getStringFromFile("bab2.txt")
newDict= letterFreq(grim,title="Letter Usage in a random babel page")

#print wholeString