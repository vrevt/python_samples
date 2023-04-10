a = (1, 2, 3)
b = (4, 5, 6)

print(f'{a} + {b} = {a + b}')

a += b
print('a += b:', a)
print('a x 2:', a * 2)

sorted_a = sorted(a, reverse=True)
print('sorted a:', sorted_a)

new_a = [i + 20 for i in sorted_a]
print('new_a =', new_a)

print('index 21:', new_a.index(21))
print('count 22:', (new_a*3).count(22))


list_a = (1, [2, 3], 4)
list_a[1][0] = 100
print('change list object in tuple:', list_a)
