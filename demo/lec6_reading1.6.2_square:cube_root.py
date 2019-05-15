"""计算平方根"""
def square_root(a):
	x = 1
	while x * x != a:
		print(x)
		x = square_root_update(x, a)
	return x 

def square_root_update(x, a):
	return (x + a/x) / 2

"""计算立方根"""
def cube_root(a):
	x = 1
	while x * x * x != a:
		print(x)
		x = cube_root_update(x, a)
	return x

def cube_root_update(x, a):
	return (2*x + a/(x*x)) / 3


"""generalization"""
def improve(update, close, guess = 1, max_update = 100):  #这里update和close都是关于guess的函数，并且限制最大的循环次数
	"""update是用来更新的函数，close是用来检验的函数，例如立方/平方"""
	k = 0
	while not close(guess) and k < max_update:   #当guess的值不够接近的时候进行循环
		k = k + 1
		guess = update(guess)  #对guess进行更新
	return guess
 
 
def approx_eq(x, y, tolerance=1e-14):  #1e-15表示10^(-15)，这样的写法代表tolerance是默认值，后面可以省略
	return abs(x-y) < tolerance   #返回到True/False



"""对求解平方根进行优化，可以直接把approx_eq放到close函数"""
def square_root(a):
	def update(x):
		return square_root_update(x, a)
	def close(x):
		return approx_eq(x*x, a)
	return improve(update, close)

"""优化立方根函数 """
def cube_root(a):   #使用lambda函数再一次精简，因为在上面定义的update和close函数都是简单函数，直接return了
	return improve(lambda x: cube_root_update(x, a),   
				   lambda x: approx_eq(x*x*x, a))