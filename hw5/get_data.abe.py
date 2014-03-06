# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 17:23:08 2014

@author: jvaccaro
"""
from pattern.web import *
from pyquery import PyQuery as pq

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

def get_data(url="https://twitter.com/", handle="lordemusic"):
     """
         Gets the data out of twitter or facebook, saves it
         as a string.
         Ins: none
         Outs: string of all data, fairly raw with annoying things.
     """
    data = pq(url + handle) # get data from url address (url + handle)

    # div.content are the html codes where tweets are stored. So we're gonna get all of them.

    li = data("div.content") # gives you all the div tags that have content class in a list format

    return li[15].text_content().replace('\n','').strip() # get the content of html code in li[#] and replace spaces with empty strings, [#], where # is the tweet you want