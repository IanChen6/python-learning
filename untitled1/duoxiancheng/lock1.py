#多线程共享变量，变量可以被任何线程修改
import threading
balance = 0
def change_balance(n):
    global balance
    balance = balance+n
    balance=balance-n
def run_thread(n):
    for i in range(10000000):#当循环过多时，结果就不一定为0
        #究其原因，是因为修改balance需要多条语句，
        # 而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了
        change_balance(n)
t1=threading.Thread(target=run_thread,name="myThread",args=(10,))
t2=threading.Thread(target=run_thread,name="myThread",args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#要确保balance计算正确，就要给change_it()上一把锁，
# 当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
