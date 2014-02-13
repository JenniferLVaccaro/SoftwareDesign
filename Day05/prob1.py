# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:56:21 2014

@author: jvaccaro
"""

def sum2list(L):
    S = []    
    S.append(L[0])
    for i in range(1,len(L),1):
        S.append(L[i]+S[i-1])
    return S
    
L = [1, 2, 3]

S = sum2list(L)
print S