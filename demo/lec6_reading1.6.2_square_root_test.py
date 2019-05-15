def improve(update, close, guess = 1, max_update = 100):  #这里update和close都是关于guess的函数，并且限制最大的循环次数
	"""update是用来更新的函数，close是用来检验的函数，例如立方/平方"""
	while close(guess):  #当guess的值不够接近的时候进行循环
		guess = update(guess)  #对guess进行更新
	return guess
 
def approx_eq(x, y, tolerance=1e-14):  #1e-15表示10^(-15)，这样的写法代表tolerance是默认值，后面可以省略
	return abs(x-y) > tolerance   #返回到True/False


def square_root_update(x, a):
	return (x + a/x) / 2

def square_root(a):
	def update(x):
		return square_root_update(x, a)
	def close(x):
		return approx_eq(x*x, a)
	return improve(update, close)

