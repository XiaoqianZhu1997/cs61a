"""fib"""
def fib(n):

	pred, curr = 1, 0
	k = 0
	print(curr)
	while k < n:
		pred, curr = curr, curr + pred
		k = k + 1
		print(curr)
	return curr
	print(curr)


def fib(n):
	k, a, b, c = 0, 1, 0, 1
	while k < n:
		c = a
		a = b
		b = b + c
		k = k + 1
	return b