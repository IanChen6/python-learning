# -*- coding:utf-8 -*-
__author__ = 'IanChen'

import pygame

def main():
#创建一个窗口来显示内容
    screen = pygame.display.set_mode((480,852),0,32)
    #2.创建一个和窗口大小相同的图片填充背景
    background = pygame.image.load("./feiji/background.png")
    #3. 把背景图片放到窗口上显示
    while True:
    #设定需要显示的背景图
        screen.blit(background,(0,0))
    #更新需要显示的内容
        pygame.display.update()

if __name__ == "__main__":
    main()