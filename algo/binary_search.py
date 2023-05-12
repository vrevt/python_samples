from random import randint

a = []
n = randint(1, 20)
for i in range(n):
	a.append(randint(1, 100))

a.sort()
print(a)

value = int(input())

l = 0
r = len(a) - 1

while l < r:
	print(l, ' ', r)
	m = (l + r) // 2
	if value > a[m]:
		l = m + 1
	else:
		r = m

if a[l] != value:
	print('no value')
else:
	print(l)
