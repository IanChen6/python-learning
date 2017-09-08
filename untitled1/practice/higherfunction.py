# def f(x):
#     return x**2+1
# l=[2,12,11,31,4,5,6]
# r=map(f,l)
# print(list(r))#map函数

# from functools import reduce
# l=[1,2,3,4,5]
# def f(x,y):
#     return x*10+y
# print(reduce(f,l))

def primeupper(str):
    str=str[0].upper()+str[1:].lower()
    return str
l=['sda','wDf','sdaERR']
l2=map(primeupper,l)
l3=list(l2)
print(l3)

