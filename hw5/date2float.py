# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:48:52 2014

@author: jvaccaro
"""

def date2float(Dates):
    '''
        Takes a list of dates in string form and makes them into
        a list of usable floats, for plotting purposes.
    '''
    F = []
    for i in range(len(Dates)):
        d = Dates[i]
        m = d[:3]
        d = d[5:]
        Months = {'jan':0,'feb':31,'mar':59,'apr':}
        m = get(Months(m))
        F.append(int(m)+int(d))
    return F
