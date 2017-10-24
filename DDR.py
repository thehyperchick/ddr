import pygame
from pygame.locals import *
import math
import random

# Initialize Pygame
pygame.init()
# Initiliace Mixer
pygame.mixer.init()
badguys=[[480,100]]
badtimer=100
badtimer1=0
fromleft=0
fromtop=1


#Set Width and Height of the Window in Pixels.
width, height = 480, 640

#Sets Screen and assigns it to a variable.
screen=pygame.display.set_mode((width, height))

#Initiliaze Images
grass = pygame.image.load("resources/images/grass.png")
badguyimg = pygame.image.load("resources/images/badguy.png")


pygame.mixer.music.load('resources/audio/moonlight.wav')

running = 1
while running:
    badtimer -= 1
    screen.fill(0)
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    if badtimer == 0:
        badguys.append([random.randint(50, 430), 0])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[fromtop] > 640:
            badguys.pop(index)
        badguy[fromtop] += 7

    for badguy in badguys:
        screen.blit(badguyimg, badguy)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key == K_SPACE:
                pygame.mixer.music.play(-1, 0.0)
                pygame.mixer.music.set_volume(0.25)




