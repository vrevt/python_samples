import shelve

db = shelve.open('shelveDB.txt')

# интерпретатор автоматически импортирует класс А, так как сохранил его имя при записи в файл
print(db['Ivan'])
x = db['Ivan']
x.raiseAge(10)
db['Ivan'] = x
db.close()

db = shelve.open('shelveDB.txt')
print(db['Ivan'].age)
db.close()
