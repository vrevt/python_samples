from functools import reduce

def add_elem(x,y):
    return x + y

li = [1, 2, 3, 5]

reduce(add_elem, li)

#=> 11