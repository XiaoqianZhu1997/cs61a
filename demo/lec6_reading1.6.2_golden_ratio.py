def improve(update, close, guess = 1):
	while close(guess):
		guess = update(guess)
	return guess


def golden_update(guess):
	return 1/guess + 1

def square_close_to_successor(guess):
	return approx_eq(guess * guess, guess + 1)

def approx_eq(a, b, tolerance = 1e-15):
	return abs(a-b) > tolerance


"""进行检验"""
from math import sqrt
phi = 1/2 + sqrt(5)/2

def improve_test():
	approx_phi = improve(golden_update, square_close_to_successor)
	assert not approx_eq(phi, approx_phi)   #如果下一行要输出这个test函数的时候，返回值是none，那就说明检验通过