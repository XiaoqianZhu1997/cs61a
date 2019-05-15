def xk(c, d):
	if c == 4:
		return 6
	elif d > 4:
		return 6 + 7 + c
	else:
		return 25


def how_big(x):
	if x > 10:
		print('huge')
	elif x > 5:
		return 'big'
	elif x > 0:
		print('small')
	else:
		print("nothin'")


def so_big(x):
	if x > 10:
		print('huge')
	if x > 5:
		return 'big'   #⚠️if 和 elif，如果是两个if的话，那就都要走一遍，如果是走了一个下一个就不走了⚠️return以后函数就结束了
	if x > 0:
		print('small') #如果x的值使得其走到了这一步，那么下面的print也会执行，因为这一行是print而不是return
	print("nothin'")


def ab(c, d):
	if c > 5:
		print(c)
	elif c > 7:
		print('foo')
	print('foo')


def bake(cake, make):
	if cake == 0:
		cake = cake + 1
		print(cake)
	if cake == 1:
		print(make)
	else:
		return cake
	return make
#bake(0, 29): 进入第一个if，然后print cake=1，然后进入第二个if，print make=29，接下来才是return
#bake(1, "mashed potatoes")，这里要⚠️的是print和return 的区别，在print的时候，引号不会出现，而return的话会出现引号，但不管之前是什么引号，都会显示单引号‘’
