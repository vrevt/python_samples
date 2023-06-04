import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
def form(func):
    call_amount = 0
    def output(*args, **kwargs):
        nonlocal call_amount
        call_amount += 1
        executed_func = func(*args, **kwargs)
        a, b = args
        print(f'step: {call_amount}')
        print(f'{a} + {b} = {executed_func}')
        return executed_func
    return output
@form
def solution(a, b):
    return a + b

if __name__ == '__main__':
    solution(3, 3)
    solution(3, 10)
    solution(4, 11)
