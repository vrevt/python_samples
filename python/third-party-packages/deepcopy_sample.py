import copy

x = [1, [2], 3]

y = copy.copy(x)
z = copy.deepcopy(x)

x[1][0] = 10
print(y)
print(z)
