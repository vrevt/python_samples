import time
from functools import wraps


def timeit(func):
    # @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def calculate_something(num, x):
    print(x)
    total = sum((x for x in range(0, num**2)))
    return total


if __name__ == '__main__':
    calculate_something(10, 1)
    calculate_something(100, 2)
    calculate_something(1000, 3)
    calculate_something(5000, 4)
    calculate_something(10000, 5)
