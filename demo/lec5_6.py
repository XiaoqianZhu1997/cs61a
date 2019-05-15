def f(x, y):
	return 	g(x)

def g(a):
	return a + y   #z这样书写会报错，因为没有对y进行定义，而在下面的code中是nested


def f(x, y):
	def g(x):
		return x + y
	return g(x)

def compose1(f, g):
	def h(x):
		return f(g(x))
	return h
	