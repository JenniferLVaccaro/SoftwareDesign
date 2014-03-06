# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 13:50:46 2014

@author: jvaccaro
"""
from Point1 import *

def distance_between_points(P1, P2):
    '''
        Write a function called distance_between_points that takes two 
        Points as arguments and returns the distance between them.
        Ins: [P1, P2]
        Outs: distance (type = float)
    '''
    dx = P1.x - P2.x
    dy = P1.y - P2.y
    return (dx**2 + dy**2)**.5

def move_rectangle(rect, dx, dy):
    '''
        Write a function named move_rectangle that takes a Rectangle and 
        two numbers named dx and dy. It should change the location of the 
        rectangle by adding dx to the x coordinate of corner and adding dy 
        to the y coordinate of corner.
    '''
    rect.corner[0] = rect.corner[0] + dx
    rect.corner[1] = rect.corner[1] + dy
    
def E3(rect, dx, dy):
    '''
        Write a version of move_rectangle that creates and returns a new 
        Rectangle instead of modifying the old one.
    '''
    new_rect = Rectangle()
    new_rect.width = rect.width
    new_rect.height = rect.height
    new_rect.corner = [rect.corner[0]+dx, rect.corner[1]+dy]
    return new_rect
    
def E4():
    '''
        
    '''
    
if __name__ == "__main__":
    A = Point()
    A.x = -50
    A.y = 50
    B = Point()
    B.x = 50
    B.y = -50    
    print distance_between_points(A, B)
    R = Rectangle()
    R.width = 50
    R.height = 100
    R.corner = [20, 10]
    move_rectangle(R, 5, 10)
    print R.corner
    R2 = E3(R, 5, 10)
    print R2.corner