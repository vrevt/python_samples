from cmath import sqrt

map_obj = map(lambda x: sqrt(x).real, [4, 16, 20, 5])

print(list(map_obj))

# после вывода объект map_obj нужно пересоздать
for i in map_obj:
    print(i.real)

print(list(map_obj))