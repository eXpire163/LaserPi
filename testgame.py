import pygame
from pygame.locals import *

pygame.init()

while(True):
   for event in pygame.event.get():
      if (event.type == KEYDOWN):
         print event
         print event.key
         if (event.key == K_KP0):
			print "numpad 0"
         if (event.key == K_KP1):
			print "numpad 1"