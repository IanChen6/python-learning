# -*- coding:utf-8 -*-
__author__ = 'IanChen'
import pygame
from pygame.locals import *

class HeroPlane(object):
    def __init__(self, screen):

    # 􁦡􁗝􁷢􀹢􁼕􁦊􁌱􀖖􁗝
        self.x = 230
        self.y = 700
    # 􁦡
        self.screen = screen
        self.imageName = "./feiji/hero1.png"
        self.image = pygame.image.load(self.imageName)
    # 􁊠􀹶􀨂􀘙􁝕􁵜􁷢􀹢􀝎􀩘􁌱􀲅􀹍􀧼􀭨
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bulletList:
            bullet.display()  # 􀸔􁐏􀓞􀓻􀧼􀭨􁌱􀖖􁗝
            bullet.move()

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)

        self.bulletList.append(newBullet)
class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet.png")

    def move(self):
        self.y -= 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
class EnemyPlane(object):
    def __init__(self,screen):
#􁦡􁗝􁷢􀹢􁼕􁦊􁌱􀖖􁗝
        self.x = 0
        self.y = 0
#􁦡􁗝􁥝􀸔􁐏􀙖􀨻􁌱􁑻􀝗
        self.screen = screen
        self.imageName = "./feiji/enemy0.png"
        self.image = pygame.image.load(self.imageName)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
def key_control(heroPlane):
#􀚣􀷙􀸎􀞈􀸎􁅩􀚋􀔧􁭅􀚊􀳲􁰵
    for event in pygame.event.get():
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
                heroPlane.sheBullet()
def main():
#1. 􀚠􀭌􀓞􀓻􁑻􀝗􀒅􁊠􀹶􀸔􁐏􀙖􀨻
    screen = pygame.display.set_mode((480,852),0,32)
#2. 􀚠􀭌􀓞􀓻􀞾􁑻􀝗􀥟􀩜􁌱􀢶􁇆􀒅􁊠􀹶􊧌􀭮􁙧􀸧
    background = pygame.image.load("./feiji/background.png")
#3.1 􀚠􀭌􀓞􀓻􁷢􀹢􀩒􁨝
    heroPlane = HeroPlane(screen)
#3.2 􀚠􀭌􀓞􀓻􀶶􀕈􁷢􀹢
    enemyPlane = EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        heroPlane.display()
        enemyPlane.display()
        key_control(heroPlane)
        pygame.display.update()
if __name__ == "__main__":
    main()