# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:11:58 2014

@author: jvaccaro
"""

#texanalysis
#data stuff: python twitter api
#plotting: "numpi"

def get_data():
    """
        Gets the data out of twitter or facebook, saves it
        as a string.
        Ins: none
        Outs: string of all data, fairly raw with annoying things.
    """

def listify(String):
    """
        Takes a string and makes it into a list of seperate tweets, and 
        another with all of the dates.        
        Ins: string with dates and times
        Outs: [dates, tweets]
    """

def get_sentiment(Tweets):
    '''
        Takes the list of tweets and gets the sentiment floats.
        Ins: list of tweets in string form
        Outs: list of tuples [(sentiments, subjectivity)]
    '''

def date2float(dates):
    '''
        Takes a list of dates in string form and makes them into
        a list of usable floats, for plotting purposes.
    '''
    
def plot_sentimentvtime(t, sentiments):
    '''
        This takes the date and makes the date into a usable float, probably
        in 0-365.0 days depending on the scope of the data.
        Ins: list of strings correspong to dates
        Outs: list of floats corresponding to dates
    '''
        
        
def compare_subjectivity(data1, data2):
    '''
        This places the plots of two data sources on the same
        plot, and compares the average subjectivity of each.
        MAKE THIS PART DO WORK:
            Were they authored by the same person?
            Do they reflect other events?
            Which data sources showed highest ranges/net positivity
        Ins: both/all datas of whatever we are doing
        Outs: Picture showing what we need
    '''
