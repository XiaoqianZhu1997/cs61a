    def trace1(fn):
	def traced(x):
		print('Calling', fn, 'on argument', x)
		return fn(x)
	return traced


def trace(fn):
	def wrapped(x):
		print('->', fn, '(', x, ')')
		return fn(x)
	return wrapped

@trace
@trace1  #写了这个在这里以后就是执行trace1(square)，这个又称为function decorator
def square(x):
	return x * x

@trace1
def sum_squares_up_to(n):
	k = 1
	total = 0
	while k <= n: 
		total = total + square(k)
		k = k + 1
	return total