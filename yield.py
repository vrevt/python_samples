# if you don`t need save all list of elements

def gen(n):
    for i in range(n):
        yield i


a = gen(5)
print(a)
print(next(a))
print(next(a))
