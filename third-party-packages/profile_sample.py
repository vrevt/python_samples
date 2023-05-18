import profile

def calc():
    sum = 0
    for i in range(100000000):
        if i & 1 and i % 13 == 0:
            sum += i
    return sum

if __name__ == '__main__':
    profile.run('code')


# python3 -m profile profile_sample.py
