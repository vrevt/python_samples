import pickle

class someClass():
    attr = 1
    def counter(self):
        self.attr += 1


filename = 'tmp.txt'

object = someClass()
file = open(filename, 'wb') # Создать внешний файл
pickle.dump(object, file) # Сохранить объект в файле

file = open(filename, 'rb')
object = pickle.load(file) # Позднее извлечь обратно

print(type(object))
object.counter()
print(object.attr)
