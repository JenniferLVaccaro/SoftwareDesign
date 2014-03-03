# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:11:58 2014
Hey Ninjas!
So, here's our (Mika's and Jenny's) Homework 5 code!
We wanted to look at sentiment of celebrities over time using their Twitter accounts.
We extract tweets from the month of February (get_data) and parse out tweets and dates. 
(listify_dates and listify_tweets) We also filter out retweets from 
other users. Then, we calculate the positivity of sentiment and plot it vs.
the date.
We expected to see a greater response to Valentine's Day on the 14th, but no such luck.
The graphs created by this project are included in the same folder.
@author: jvaccaro
"""
from pattern.web import *
from pattern.en import *
from pyquery import PyQuery as pq
from matplotlib.pyplot import *

#texanalysis #Abe gave us advice about what programs to use
#data stuff: python twitter api
#plotting: "numpi"

def get_data(url, handle):
    """
        Gets the data out of twitter , saves it
        as a list of oddly formatted strings.
        Ins: handle = "https://twitter.com/" and twitter handle
        Outs: string of all data, fairly raw with annoying formatting things.
    """
    data = pq(url + handle) # get data from url address (url + handle)
    # div.content are the html codes where tweets are stored. So we're gonna get all of them.

    li = data("div.content") # gives you all the div tags that have content class in a list format
    return li

#    return li[n].text_content().replace('\n','').strip() #easier to put later, because works individual elements separately.
    
def listify_dates(L, handle):
    """
        Takes a rough list of strings from the tweets and makes it into a 
        list of integer dates.        
        Parses out the day of the month.        
        Ins: raw list, twitter handle (for filtering reasons)
        Outs: [Dates]
    """
    Dates = []
    for i in range(3,len(L)):
        k = L[i].text_content().replace('\n','') #gets rid of annoying spacing
        search0 = k.find('@'+handle)+len(handle)+1 #filters out retweets
        
        search1 = k[search0:].find('Feb')+search0+4
        search2 = 2+search1
        date = k[search1:search2]            
        date = date.strip()
        
        if len(date) != 0:
            Dates.append(int(date))

    return Dates

def listify_tweets(L, handle):
    """
        Takes a string and makes it into a list of seperate tweets.        
        Parses out the text of a tweet.        
        Ins: raw list, twitter handle #for filtering reasons
        Outs: [Tweets]
    """
    Tweets = []
    for i in range(3,len(L)):
        k = L[i].text_content().replace('\n','') #gets rid of annoying spacing
        
        search1= k.find('@'+handle)+len(handle)+40 #if this is a retweet, the original handle will probably not appear. At least I hope not!
        search2= k[search1:].find('Expand')+search1        
        tweet = k[search1:search2].strip()
        
        if '   ' in tweet: #gets rid of annoying data at the end of a tweet (Options, Expand and such)
            tweet = tweet[:(tweet.find('   ')+1)]

        Tweets.append(str(tweet))

    return Tweets
    
def filter_yolo(L):
    '''
        Filters empty entries out of lists yay! This is how we could get rid of retweets
        Ins: Disgusting list with empty entries
        Outs: Beautiful filtered list
    '''
    K = []
    for i in L:
        if len(i) != 0:
            K.append(i)

    return K    

def get_sentiment(Tweets):
    '''
        Takes the list of tweets and gets the sentiment floats.
        Ins: list of tweets in string form
        Outs: list of floats [sentiments]
    '''
    K = []

    for i in range(len(Tweets)):
        scent = sentiment(Tweets[i])[0]
        K.append(scent)

    return K    
    
def test1():
    '''
        Tests the above functions
        Outs depend on what is commented and not.
    '''    
    L = get_data("https://twitter.com/", "lordemusic")

    return listify_dates(L, "lordemusic")

#    return get_sentiment(filter_yolo(listify_tweets(L, "lordemusic")))
#    return filter_yolo(listify_tweets(L, "lordemusic"))
    
def plot_sentimentvtime(handle):
    '''
        This plots the sentiment positivity vs. time with a well-labelled 
        graph, which can be saved for happiness.
        Ins: Twitter handle of celebrity (or anyone)
        Outs: Well-labelled graph
    '''
    L = get_data("https://twitter.com/", handle)
    T = listify_dates(L, handle)
    Y = get_sentiment(filter_yolo(listify_tweets(L, handle)))
    Y = Y[:(len(Y)-1)] 

    plot(T, Y,'r.-')
    title(handle+"'s Sentiment Over Time")
    xlabel("Time (Days in February)")
    ylabel("Sentiment (-1 to 1)")
    show()
        
#print test1()
plot_sentimentvtime('zellly1')