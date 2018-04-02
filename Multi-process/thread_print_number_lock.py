import threading
import time
import string

a2z_list = list(string.ascii_lowercase)


def print_char(lock, char):
    lock.acquire()
    print(char)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    for char in a2z_list:
        p = threading.Thread(target=print_char, args=(lock, char))
        p.start()
        p.join()
