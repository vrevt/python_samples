class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change..')
        self._name = value

    @name.deleter
    def name(self):
        print('remove..')
        del self._name


if __name__ == '__main__':
    bob = Person('Bob Smth')
    print(bob.name)

    bob.name = 'Bobby X'
    print(bob.name)

    # print(Person.name.__doc__)