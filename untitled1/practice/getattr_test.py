# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#     def __str__(self):
#         return self._path
#     __repr__ = __str__
# a=Chain().status.user.timeline.list
# print(a)

#__call__
class Student(object):#调用实例本身
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s()
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(Student("mike")))