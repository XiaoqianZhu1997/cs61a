"""连续加法"""

def con_sum(n):

	a, b = 0, 0
	k = 0
	while k < n:
		a = a + 1
		b = a + b
		k = k + 1
	return b

def sum_naturals(n):
	k, b = 1, 0
	while k <= n:
		b = b + k
		k = k + 1
	return b

"""连续平方和"""
from operator import mul
def con_squaresum(n):

	x, k = 0, 0
	while k < n:
		k = k + 1
		x = x + mul(k, k)
	return x


"""连续立方和"""

def con_cubicsum(z):
	i, j = 0, 0
	while i < z:
		i = i + 1
		j = j + mul(i, mul(i, i))
	return j

"""lec4 third function"""
from operator import truediv
def de_sum(n):
	y, k = 0, 0
	while k < n:
		k = k + 1
		y = y + truediv(truediv(8, 4 * k - 3), 4 * k - 1)
	return y