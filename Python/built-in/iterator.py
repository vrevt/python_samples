class Iterator:
	# for work in for 
	def __iter__(self):
		return self
	def __init__(self, limit):
		self.limit = limit
		self.counter = 0

	def __next__(self):
		if self.counter < self.limit:
			self.counter += 1
			return 1
		else:
			raise StopIteration


iter = Iterator(3)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
