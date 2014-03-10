# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 22:20:55 2014

@author: jvaccaro
"""

#practice again
#This one has growing boxes, but unrealistic perspective. Oh well.

import pygame
from pygame.locals import *
import random
import math
import time

class GrowModel:
    '''
        This class encodes the game state.
    '''
    def __init__(self, size):
        print "yoloswag"
        self.boxes = []
        (self.sx, self.sy) = size
        self.side = (self.sx-10)/10
        self.missed = 0
        self.lives = 20
        self.score = 0
        self.arrowlist = ['K_UP','K_DOWN','K_LEFT','K_RIGHT']
        self.speedFactor = 0
        for x in range((self.side/2+5), (self.sx-self.side/2-5), self.side):
            y = self.side/2
            box = Box((0,random.randint(50,255),random.randint(50,255)),self.sx/2,-y,self.side/4,-.001*x/self.sy,random.random()/4+.4, .001, self.arrowlist[random.randint(0,3)])
            self.boxes.append(box)
            
    def makeBox(self):
        color = (0, random.randint(0,255), random.randint(0,255))
        x = random.randint((self.side/2+5), (self.sx-self.side/2-5))
        speed = (random.random()/4+.4+self.speedFactor)
        box = Box(color, self.sx/2, -self.side, self.side/4, (-.001*(x-self.sx/2)/speed), speed, .001, self.arrowlist[random.randint(0,3)])
        self.boxes.append(box)
            
    def update(self):
        for box in self.boxes:
            box.centerx += box.vx
            box.centery += box.vy
            box.vx += box.ay
            box.vy += box.ay
            box.side += .2
            if box.centery > self.sy - 5*self.side/2:
                box.color = (255,0,0)
            if box.centery > self.sy - self.side/2:
                self.boxes.remove(box)
                self.missed += 1
                self.lives -= 1
        chance = random.randint(0,500)
        if chance < 3:
            self.speedFactor += .01
            self.makeBox()
        
class Box:
    '''This makes a box hooray!'''
    def __init__(self, color, centerx, centery, side, vx, vy, ay, arrow):
        self.color = color
        self.centerx = centerx #center x coordinate
        self.centery = centery #center y coordinate
        self.side = side #side length, assuming square
        self.vx = vx        
        self.vy = vy
        self.ay = ay
        self.arrow = arrow #like K_UP

class GrowViewPyGame:
    '''
        This class renders a display of the game in PyGame.
    '''
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        self.arrowImageDict = {'K_UP':'arrowU.png','K_DOWN':'arrowD.png','K_LEFT':'arrowL.png','K_RIGHT':'arrowR.png'}
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for b in self.model.boxes:
            cx = b.centerx - b.side/2
            cy = b.centery - b.side/2
            box_rect = pygame.Rect(cx, cy, b.side, b.side)
            pygame.draw.rect(self.screen,
                             pygame.Color(b.color[0], b.color[1], b.color[2]),
                             box_rect)
            arrowImage = pygame.image.load(self.arrowImageDict[b.arrow])
            pygame.transform.scale(arrowImage, (int(b.side),int(b.side)))
            #arrowrect = arrowImage.get_rect(center=(cx,cy))    
            self.screen.blit(arrowImage, box_rect)
        pygame.display.update()
    
    
class GrowKeyboardPyGame:
    '''
        This class allows for control of the PyGame rendering using a keyboard.
    '''
class GrowMousePyGame:
    '''
    '''
    def __init__(self, model):
        self.model = model
        
    def handle_mouse_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            (x, y) = event.pos
            for box in self.model.boxes:
                if x < box.centerx + box.side/2 and x > box.centerx - box.side/2:
                    if y <box.centery +box.side/2 and y>box.centery - box.side/2:
                        self.model.boxes.remove(box)
                        self.model.score +=1
                        print "Score: " + str(self.model.score) + "   Lives: " + str(self.model.lives)
            
#class GrowArrowPyGame:
#    '''
#    '''
 #   def __init__(self,model):
#        self.model = model
#        
#    def handle_arrow_event(self, event):
#        if event.type == :
    
if __name__ == '__main__':
    pygame.init()

    size = (800,800) #make sure sx-10 is multiple of 20
    screen = pygame.display.set_mode(size)
    
    model = GrowModel(size) 
    view = GrowViewPyGame(model, screen)
    controller = GrowMousePyGame(model)
    
    running = True

    while running:
        if model.lives == 0:
            running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)
        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()