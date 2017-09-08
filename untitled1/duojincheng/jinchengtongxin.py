#以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Process, Queue
import os, time, random
#写数据进程执行的代码
def write(q):
    print('process to write:%s'% os.getpid())
    for a in ['A','B','C']:
        print('put %s to que...'%a)
        q.put(a)
        time.sleep(random.random())
#读数据进程执行的代码:
def read(q):
    print('process to read:%s'% os.getpid())
    while True:
        v=q.get(True)
        print('get %s from queue'%v)
if __name__=="__main__":
    # 父进程创建queue，并传给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动子进程pw,写入：
    pw.start()
    #启动子进程pr,读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr是死循环，无法等待结束，智能强行终止
    pr.terminate()