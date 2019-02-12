from multiprocessing import Pool, Queue, Process

q = Queue()
show_q = Queue()


def producer():
    for i in range(100):
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
            show_q.put("None")
        else:
            # print(result)
            show_q.put(result)


p = Process(target=producer)
c = Process(target=consumer)

p.start()
c.start()

show_q_end = False
while True:
    if show_q.empty() is True and show_q_end is False:
        continue
    if show_q.empty() is True and show_q_end is True:
        break
    result = show_q.get()
    if result == "None":
        show_q_end = True
    else:
        print(result)

p.join()
c.join()
