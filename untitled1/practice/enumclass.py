from enum import Enum, unique

Month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#获得Month类型的枚举类，可直接使用Month.Jan来引用一个常量
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)#value是自动赋给成员的常量，默认从1开始
#Month.Jan=121 #这里会报错，因为已经将成员属性设为常量
@unique#unique装饰器用来检查保证没有重复值
class Weekday(Enum):
    Sun=1#也可以自己赋值
    Mon=2
    Tue=3
    Wed = 4
    Thu = 5
    Fri = 6
    Sat =7
print(Weekday.Sat)
print(Weekday.Sat.value)
print(Weekday["Sat"])
print(Weekday(1))
