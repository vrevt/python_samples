from collections import namedtuple

Car = namedtuple('Car', 'name color mileage price')

myCar = Car('chevy', 'black', 15, 1000)
print(myCar.name)
print(myCar[3])
a = myCar
print(tuple(a))


class MyCarWithMethods(Car):
    def print_color(self):
        print(self.color)


c = MyCarWithMethods('oka', 'white', 1, 200)
print(c.price)


ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
x = ElectricCar('zil', 'red', 1234, 1000, 45.0)
print(x)
