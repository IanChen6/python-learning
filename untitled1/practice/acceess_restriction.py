class Student(object):
    def __init__(self, name, score):#__name在属性名前加两个下划线将name设为private变量，只有内部可以访问
        self.__name = name
        self.__score = score
    def print__score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get__name(self):
        return self.__name
    def get__score(self):
        return self.__score
bart =Student('SDA',10)
# bart.__name#__name无法被外部访问，可增加get__name方法;注意以双下划线开头和双下划线结尾的变量是特殊变量，可直接访问
print(bart.get__name())