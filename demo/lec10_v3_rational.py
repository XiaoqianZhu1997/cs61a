def mul_rational(x, y):   # retional(n, d)表示的是一个有理数的分子n和分母d
	return rational(numer(x) * numer(y),   # numer表示一个有理数的分子
					denom(x) * denom(y))   # demon表示一个有理数的分母

def add_rational(x, y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx * dy + ny * dx, dx * dy)

def div_retional(x, y):
	return retional(numer(x) * denom(y),
					denom(x) * numer(y))

def equal_rational(x, y):
	return numer(x) * denom(y) == numer(y) * denom(x)
	# 或者return div_retional(x, y) == 1

def print_rational(x):
	print(numer(x), '/', denom(x))


# constructor and selectors
# 这里其实不需要知道具体的数值/有理数是怎样变到rational(n, d)的，但是要用这个rationla函数进行运算
def rational(n, d):   # ⚠️constructor
	# construct a rational number that represents N/D
	# return [n, d]
	def select(name):
		if name == 'n':   # 因为要求输入的是一个string
			return n
		elif name == 'd':
			return d
	return select

# ❕selector
def numer(x):   # ⚠️selector
	# return the numerator of rational x
	# return x[0]
	return x('n')

def denom(x):
	# return x[1]
	return x('d')

# 之前的对rational 的定义并没有到通分最简形式
from fractions import gcd
def rational1(n, d):
	g = gcd(n, d)
	return [n//g, d//g]