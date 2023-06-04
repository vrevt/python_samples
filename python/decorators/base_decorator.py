def wrap(func):
    calculated = [i*i for i in range(100)]
    def make(*args, **kwargs):
        nonlocal calculated
        p = args[0]
        return calculated[p]
    return make

@wrap
def foo(x):
    res = x * x
    print(res, '!')
    return res

if __name__ == '__main__':
    print(foo(11))