"""this algorithm returns the prime number list from 2-n
"""

import math


def main():
    n = int(input('Please input a number as n: '))
    original_list = list(range(2, n+1))

    for index in range(0, original_list.index(math.floor(math.sqrt(n)))+1):
        if original_list[index] != 0:
            p = original_list[index]
            j = p*p
            print(j)
            while(j <= n):
                try:
                    original_list[original_list.index(j)] = 0
                    j += original_list[index]
                except Exception as identifier:
                    j += original_list[index]
                    continue
    while True:
        try:
            original_list.remove(0)
        except Exception as identifier:
            break
    print(original_list)


if __name__ == '__main__':
    main()
