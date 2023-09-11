# a - simple generator ( expression)

a = (i for i in range(2, 8))
print(a)

for i in a:
	print(i)

# long entry with yield


def gen(start, finish):
	while (start < finish):
		yield start * 0.33
		start += 1


a = gen(1, 4)
print(a)
for i in a:
	print(i)


