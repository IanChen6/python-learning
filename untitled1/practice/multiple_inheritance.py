#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# class Mammal(object):
#     pass
# class RunnableMixIn(object):
#     pass
# class CarnivorousMixIn(object):
#     pass
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):#定义__str__()方法，返回实例的字符串说明
#         return 'Student object (name:%s)'%self.name
#
#     __repr__=__str__
# print(Student('Mike'))
# s=Student('Jack')#直接敲变量不用print，s实例返回的还是<__main__.Student object at 0x...>
#所以重写__repr__()方法

#__iter__()、__getitem__()
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1#菲波那切数列，初始化
    def __iter__(self):
        return self#iter方法返回一个迭代对象
    def __next__(self):#next方法拿到下一次循环的值
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration()
        return self.a
    # def __getitem__(self,n):#类实例虽让能作用于for循环，但是无法直接当成list使用，getitem方法能实现下标取元素
    #     a,b=1,1
    #     for x in range(n):
    #         a,b=b,a+b
    #     return a
    #增加片选
    def __getitem__(self,n):
        if isinstance(n,int):#n是索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):#n是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
    # __getattr__:只有当调用不存在的属性时，才会在刚方法中寻找
    def __getattr__(self,attr):
        if attr=="score":
            return lambda :25
# for n in Fib():
#     print(n)
f=Fib()
print(f[2])
print(f[1:9])
print(f.score())
print(f.aaa)#写了getattr方法后，调用任意属性，就会返回None；
#
