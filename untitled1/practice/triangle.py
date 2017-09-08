# def triangles(n):
#     L=[1]
#     while True:
#         yield L
#         L=[L[X]+L[X+1] for X in range(len(L)-1)]
#         L.insert(0,1)
#         L.append(1)
#         if len(L)>10:
#             break
# a=triangles(15)
# for i in a:
#     print(i)
# from collections import Iterator
# print(isinstance(iter([]),Iterator))
#杨氏三角形