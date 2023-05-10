file = open('1.txt', 'r',  encoding='utf-8')
print(file.read())
#print(file.read())
# return to start
file.seek(0)

print(file.readline())

for row in file:
    print(row)

file.seek(0)
s = file.readlines()
print(s)

# a+ for read and write
file = open('1.txt', 'a', encoding='utf-8')
file.write('hello\n')

# for avoid memory leak
file.close()




