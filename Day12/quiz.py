# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 13:35:48 2014

@author: jvaccaro
"""

#quiz script

def exclusive_or_dict(d1, d2):
    dict = {}
    for i in d1:
        if i not in d2:
            dict[i] = d1[i]
    for j in d2:
        if j not in d1:
            dict[j] = d2[j]
    return dict
    
d1 = {'a':1, 'b':2}
d2 = {'b':1, 'c':3}
print exclusive_or_dict(d1, d2)