from multiprocessing import Pool
import os,random,time

def long_time_task(name):
    print("Run task %s(%s)..."%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print("task %s runs %0.2f seconds... "%(name,(end-start)))

if __name__=="__main__":
    print("parent process %s"% os.getpid())
    p=Pool(4)#最多同时4个进程
    for i in range(6):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocess done...')
    p.close()#调用close()之后就不能继续添加新的Process了
    p.join()
    print('all subprocess done...')