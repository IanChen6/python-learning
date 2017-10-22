# -*- coding:utf-8 -*-
__author__ = 'IanChen'

def normalize(name):
    return name.lower().capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
