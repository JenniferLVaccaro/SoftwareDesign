# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:48:50 2014

@author: jvaccaro
"""
from pattern.web import *


def listify():
    """
        Takes a string and makes it into a list of seperate tweets, and 
        another with all of the dates.        
        Imports: content.index thingy
        Outs: [dates, tweets]
    """
    
    with open('test.txt','wb') as f:
        f.write
    content = f.read()
    yolo = content.index('div.class="content">')
    content[yolo:yolo+1000]
    
    
    
    content[index:index+1000]
    html = open('test.txt','r'.read())
    d = pq(html)
    d('div.content')    
    
    li[0].text_content