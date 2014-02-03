# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:47:50 2014

@author: jvaccaro
"""

"Exercise 5-3"
"""
1. Write a function named
check_fermat
that takes four parameters—a, b, c and n
—and that checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
an +bn = cn
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for
a
,
b
,
c
and
n
, converts them to
integers, and uses
check_fermat
to check whether they violate Fermat’s theorem."""

def checkfermat(a, b, c, n):
    d = a**n + b**n
    if c**n == d:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
checkfermat(5, 6, 7, 3)

def promptlyfe(a, b, c, n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    checkfermat(a, b, c, n)
    
promptlyfe(3, 4, 5, 2)