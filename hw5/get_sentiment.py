# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:48:51 2014

@author: jvaccaro
"""
from pattern.en import *

def get_sentiment(Tweets):
    '''
        Takes the list of tweets and gets the sentiment floats.
        Ins: list of tweets in string form
        Outs: list of tuples [(sentiments, subjectivity)]
    '''
    K = []
    for i in range(len(Tweets)):
        scent = sentiment(str(Tweets[i]))
        K.append(scent)
    return K