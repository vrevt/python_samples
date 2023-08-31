class Catcher:
    def __getattr__(self, item):
        print('Get: ', item)
        return 'ne dam'

    def __setattr__(self, key, value):
        print('Set: ', key, value)


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value


if __name__ == '__main__':
    # Catcher test
    c = Catcher()
    c.a = 1
    print(c.a)

    # Powers test
    X = Powers(3, 4)
    print(X.square)
    print(X.cube)
    X.square = 5
    print(X.square)
