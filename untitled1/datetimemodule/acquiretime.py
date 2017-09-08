# import time
# a=time.time()
# for i in range(10):
#     n=i+1
#     time.sleep(1)
# b=time.time()
# l=b-a
# print(l)
from datetime import datetime#导入datetime模块中的datetime类

now=datetime.now()
print(now)
print(type(now))
dt=datetime(2018,2,21,23,30,59)
print(dt)
t=dt.timestamp()
print(t)#timestap是一个浮点数，如果有小数位表示毫秒
t1=1231231.0
print(datetime.fromtimestamp(t1))#将datetime转换成timestamp
print(datetime.utcfromtimestamp(t1))#转成UTC标准时间