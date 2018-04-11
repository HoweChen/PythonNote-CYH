def Euclid_gcd(m, n):
    m = int(m)
    n = int(n)
    if n == 0:
        return m
    else:
        return Euclid_gcd(n, m % n)


if __name__ == '__main__':
    m = input('m: ')
    n = input('n: ')
    print(Euclid_gcd(m, n))