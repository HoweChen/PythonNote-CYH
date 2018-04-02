def fibonacci_classic(n):
    if n < 2:
        return 1
    else:
        return fibonacci_classic(n - 1) + fibonacci_classic(n - 2)


if __name__ == '__main__':
    for i in range(1, 10):
        print(fibonacci_classic(i))
