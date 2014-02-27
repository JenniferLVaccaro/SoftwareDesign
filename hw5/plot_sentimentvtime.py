# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:50:34 2014

@author: jvaccaro
"""



def plot_sentimentvtime(t, sentiments):
    '''
        This takes the date and makes the date into a usable float, probably
        in 0-365.0 days depending on the scope of the data.
        Ins: list of strings correspong to dates
        Outs: list of floats corresponding to dates
    '''
    