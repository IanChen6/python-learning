# L=[['APPLE','GOOGLE','MICROSOFT'],['JAVA','PYTHON','RUBY']]
# print(L[1][1])
# a=input("你的年龄：")
# age=int(a)
# if age>6 and age<18:
#     print("teenager")
# elif age>=18:
#     print("adult")
# a=242
# print(hex(a))
def move(n,a,b,c):
    if n==1:
        print('move'+a+'->'+c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(10,"A","B","C")
