d = {'a': 1, 'b': 3, 'c': 2}
for key in d:
  print(key, d[key])

for (key, value) in d.items():
  print(key, value)
  
new_way = dict(a=5, b=6)
print(f'new way: {new_way}')

keys = ['foo', 'bar', 'baz']
values = [1, 2, 3]
x = dict(zip(keys, values))
print(f'zip(keys, values) = {x}')

d = {x: x ** 2 for x in [1, 2, 3, 5, 7]}
print(f'for x**2: {d}')

d = {c: c*4 for c in 'ABCD'}
print(f'ABCD: {d}')

d = dict.fromkeys(range(0, 10), 0)
print(f'fromkeys iterable range(): {d}')

d = dict.fromkeys([1,2,3,4], 100)
print(f'fromkeys iterable list: {d}')

d = {'a': 1}
c = {'c': 2}
print(f'{d} | {c} = {d | c}')

d |= c
print(f'd.items(): {list(d.items())}')
print(f'd.keys(): {list(d.keys())}')
print(f'd.values(): {list(d.values())}')

d |= {'a': 15, 'e': 8, 'z': 5}
x = sorted(d, reverse=True)
print(f'sorted(d): {x}')

new_d = {'a': 1, 'b': 2}
print(d == new_d) # but > < no longer works
