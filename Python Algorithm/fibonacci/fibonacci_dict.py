dict_cache = {0: 1, 1: 1}


def fibonacci_dict(n):
    if n not in dict_cache:
        dict_cache[n] = fibonacci_dict(n - 1) + fibonacci_dict(n - 2)
    return dict_cache[n]


if __name__ == '__main__':
    for i in range(1, 100):
        print(fibonacci_dict(i))
