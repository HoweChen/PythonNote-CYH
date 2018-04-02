import threading
import time


def run(n):
    print("task", n, threading.current_thread())
    time.sleep(1)
    print('3s')
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')


thread_list = []

time_flag = time.time()
for i in range(3):
    t = threading.Thread(target=run, args=(str(i)))
    t.start()
    thread_list.append(t)

for each_t in thread_list:
    each_t.join()

print('Cost of creating threads: {0}'.format(time.time()-time_flag))
print(threading.current_thread())
