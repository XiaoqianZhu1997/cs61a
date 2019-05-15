def f(x):
	print(x)
	return f   #返回到自己这个函数上
f(1)(2)(3)  #这样仍然得到的是一个函数，但是会把1，2，3都print出来


def print_all(x):
	print(x)
	return print_all
	

def print_sums(x):
	print(x)
	def next_sum(y):
		return print_sums(x + y)	
	return next_sum

