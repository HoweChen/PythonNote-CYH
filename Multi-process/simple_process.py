from multiprocessing import Process
import os
from multiprocessing.dummy import Pool

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())  # 获取父进程id
    print('process id:', os.getpid())  # 获取自己的进程id
    print("\n\n")


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()