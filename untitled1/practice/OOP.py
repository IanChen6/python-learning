class Student(object):#括号内的object表示Student类从Object类中继承（object类是超类）
    def __init__(self,name,score):#_init_函数用于初始化对象的属性
        self.name = name#self为对象自身的引用，给对象增加name和score属性
        self.score = score
    def print_score(self):#和普通的函数不同，在类中定义的函数的第一个参数一定是实例对象self本身
        print('%s: %s'%(self.name,self.score))
# bart=Student
# bart.score=59
# bart.name='Bart'
# bart.print_score(bart)
bart=Student('Bart',59)
bart.print_score()
bart.age=23#能给实例对象增加属性
print(bart.age)
