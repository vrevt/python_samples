def spam(x):
    print(10 // x)

def sol(d):
    try:
        spam(0)
        print(d[1])
    except KeyError as error:
        print(type(error))
        print('No such index')
    except IndexError:
        print('wrong index')
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('else doesnt fullfilled')

    try:
        x = 1
    except:
        pass
    else:
        print('else turned')


    return True


if __name__ == '__main__':
    d = {}
    print(sol(d))
