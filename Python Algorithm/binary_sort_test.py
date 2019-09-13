import sys
from random import shuffle, randrange
import bisect

if __name__ == '__main__':

    n, q = map(int, sys.stdin.readline().split(","))
    print(n, q)
    # n = int(n)
    numbers = [randrange(0, n) for i in range(n)]
    numbers = sorted(numbers)
    print(numbers)
    for i in range(q):
        target_num = int(sys.stdin.readline().strip())
        index = bisect.bisect(numbers, target_num) - 1
        # print(index)
        # print(n - index)
        count = 0
        for i in range(index, len(numbers)):
            numbers[i] -= 1
            count += 1
        print(count)
