# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:56:47 2014

@author: jvaccaro
"""

def factorial(n):
    q = 1
    for i in range(1,n+1):
        q = i*q
    return q
    
print factorial(5)
print factorial(6)