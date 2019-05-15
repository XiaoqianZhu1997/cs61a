def even(f):
	def odd(x):
		if x < 0:
			return f(-x)   
		return f(x)   #其实是说明当x>0的时候，直接输出f(x)，其实就是省略了前面有个else 的表达
	return odd

steven = lambda x: x
stewart = even(steven)


def cake():
	print('beets')
	def pie():
		print('sweets')
		return cake
	return pie
chocolate = cake() #这个时候给chocolate赋值为cake(),并且call 了cake()所以会得到beets。⚠️但是并不会告诉你函数的类型，因为并没有询问，要在下一行的命令才会告知函数信息
chocolate   #这个代表是个函数
chocolate()  #这个时候相当于cake()()也就是pie()，所以call 了pie()，会显示出sweets

cake()  #这个时候print会执行，然后return到函数pie
cake()()  #这个时候两个print都会执行，return到pie()，也就是cake
cake()()()  #相当于又再次回到第一个的循环

more_chocolate, more_cake = chocolate(), cake

def snake(x, y):
	if cake == more_cake:
		return lambda z: x + z   #⚠️这个时候y并没有任何作用
	else:
		return x + y

snake(10, 20)  #这个是一个lambda function，因为more_cake == cake
snake(10, 20)(30)   #⚠️输出结果是40，因为这里snake(10, 20)理解成一个函数f(y)，这个时候y就是我们输入的30，而要执行的x + y中的x = 10

cake = 'cake'
snake(10, 20) #这个时候if语句判断是错误的，所以直接return x+y的值，而非函数