# ToDo

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @ abstractmethod
    def action(self):
        pass

class Sub(Super):
    def action(self):
        print('spam')

if __name__ == '__main__':
    x = Sub() # raise TypeError before def action in class Sub
    x.delegate()
