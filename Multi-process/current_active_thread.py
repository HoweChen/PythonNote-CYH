import threading
import time


def run(n):
    print('task {0}'.format(n))
    time.sleep(1)


for i in range(3):
    t = threading.Thread(target=run, args=(str(i)))
    t.start()

time.sleep(0.5)
print(threading.active_count())
