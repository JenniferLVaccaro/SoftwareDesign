# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:57:25 2014

@author: jvaccaro
"""

from math import *
print "hayy"
def get_complementary_base(n):
    """
    Takes a base, returns its complement. Prints error message if invalid.
    """
    if n == 'A':
        return 'T'
    elif n == 'C':
        return 'G'
    elif n == 'T':
        return 'A'
    elif n == 'G':
        return 'C'
    else:
        print "error! invalid input!"
        
def is_between(x,y,z):
    if y<z:
        if y>x:
            return "true"
    elif y>z:
        if y<x:
            return "true"
    else:
        return "false"
        
def random_float(start,stop):
    from random import random
    return random()* (stop-start) + start
