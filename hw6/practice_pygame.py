# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:26:35 2014

@author: jvaccaro
"""

#pygame practice

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfObj = pygame.display.set_mode(640,480)
pygame.display.set_caption('Pygame Cheat Sheet')

jennySurfObj = pygame.image.load('jenny.png')
red = pygame.Color(255, 0, 0)
blu = pygame.Color(0, 255, 0)
grn = pygame.Color(0, 0, 255)
wht = pygame.Color(255, 255, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)

#win_music = pygame.
#lose_music = 

win_msg = ('Yay you win!')
lose_msg = ('Aww you lose =(')

while True:
    windowSurfObj.fill(blu)
    
    
    pygame.blit()
    
    for event in pygame.event.get():
        if event.type == LOSE:
            
            pygame.quit()
            sys.exit()
        if event.type == WIN:
            