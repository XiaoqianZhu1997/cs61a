def improve(update, close, guess = 1):
	while close(guess):
		guess = update(guess)
	return guess


def approx_eq(a, b, tolerance = 1e-15):
	return abs(a-b) > tolerance

def average(x, y):
	return (x + y) / 2


def sqrt(a):
	return improve(lambda x: average(x, a/x),
				   lambda x: approx_eq(x * x, a))