#限制属性范围（检查参数）
# class Student(object):
#     def get__score(self):
#         return self.__score
#     def set__score(self,value):
#         if not isinstance(value,int):
#             raise ValueError("score must be an integer")
#         if value<0 or value>100:
#             raise ValueError("score must between 0~100")
#         self.__score=value
# s=Student()
# s.set__score(40)
# print(s.get__score())

#为了用类似属性的方式访问类的变量，引入装饰器@property，把方法变为属性调用；@attr.setter,负责把一个setter方法变为属性赋值
# class Student(object):
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError("score must be an integer")
#         if value<0 or value>100:
#             raise ValueError("score must between 0~100")
#         self.__score=value
# s=Student()
# s.score=40
# print(s.score)

class Student(object):
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer")
        if value>=2017 or value<1917:
            raise ValueError("score must between 1917~2017")
        self.__birth=value
    @property
    def age(self):
        return 2017-self.__birth
s=Student()
s.birth=1993
# s.age=21 age只定义了getter方法，没有定义setter方法，所以age是只读属性
print(s.age)
