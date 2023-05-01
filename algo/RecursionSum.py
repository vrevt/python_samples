def sumtree(x):
    sum = 0
    for i in x:
        print(i, isinstance(i, int))
        if isinstance(i, int):
            sum += i
        else:
            sum += sumtree(i)
    return sum

a = [[1, 2], [[4, 5], 3]]
print(sumtree(a))
# print(sumtree.__code__.co_varnames)
