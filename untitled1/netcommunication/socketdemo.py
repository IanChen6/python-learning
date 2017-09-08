import socket
# socket.socket(family="AF_UNIX",type="SOCK_STREAM")
# AF_UNIX用于同一台机器的进程间访问（UNIX）
#AF_INET对于IPV4的TCP和UDP
# type参数SOCK_STREAM（流套接字），SOCK_DGRAM（数据报文套接字），SOCK_RAW(RAW套接字)
s=socket.socket()
#发起连接
s.connect(("www.sina.com.cn",80))#80端口是 Web服务的标准端口，SMTP（邮件服务）25，FTP （文件传输）21
#端口大于1024的可以任意使用，

#TCP连接后，向服务器发送请求，要求发回首页内容：
#发送数据：
s.send()