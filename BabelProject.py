#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:10:42 2019

@author: lu
"""

from library_of_babel import LoB
import random
import string
import matplotlib.pyplot as plt
import numpy as np
lob=LoB()

keyword="trash"
address=lob.search(keyword)
print address
page= lob.getPage(address)

index=page.find(keyword)
print page[index:index+len(keyword)+10]



keyword="garbage"
address=lob.search(keyword)
#print address
page= lob.getPage(address)
index=page.find(keyword)
#print page[index:index+len(keyword)+10]

babelString=""
for i in range(0,100):
    randomString = ''.join([random.choice(string.ascii_lowercase) for n in xrange(16)])
    try:
        address=lob.search(randomString)
    #print address
        page= lob.getPage(address)
        babelString+=page
    except:
        print "cant find"




def letterFreq(wholeString,yLabel="Letter Frequencies",title="title"):
    alphabeltString=string.ascii_lowercase
    print alphabeltString
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
    freqList=[]
    for tup in sorted_x:

        keyList.append(tup[0])
        cntList.append(int(tup[1]))
        freqList.append(float(tup[1])/len(wholeString))
    
    objects = keyList
    y_pos = np.arange(len(objects))
    performance = freqList
    plt.figure()
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()
    return letterFreqDict

letterFreq(babelString.lower(),title="Letter Frequency of 100 babel pages")