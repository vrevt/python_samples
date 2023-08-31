class classA():
    def __init__(self, arg):
        self.arg = arg

    def methodA(self):
        print(self.arg)


if __name__ == '__main__':
    a = classA(1)
    a.methodA()
    b = classA(2)
    b.methodA()
    c = classA(3)
    c.methodA()
