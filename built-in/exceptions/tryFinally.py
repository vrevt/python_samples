if __name__ == '__main__':
    d = {}
    try:
        print(d[2])
    finally:
        print('module finished')

    print('after try') # не выполнится, так как сработало исключение
