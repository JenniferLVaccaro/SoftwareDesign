# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:59:52 2014

@author: jvaccaro
"""

"Exercise 6.1"

"""
Write a
compare
function that returns
1
if
x > y
,
0
if
x == y
, and
-1
if
x < y"""

def compare(x, y):
    a = x - y
    if a>0:
        print 1
    elif a == 0:
        print 0
    else:
        print -1