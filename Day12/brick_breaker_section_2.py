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

class BrickBreakerModel:
    """ Encodes the game state """
    def __init__(self):
        self.bricks = []
#        for x in range(10,530,110):
#            for y in range(10,240,30):
#                brick = Brick((255,0,0),20,100,x,y)
#                self.bricks.append(brick)
        for x in range(10, 530, 110):
            for y in range(10, 250, 60):
                brick = Brick((0,random.randint(0,256),random.randint(0,50)), 20, 100, x, y)
                self.bricks.append(brick)
        for x in range(60, 470, 110):
            for y in range(40, 220, 60):
                brick = Brick((random.randint(0,50),0,random.randint(0,256)), 20, 100, x, y)
                self.bricks.append(brick)
        self.Paddle = Paddle((255,255,255),20,100,200,450,0)
        
    def update(self):
        self.Paddle.update()

class Brick:
    """ Encodes the state of a brick in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Paddle:
    '''
        Encodes the state of the paddle.
    '''
    def __init__(self, color, height,width,x,y,vx):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.vx = vx
    
class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, pygame.Color(brick.color[0],brick.color[1],brick.color[2]),pygame.Rect(brick.x,brick.y,brick.width,brick.height))
        P = self.model.Paddle
        pygame.draw.rect(self.screen, pygame.Color(P.color),pygame.Rect(P.x,P.y,P.width,P.height))
        pygame.display.update()
        
class PyGameKeyboardController:
    
    def __init__(self,model):
        self.model = model
        
    def handle_keyboard_event(self,event):
        if event.type !=KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.paddle.vx +=-1.0
        if event.key = pygame.K_RIGHT:
            self.model.paddle.vx
        
class PyGameMouseController:
    
    def __init__(self, model):
        self.model = model
        
    def handle_mouse_event(self,event):
        if
if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = BrickBreakerModel()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_keyboard_event(event)
        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()