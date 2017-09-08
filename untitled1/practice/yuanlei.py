# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
# h=Hello()
# print(type(Hello))
# print(type(h))

#type()函数既可以返回一个对象的类型，
# 又可以创建出新的类型，比如，
# 我们可以通过type()函数创建出Hello类，
# 而无需通过class Hello(object)...的定义：
def fn(self,name='world'):
    print('Hello,%s'%name)
Hello=type("Hello",(object,),dict(hello=fn))#创建Hello class,第二个参数必须是tuple
#通过type()函数创建类，依次传入3个参数
#1.class的名称
# 2.继承的父类集合（tuple）
# 3.class的方法名称与函数绑定
h=Hello()
h.hello()