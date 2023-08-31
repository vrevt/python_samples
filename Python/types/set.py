x = set('abacabe')
y = set('bdxyz')

print(x)
# {'c', 'e', 'b', 'a'}
print(y)
# {'d', 'x', 'y', 'b', 'z'}


# Разность множеств
print(x - y)
# {'c', 'e', 'a'}


# Объединение множеств
print(x | y)
# {'c', 'd', 'x', 'y', 'b', 'a', 'e', 'z'}


 # Пересечение множеств
print(x & y)
# {'b'}


# Симметрическая разность (XOR)
print(x ^ y)
# {'c', 'd', 'e', 'x', 'y', 'a', 'z'}


#other:
z = set()

tmp = set('SPAM')
print(tmp)
z.add('S') # Добавит один элемент
z.update(tmp) # Объединение множеств
print(f'{z=}')
z.remove('S') # Удалит один элемент
print(f'{z=}')

 
gen = {x ** 2 for x in [1, 2, 3, 4]} # Генератор множеств в 3.0
print(gen)