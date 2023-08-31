class Car:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def __changeCost(self, cost):
        self.cost = cost


if __name__ == '__main__':
    obj_Car = Car('bmw', 1000)
    obj_Car._Car__changeCost(100)
    print(obj_Car.getCost())
