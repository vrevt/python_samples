import pickle

data = {'foo': [1, 2, 3],
        'bar': ('Hello', 'world!'),
        'baz': True}
jar = open('data.pkl', 'wb')
pickle.dump(data, jar) # записать сериализованные данные в jar
jar.close()


pkl_file = open('data.pkl', 'rb') # открываем
data = pickle.load(pkl_file) # сохраняем в переменную
print(data)
pkl_file.close()
