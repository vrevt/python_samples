def sol(d):
    try:
        print(d[1])
    except KeyError:
        print('No such index')
    finally:
        print('finally')

    print(d.get(2, -1))
    return True


if __name__ == '__main__':
    d = {}
    print(sol(d))
