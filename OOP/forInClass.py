class base():
    def __getitem__(self, item):
        return self.v2[item]


x = base()
x.v1 = 'aba'
x.v2 = [1, 2, 3, 10, 1]

for i in x:
    print(i)
