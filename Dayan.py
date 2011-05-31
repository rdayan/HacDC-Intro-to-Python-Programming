#! /usr/bin/env python
import time
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("HacDC Intro to Python Programming Homework 1 by Russ Dayan")

#Clear screen.
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 800, 500))

# Define star location variables.
s1x = 0
s2y = 175
s3x = 800
b1y = 245
b2x = 0

# Draw animated stars using two triangles.
while (s1x<200):
    # Clear star location.
    pygame.draw.rect(screen, (255, 255, 255), (s1x-50, 25, 101, 101))
    pygame.draw.rect(screen, (255, 255, 255), (350, s2y-50, 101, 101))
    pygame.draw.rect(screen, (255, 255, 255), (s3x-50, 25, 101, 101))
    
    # Advance location variables.
    s1x += 10
    s2y -= 5
    s3x -= 10
    b1y -= 5
    b2x += 20
    
    # Redraw stars.
    pygame.draw.polygon(screen, (255, 0, 0), [(s1x, 25), (s1x+50, 100), (s1x-50, 100)])
    pygame.draw.polygon(screen, (255, 0, 0), [(s1x, 125), (s1x+50, 50), (s1x-50, 50)])
    pygame.draw.polygon(screen, (255, 0, 0), [(400, s2y-50), (450, s2y+25), (350, s2y+25)])
    pygame.draw.polygon(screen, (255, 0, 0), [(400, s2y+50), (450, s2y-25), (350, s2y-25)])
    pygame.draw.polygon(screen, (255, 0, 0), [(s3x, 25), (s3x+50, 100), (s3x-50, 100)])
    pygame.draw.polygon(screen, (255, 0, 0), [(s3x, 125), (s3x+50, 50), (s3x-50, 50)])

    pygame.draw.rect(screen, (255, 0, 0), (0, b1y, 800, 5))
    pygame.draw.rect(screen, (255, 0, 0), (400-b2x, 300, b2x*2, 100))
    
    # Redraw display and wait 100 ms.
    pygame.display.flip()
    time.sleep(0.1)    

# Draw flag lines.
#pygame.draw.rect(screen, (255, 0, 0), (0, 150, 800, 100))
#pygame.draw.rect(screen, (255, 0, 0), (0, 300, 800, 100))

# Redraw display.
pygame.display.flip()

# Sleep for 10 seconds and close application.
time.sleep(10)