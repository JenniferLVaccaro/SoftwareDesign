# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:48:50 2014

@author: jvaccaro
"""
from pattern.web import *


def listify_dates(L):
    """
        Takes a list of strings and makes it into a list of seperate dates.        
        Ins: raw list
        Outs: [Dates]
    """
    Dates = []
    for i in range(len(L)):
        k = L[i]
        search1 = k.find('-')
        search2 = k[search1:].find('.')
        date = k[search1:search2]
        Dates.append(date)
    return Dates

def listify_tweets(L):
    """
        Takes a list of strings and makes it into a list of seperate tweets.        
        Ins: raw list
        Outs: [Tweets]
    """
    Tweets = []
    for i in range(len(L)):
        k = L[i]
        search1= k.find('@lordemusic')
        search2= k.find(':')
        tweet = k[search1+44:search2-2]
        Tweets.append(tweet)
    return Tweets