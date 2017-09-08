import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s=Student('mike',23,99)
#print(json.dumps(s))#无法把Student类实例序列化为JSON，
# 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

#可选参数default就是把任意一个对象变成一个可序列为JSON的对象
# 我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
    return {"name":std.name,"age":std.age,"score":std.score}
print(json.dumps(s,default=student2dict))
#不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
# 我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s,default=lambda obj:obj.__dict__))

#loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2Student(d):
    return Student(d['name'],d['age'],d['score'])
print(json.loads(json.dumps(s,default=student2dict),object_hook=dict2Student))