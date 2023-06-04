class A():
    def __init__(self, a1 = None, a2 = None, a3 = None):
        self.name = a1
        self.age = a2
        self.level = a3
    def arg_out(self):
        print(self.name, self.age, self.level)

    def raiseAge(self, amount = 1):
        self.age += amount
