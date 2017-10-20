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


def triangel(n):
    L=[1]                                                                 #定义一个list[1]
    while True:
        yield L                                                           #打印出该list
        L=[L[x]+L[x+1] for x in range(len(L)-1)]        #计算下一行中间的值（除去两边的1）
        L.insert(0,1)                                                 #在开头插入1
        L.append(1)                                                 #在结尾添加1
        if len(L)>10:                                                 #仅输出10行
            break

triangel(10)