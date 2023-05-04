from classA import A
import shelve

bob = A('Ivan', 22, 'D6')

db = shelve.open('shelveDB.txt')
db[bob.name] = bob
db.close()
