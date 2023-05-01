some_list = [1, 10, 3, 4, 8, 6]

f = lambda x: x * x
print(f(5))

x = list(map(lambda i: i ** 2, some_list))
print(x)

x = list(filter(lambda i: i % 2 == 0, some_list))
print(x)

some_list.sort(key=lambda x: bin(x).count('1'))
print(some_list)

# with string in file
print(list(map(lambda x: (x.upper()).strip(), open('1.txt'))))


# with dict items
d = {'a': 1, 'b': -1}

x = list(d.items())
x.sort(key=lambda i: i[1])

for i in x: print(i)
