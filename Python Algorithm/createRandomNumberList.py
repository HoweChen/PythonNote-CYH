import random as rd
import sys

maxInt = sys.maxsize
randomList = []


def createRandomNumberList(size):
    for i in range(int(size)):
        rdNumber = rd.randint(0, maxInt)
        if rdNumber not in randomList:
            randomList.append(rdNumber)

    return


def main():
    size = input("Please input the size of random number list\n")
    createRandomNumberList(size)
    return randomList


if __name__ == '__main__':
    main()
