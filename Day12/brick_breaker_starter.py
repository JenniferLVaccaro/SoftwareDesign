# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:34:24 2014

@author: pruvolo
"""

import pygame
from pygame.locals import *
import random
import math
import time

class BrickBreakerModel():
    '''
        This class encodes the game state. (What's going on in the game.)
    '''
    def __init__(self):
        print "Creating an object!"
        self.bricks = []
        for x in range(10, 530, 110):
            for y in range(10, 250, 60):
                brick = Brick((255,0,0), 20, 100, x, y)
                self.bricks.append(brick)
        for x in range(60, 470, 110):
            for y in range(40, 220, 60):
                brick = Brick((0,255,0), 20, 100, x, y)
                self.bricks.append(brick)

class Brick:
    '''
        Encodes the state of brick in the game.
    '''
    def __init__(self, color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        
class BBView():
    '''
        Renders the model into a viewable experience.
    '''
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, pygame.Color(brick.color), pygame.rect(brick.x,brick.y,brick.width,brick.height))
        pygame.display.update()
        
class BBController():
    '''
        Connects input from user to manipulate state of model.
    '''
            
if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)
    
    model = BrickBreakerModel()    
    view = BBView(model, screen)
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.001)

    pygame.quit()