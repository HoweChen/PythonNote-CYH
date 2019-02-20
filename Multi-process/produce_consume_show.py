from multiprocessing import Pool, Queue, Process
import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        t_start = time.time()
        f(*args, **kwargs)
        t_end = time.time()
        print(
            f"func: {f.__name__}\nargs:[{args}, {kwargs}]\ntook: {t_end-t_start} sec")
    return wrap


class Main(object):
    def __init__(self, *args, **kwargs):
        self.q = Queue()
        self.main_q = Queue()

    @timing
    def start(self):
        p = Process(target=self.producer)
        c = Process(target=self.consumer)
        start = time.time()
        processes = [p, c]
        for process in processes:
            process.start()

        self.show()

        for process in processes:
            process.join()
        end = time.time()
        # print(end - start)

    def producer(self):
        for i in range(10000):
            self.q.put(i)
        self.q.put(None)

    def consumer(self):
        while True:
            if self.q.empty() is True:
                # which means still need to wait for the stuff produced
                continue
            else:
                result = self.q.get()

                if result is not None:
                    # print(result)
                    self.main_q.put(result)
                else:
                    self.main_q.put(None)
                    break

    def show(self):
        while True:
            if self.main_q.empty() is True:
                continue
            else:
                result = self.main_q.get()
                if result is not None:
                    print(result)
                else:
                    break


main = Main()
main.start()
