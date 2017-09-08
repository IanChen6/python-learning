import threading
#创建全局的ThreadLocal对象
local_school=threading.local()
def process_student():
    #获取当前线程关联的student
    std=local_school.student
    print("Hello %s (in %s)"%(std,threading.current_thread().name))
def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student=name#local_school是全局变量，但是local_school的属性时线程局部变量
    process_student()
t1=threading.Thread(target=process_thread,name="Thread A",args=("Julia",))
t2=threading.Thread(target=process_thread,name="Thread B",args=("Lilly",))
t2.start()
t1.start()
t1.join()
t2.join()
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

#IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。
#计算密集型人物，最好用C语言编写