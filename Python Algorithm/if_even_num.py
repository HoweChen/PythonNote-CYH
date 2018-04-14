def main():
    num = int(input('Please input a number: '))
    num = (num - 1) & num
    if num != 0:
        print("Odd Number")
    else:
        print('Even Number')


if __name__ == '__main__':
    main()
