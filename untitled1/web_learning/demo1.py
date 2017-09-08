# import socket
# import urllib.parse
# import urllib.request
# import urllib.error
import socket
import urllib.request
import urllib.error

#添加data参数的时候就是以post请求方式请求，如果没有data参数就是get请求方式
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# print(data)
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
#
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())


try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')