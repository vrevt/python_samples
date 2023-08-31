class Bad(Exception):
    pass

def doomed():
    raise Bad()


if __name__ == '__main__':
    try:
        doomed()
    except Bad:
        print('got Bad')
