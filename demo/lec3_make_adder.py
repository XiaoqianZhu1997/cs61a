def make_adder(n):
	"""将这个函数的返回值定义成另一个函数"""
	def adder(k):
		"""上一个确定了n，这里仅仅与k有关"""
		return k + n
	return adder

	
def make_adder(n):
	return lambda k: k + n

