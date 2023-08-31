class Entity:
    '''Класс, описывающий объект на плоскости. "Вызываемый", чтобы обновить позицию объекта.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Изменить положение объекта.'''
        self.x, self.y = x, y


if __name__ == '__main__':
    x = Entity(4, 1, 2)
    x(5, 5)
    print(x.size, x.x, x.y)
