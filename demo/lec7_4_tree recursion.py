from ucb import trace

@trace
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

"""这样的递归设涉及到了重复计算，计算效率很低，在接下来的学习会介绍改进的方法"""