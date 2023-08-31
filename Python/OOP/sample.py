class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def repr(self):
        print(f'{self.name=}')
        print(f'{self.age=}')

class Manager(Person):
    def __init__(self, name, age, rank, skill):
        super().__init__(name, age)
        self.rank = rank
        self.skill = skill

    def return_rank(self):
        return self.rank


if __name__ == '__main__':
    p = Person('Ivan', 22)
    m = Manager('Petr', 35, 'D5', 'English C2')

    print(m.__dict__.keys())
    print(getattr(m, 'name'))