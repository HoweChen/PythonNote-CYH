from multiprocessing import Pool, Queue, Process
import time

q = Queue()
main_q = Queue()


def producer():
    for i in range(1000):
        q.put(i)
    q.put("None")


def consumer():
    meet_end = False
    while True:
        if q.empty() is True and meet_end is False:
            # which means still need to wait for the stuff produced
            continue
        if q.empty() is True and meet_end is True:
            break
        result = q.get()
        if result == "None":
            meet_end = True
            main_q.put("None")
        else:
            # print(result)
            main_q.put(result)


def show():
    main_q_end = False
    while True:
        if main_q.empty() is True and main_q_end is False:
            continue
        if main_q.empty() is True and main_q_end is True:
            break
        result = main_q.get()
        if result == "None":
            main_q_end = True
        else:
            print(result)


p = Process(target=producer)
c = Process(target=consumer)
start = time.time()
p.start()
c.start()

show()


p.join()
c.join()
end = time.time()
print(end - start)
