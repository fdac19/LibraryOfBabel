#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:10:42 2019

@author: lu
"""

from library_of_babel import LoB

lob=LoB()


keyword="trash"
address=lob.search(keyword)
print address
page= lob.getPage(address)

index=page.find(keyword)
print page[index:index+len(keyword)+10]



keyword="garbage"
address=lob.search(keyword)
print address
page= lob.getPage(address)
index=page.find(keyword)
print page[index:index+len(keyword)+10]