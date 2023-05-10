a = [1, 2, 3, 4, 5]
b = ['a', 'aa', 'aaa', 'ccc']

zip_obj = zip(a, b)
print(list(zip_obj))

# после вывода объект zip_obj нужно пересоздать
for i in zip_obj:
    print(i)
