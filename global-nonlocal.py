x = 50

def func():
    global x
    print('x =', x)
    x = 2
    print('changed x = ', x)

func()
print('last x = ', x)


def func_outer():
    x = 2
    print('x = ', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('changed x = ', x)


func_outer()
