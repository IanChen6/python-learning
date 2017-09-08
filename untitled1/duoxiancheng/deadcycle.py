import threading, multiprocessing

def loop():#死循环
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):#启动与CPU核数一致的线程
    t = threading.Thread(target=loop)
    t.start()
#通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器