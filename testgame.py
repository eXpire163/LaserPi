import pygame
from pygame.locals import *

pygame.init()

while(True):
    for event in pygame.event.get():
        print event.type
        if (event.type == KEYDOWN):
            print event
            print event.key
