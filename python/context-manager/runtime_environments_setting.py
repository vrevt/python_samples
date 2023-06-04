import decimal

if __name__ == '__main__':
    with decimal.localcontext() as ctx:
        # настройка точности операции внутри этого контекста
        ctx.prec = 2
        print(13.21212 + 112.1212)


