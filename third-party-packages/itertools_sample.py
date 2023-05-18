import itertools


def permutations():
    horses = [1, 2, 3, 4]
    races = itertools.permutations(horses)
    print(list(races))

def arithmetic_progression(start, step):
    sum = itertools.count(start, step)
    next(sum)
    next(sum)
    next(sum)
    print(sum)

def prefix_sums():
    arr = [1, 2, 3, 4, 5]
    arr_sums = itertools.accumulate(arr)
    print(list(arr_sums))

def n_combinations():
    arr = 'abcd'
    comb = itertools.combinations(arr, 3)
    print(list(comb))

if __name__ == '__main__':
    permutations()
    arithmetic_progression(start=1, step=12)
    prefix_sums()
    n_combinations()

    '''
    others:
    itertools.filterfalse(func, iterable) -> elements with false after func
    itertools.permutations(iterable, r=None) -> перестановки длиной r из iterable.
    '''