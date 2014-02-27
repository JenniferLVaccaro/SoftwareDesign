# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:41:45 2014

@author: jvaccaro
"""
from pattern.web import *


def get_data():
    """
        Gets the data out of twitter or facebook, saves it
        as a string.
        Ins: none
        Outs: string of all data, fairly raw with annoying things.
    """
    query = {'q': '[my search text here]', 'sc':'typd'}
    twitter_search_url = 'https://twitter.com/lordemusic' #twit
    twit = twitter_search_url
    
    url = URL(string=twit, method=GET, query=query)
    with open('test.txt','wb') as f:
        f.write(url.read())
        
    with open('test.txt','wb') as f:
        content = f.read()
        
    yolo = content.index('div.class="content">')    
    
    content[index:index+1000]
    html = open('test.txt','r'.read())
    d = pq(html)
    d('div.content')
    
    li[0].text_content