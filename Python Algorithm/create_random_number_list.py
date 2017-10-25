import random as rd
import sys

max_int = sys.maxsize
random_List = []


def create_random_number_list(size):
    for i in range(int(size)):
        rd_number = rd.randint(0, max_int)
        if rd_number not in random_List:
            random_List.append(rd_number)

    return


def main():
    size = input("Please input the size of random number list\n")
    create_random_number_list(size)
    return random_List


if __name__ == '__main__':
    main()
