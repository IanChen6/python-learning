#在不同的编程语言之间传递对象
#就必须把对象序列化为标准格式，比如XML，
# 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输
# JSON不仅是标准格式，并且比XML更快
# 而且可以直接在Web页面中读取，非常方便

#如何把Python对象变成一个JSON
import json
d=dict(name='Bob', age=20, score=88)
json.dumps(d)
#dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object
f=open("D:\pydemo\json.txt",'w')#用w读写，因为json返回为字符串
json.dump(d,f)
f.close()
#load()和loads()
f2=open("D:\pydemo\json.txt",'r')
d2=json.load(f2)
f.close()
print(d2)