# 利用Event类模拟红绿灯
import threading
import time

event = threading.Event()


def lighter():
    count = 30
    event.set()  # 初始值为绿灯
    while True:
        for i in range(10):
            print('You can drive for {0} seconds.'.format(i))
            time.sleep(1)

        event.clear()  # 红灯，清除标志位
        time.sleep(1) 
        for count_down in range(count, -1, -1):
            print("Red light is on... wait for {0} seconds".format(count_down))
            time.sleep(1)
        event.set()
        print("Green light is on...")


def car(name):
    while True:
        if event.is_set():  # 判断是否设置了标志位
            print("[%s] running..." % name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..." % name)
            event.wait()
            print("[%s] green light is on,start going..." % name)


light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car, args=("MINI",))
car.start()
