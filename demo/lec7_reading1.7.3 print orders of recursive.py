def cascade(n):
	"""Print a cascade of prefixes of n."""
	if n < 10:
	print(n)
	else:
		print(n)
		cascade(n//10)
		print(n)



"""从个位数开始print"""
def cascade(n):
	if n < 10:
	print(n)  # 一直到了n小于10的时候才开始orint
	else:
		cascade(n//10)  # 前面没有print的时候，到了这里cascade函数就去执行这个函数了，并没有到print
		print(n)

def grow(n):
	if n > 10:
		grow(n // 10)
	print(n)
grow = lambda n: f_then_g(grow, print, n // 10)
"""⚠️运用的if函数，如果n//10不为0的时候，也就是说n>10"""


"""从全部数字一直print到个位数"""
def cascade(n):
	if n < 10:
	print(n)
	else:
		print(n)
		cascade(n//10)

def shrink(n):
	print(n)
	if n > 10:
		shrink(n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


def cascade(n):
	print(n)   # 一开始就print
	if n > 10:
		cascade(n // 10)   # 先执行完函数才print
		print(n)
"""或者可以写成"""
def cascade(n):
    if n > 10:
        print(n)
        cascade(n // 10)
    print(n)



"""inverse cascade"""
def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	if n:
		f(n)
		g(n)
