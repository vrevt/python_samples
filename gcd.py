def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a


if __name__ == '__main__':
    a = -36
    b = 48
    print(gcd(a, b))
