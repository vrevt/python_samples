# sample 1
def deco(func):
	def decorator():
		print('1')
		func()
		print('2')
	return decorator


@deco
def hello():
	print('hello')


hello()


# sample 2

def benchmark(func):
	import time

	def wrapper(*args, **kwargs):
		start = time.time()
		return_value = func(*args, **kwargs)
		end = time.time()
		print(f'start - {start}, end - {end}')
		return return_value
	return wrapper

@benchmark
def check_time(url):
	import requests
	page = requests.get(url)
	return page.text

check_time('https://google.com')


# sample 3

def benchmark(iters):
	def decorator(func):
		import time

		def wrapper(*args, **kwargs):
			total = 0
			for i in range(iters):
				start = time.time()
				return_value = func(*args, **kwargs)
				end = time.time()
				total = total + (end - start)
			print(f'everage time compleciti {total/iters}')
			return return_value
		return wrapper
	return decorator

# not decorator - argument not a function
@benchmark(iters=10)
def fetch_page(url):
	import requests
	page = requests.get(url)
	return page.text

print(fetch_page('https://google.com'))

