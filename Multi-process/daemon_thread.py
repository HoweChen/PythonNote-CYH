import threading
import time

import threading
import time


def run(n):
    print("task", n)
    time.sleep(1)  # 此时子线程停1s
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')


for i in range(3):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.setDaemon(True)  # 把子进程设置为守护线程，必须在start()之前设置
    t.start()

time.sleep(0.5)  # 主线程停0.5秒
print(threading.active_count())  # 输出活跃的线程数
