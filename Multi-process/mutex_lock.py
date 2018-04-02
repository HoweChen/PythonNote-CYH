import threading
import time


def run(n):
    lock.acquire()  # 获取锁
    global num
    num += 1
    lock.release()  # 释放锁


lock = threading.Lock()  # 实例化一个锁对象

num = 0
t_obj = []

for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print("num:", num)
