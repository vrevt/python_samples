s = 'lsdhfxxfeoeb'
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


# Неявная конкатенация
title = "Meaning " "of" " Life" 
print(title)
# Meaning of Life


# join method
x = ';'.join(['eggs', 'sausage', 'ham', 'toast'])
print(x)
# eggs;sausage;ham;toast


# formatting method
s = "That is %d %s bird!" % (1, 'appear')
print(s)
# That is 1 appear bird!


# formatting string using dict
s = "%(n)d %(x)s" % {"n":24, "x":"november"}
print(s)
# 24 november




