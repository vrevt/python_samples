import itertools


def permutations():
    horses = [1, 2, 3, 4]
    races = itertools.permutations(horses)
    print(list(races))


if __name__ == '__main__':
    permutations()