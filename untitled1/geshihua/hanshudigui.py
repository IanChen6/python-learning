# -*- coding:utf-8 -*-
__author__ = 'IanChen'

def move(n,a,buffer,c):
    if n==1:
        print(a,"--",c)
        return

    move(n-1,a,c,buffer)


    move(1,a,buffer,c)
    move(n-1,buffer,a,c)

move(5,"A","B","C")