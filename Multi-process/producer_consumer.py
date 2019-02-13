from multiprocessing import Process, JoinableQueue, Queue, Pool
import time
import os
from random import random

tasks_queue = JoinableQueue()
results_queue = Queue()


def double(n):
    return n * 2


def producer(in_queue: JoinableQueue):
    while True:
        wt = random()
        time.sleep(wt)
        in_queue.put((double, wt))
        if wt > 0.9:
            in_queue.put(None)
            print("stop producer")
            break


def consumer(in_queue: JoinableQueue, out_queue: Queue):
    while True:
        task: set = in_queue.get()
        if task is None:
            break
        func, arg = task
        result = func(arg)
        in_queue.task_done()
        out_queue.put(result)


processes = []

# producer process
p = Process(target=producer, args=(tasks_queue,))
p.start()
processes.append(p)

# consumer process
p = Process(target=consumer, args=(tasks_queue, results_queue))
p.start()
processes.append(p)

# Block until all items in the queue have been gotten and processed.
tasks_queue.join()

# this step is to wait till both producer and consumer process finish their jobs
for p in processes:
    p.join()

while results_queue.empty() is not True:
    result = results_queue.get()
    print(f"Result: {result}")
