import threading
balance = 0
def change_balance(n):
    global balance
    balance = balance+n
    balance=balance-n

lock = threading.Lock()

def run_thread(n):
    for i in range(10000000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_balance(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
t1=threading.Thread(target=run_thread,name="myThread",args=(10,))
t2=threading.Thread(target=run_thread,name="myThread",args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)