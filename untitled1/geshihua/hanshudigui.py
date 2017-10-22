# -*- coding:utf-8 -*-
__author__ = 'IanChen'

# def move(n,a,buffer,c):
#     if n==1:
#         print(a,"--",c)
#         return
#
#     move(n-1,a,c,buffer)
#
#
#     move(1,a,buffer,c)
#     move(n-1,buffer,a,c)
#
# move(5,"A","B","C")
# s=range(9)
# for i in s:
#     print(i)
#
# L = ['Hello', 'World', 18, 'Apple', None]
# L2=[str1.lower() for str1 in L if isinstance(str1,str)]
# print(L2)
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b#改成生成器
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(5)
#


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

n=0
for t in triangles():
    print(t)
    n+=1
    if n==10:
        break