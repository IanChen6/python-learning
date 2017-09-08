from datetime import datetime
#将str转换成datetime
# s="2016-8-1 10:30:30"
# d=datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
# print(d)#转换后的没有时区信息
# print(type(d))

now=datetime.now()
print(now.strftime("%a,%b,%Y,%H:%M:%S"))
# print(now.strftime('%a, %b %d %H:%M'))