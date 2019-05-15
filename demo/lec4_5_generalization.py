from operator import mul

def make_adder(n):
	"""为了得到一个function使得这个function是与k有关，输出结果是k+n"""
	def adder(k):
		return mul(4, k) + n
	return adder


def denomin(k):
	return 8 / mul(make_adder(-1), make_adder(-3))

def summation(n, term):
	"""计算前n项的和"""
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total

def con_p(n):
	return summation(n, denomin)