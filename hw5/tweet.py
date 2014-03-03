# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:13:40 2014

@author: mwelches
"""
from pattern.web import *
from pyquery import PyQuery as pq

t = Twitter()

res = t.search('search text here')

query = {'q': '[my search text here]','src':'typd'}
twitter_search_url = 'https://twitter.com/lordemusic' #twit
twit = twitter_search_url # aliasing

url = URL(string=twit,method=GET,query=query)

with open('test.txt','wb') as f: #turns it into text!!!
     f.write(url.read())

with open('test.txt','rb') as f:
    content = f.read()
    
index = content.index('div class="content">')
content[index:index+1000]

html = open('test.txt','r').read() #read from file 'test.txt'
d = pq(html)
li = d("div.content") # gives you all the div tags that have content class in a list format
li[0].text_content() # get the content of html code in li[0]
print li[15].text_content().replace('\n','').strip() # replace spaces with empty strings, [#], where # is the tweet you want