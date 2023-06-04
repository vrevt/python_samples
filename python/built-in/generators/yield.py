l = [1, 2, 3, 4, 5]

# if you don`t need save all list of elements
def gen(n):
    for i in range(n):
        yield i

generator = gen(5)
for i in generator:
    print(i)


i = iter(l)
print(next(i))
print(next(i))


# another way to create generator

x = (i * i for i in l) # lazy calculation
print(x)

for i in x:
    print(i)

