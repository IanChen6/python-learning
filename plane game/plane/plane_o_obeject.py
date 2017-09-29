# -*- coding:utf-8 -*-
__author__ = 'IanChen'

import pygame
from pygame.locals import *

class HeroPlane(object):
    def __init__(self, screen):
        self.x = 230
        self.y = 700

        self.screen = screen
    #
        self.imageName = "./feiji/hero1.png"
    #
        self.image = pygame.image.load(self.imageName)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

def key_control(heroPlane):
#
    for event in pygame.event.get():
# print(event.type)
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                heroPlane.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                heroPlane.moveRight()
            elif event.key == K_SPACE:
                print('space')

def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    heroPlane = HeroPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        heroPlane.display()
        key_control(heroPlane)
        pygame.display.update()
if __name__ == "__main__":
    main()
