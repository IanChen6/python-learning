#sorted函数接收一个key函数来实现自定义排序(并不会改变原序列的值)
# l=sorted([212,-24214124,32,-4,1,-32],key=abs)
# print(l)
#案例，按绝对值大小排序

# l=sorted([212,-24214124,32,-4,1,-32],key=abs,reverse=True)
# print(l)
# #反向排序，传入第三个参数

#案例三，对含tuple的列表按名字排序
def by_name(t):
    return t[0]
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)],key=by_name))
