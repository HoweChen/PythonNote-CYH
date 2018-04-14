"""
Use bit shifting operation to count how many ones for a num in binary form
The input is the integer number
"""


def main():
    num = int(input('Please input an integer: '))
    count = 0
    while (num != 0):
        count += 1
        num = (num - 1) & num
    print(count)


if __name__ == '__main__':
    main()
