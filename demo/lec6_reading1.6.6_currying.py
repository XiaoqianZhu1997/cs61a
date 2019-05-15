def make_adder(x):
	return lambda y: x + y
 
"""generalization"""
"""Return a curried version of the given two-argument function."""
def curry2(f):   #curry2(f)(x)(y)求值，等价于g(x)(y)，等价于f(x,y)
	def g(x):   #g(x)return到关于y的函数h，于是g(x)(y)等价于f(x, y)，这里相当于固定了x
		def h(y):
			return f(x, y)
		return h
	return g
"""或者使用lambda函数变更为"""
curry2 = lambda f: lambda x: lambda y: f(x, y)
"""lambda后面接的都是变量名"""


def curried_pow(x):
	def h(y):
		return pow(x, y)
	return h
"""或者写成higher-order function"""
curried_pow = lambda x: lambda y: f(x, y)



"""start和end相当于定义域的一个子集区间，这个函数是print出了这个区间内的所有函数值"""
def map_to_range(start, end, f):
	while start < end:
		print(f(start))
		start += 1



"""Return a two-argument version of the given curried function."""
def uncurry2(g):   #uncurry2(curry2(f))其实就等价于f
	"""因为uncurry2(g)最后的返回值是f(x, y)➡️g(x)(y),而当这个g现在是curry2(f)时候，curry2(f)(x)(y)就等价于f(x, y)"""
	def f(x, y):
		return g(x)(y)
	return f

pow_curried = curry2(pow)
"""那么curry2(pow)(2)(5) = pow(2, 5) = 32"""
uncurry2(pow_curried)(2, 5)
"""这里uncurry2(g)(x, y) = g(x)(y)，所以这个式子等于pow_curried(2)(5) = 32"""


from operator import add
m = curry2(add) #m现在表示一个函数，m(x)仍然是一个函数
add_three = m(3)  
add_three(2)

curry2 = lambda f : lambda x: lambda y: f(x, y)

def curried_pow(x):
	def h(y):
		return pow(x, y)
	return h



