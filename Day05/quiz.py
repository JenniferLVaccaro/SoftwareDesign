# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:55:54 2014

@author: jvaccaro
"""

def hinge(n):
    if n<0:
        return 0
    return n
    
hinge(-4)
hinge(5)

def print_number_of_days(n):
    if n == 1:
        print 'Input is 1 day"
    else:
        print "Input is" + n + "days"
        
print_number_of_days(1)
print_number_of_days(3)