import urllib
from urllib import request
with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
    data=f.read(30)
    print(data.decode('utf8'))
    print("Status:",f.status,f.reason)#返回连接状态，失败原因
    for k,v in f.getheaders():
        print("%s:%s"%(k,v))
