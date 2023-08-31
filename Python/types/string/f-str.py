len = -2


def f(len):
    return len**3


s = f'len {1 + 2 + 3 + abs(len)}, def = {f(len)}'
print(s)
