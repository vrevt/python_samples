def check_elem(x):
    if x % 2 == 0:
        return True
    else:
        return False

li = [1,2,3,4,5,6,7,8]

print([i for i in filter(check_elem, li)])
#=> [2, 4, 6, 8]
