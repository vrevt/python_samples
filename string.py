s.find('xx') # => int
s = 'abacaba'
print(s.find('b'))
# 1


s.replace('ab', 'abc') # => str
print(s)
#'abcacabca'

s = 'hello, Ivan!'
print(s.split(',')) # => list
# ['hello', ' Ivan!']


s.isalpha() # => bool
s.isdigit()


a.rstrip # => delete space
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
print(a.lower()) 
# hello, world!


a = "Hello, World!"
print(a.upper())
# HELLO, WORLD!


print(a.replace("H", "J"))
# Jello, World!

# reverse S
S = 'hello'
S[::-1]
# 'olleh'

title = "Meaning " "of" " Life" # Неявная конкатенация
print(title)
# Meaning of Life

