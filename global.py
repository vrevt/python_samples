x = 50


def func():
    global x
    print('x =', x)
    x = 2
    print('changed x = ', x)


func()
print('last x = ', x)
