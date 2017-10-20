# -*- coding:utf-8 -*-
__author__ = 'IanChen'

# a=input("score 1:")
# b=input("score 2:")
# a=int(a)
# b=int(b)
# if b>a:
#     percentage= ((b-a)/a)*100
#     percentage = "%.2f %%"%(percentage)
#     print("成绩上升"+percentage)
# else:
#     percentage = ((a - b) / a) * 100
#     percentage = "%.2f %%" % (percentage)
#     print("成绩下降"+percentage)
print(hex(100))

import math
def quadratic(a,b,c):
    gen =math.sqrt((b**2-4*a*c))
    a1=(-b+gen)/2
    a2=(-b - gen)/2
    print("该一元二次方程的两个解分别为：%.0f,%.1f"%(a1,a2))
quadratic(1,-2,-3)
