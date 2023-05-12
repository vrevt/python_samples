# base

class Descriptor:
	def __get__(self, obj, obj_type):
		print('get')

	def __set__(self, obj, value):
		print('set')

	def __delete__(self, obj):
		print('delete')


class Class:
	attr = Descriptor()


instance = Class()

instance.attr
instance.attr = 10 
del instance.attr


# sample 1

class ImportantValue:
	def __init__(self, amount):
		self.amount = amount

	def __get__(self, obj, obj_type):
		return self.amount

	def __set__(self, obj, value):
		with open('log.txt', 'w') as file:
			file.write(str(value))
		self.amount = value

class Account:
	amount = ImportantValue(100)


my_account = Account()
my_account.amount = 150


with open('log.txt', 'r') as file:
	print(file.read())

