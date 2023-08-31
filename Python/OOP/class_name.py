class ClassA:
    def __init__(self, *data):
        self.data = data

    def out(self):
        print(self.data)

    def returnClassName(self):
        return self.__name__


if __name__ == '__main__':
    a = ClassA
    print(a.__name__)
    print(a.returnClassName)
    print(a.__dict__)
