# -*- coding:utf-8 -*-
__author__ = 'IanChen'

import pygame
from pygame.locals import *

def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    hero = pygame.image.load("./feiji/hero1.png")

    x = 0
    y = 0
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x-=5
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x+=5
                elif event.key == K_SPACE:
                    print('space')

        pygame.display.update()

if __name__ == "__main__":
    main()