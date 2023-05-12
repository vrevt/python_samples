if __name__ == '__main__':
    excs = [IndexError, TypeError]
    # raise excs[0]

    try:
        1/0
    except Exception as E:
        raise TypeError('Bad!') from E

