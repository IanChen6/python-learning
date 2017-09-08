#先创建SSL安全连接，再用SMTP发送邮件
import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()#创建SMTP对象后立即调用starttls方法，就创建了安全连接
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...