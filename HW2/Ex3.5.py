# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:32:20 2014

@author: jvaccaro
"""

"Exercise 3-5"

def yoloswag(n):
    A = 5*'-'
    B = n*('+' + A) + '+'
    C = 5*' '
    D = n*('|'+C)+ '|'
    for i in xrange(n):
        print B
        print D
        print D
        print D
        print D
    print B

yoloswag(4)