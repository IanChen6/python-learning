import time,threading

#新线程执行的代码
def loop():
    print('thread %s is running...'%threading.current_thread().name)
    n=0
    while n<5:
        n += 1
        print('thread %s ---%s'%(threading.current_thread().name,n))
        time.sleep(5)
    print("thread %s end..."%threading.current_thread().name)

#主程序
print('thread %s is running...'%threading.current_thread().name)
th=threading.Thread(target=loop,name="newthread")#启动新线程，target传入目标方法，name为新线程名字，为命名则默认thread1、thread2...
th.start()
th.join()
print('thread %s end...'%threading.current_thread().name)