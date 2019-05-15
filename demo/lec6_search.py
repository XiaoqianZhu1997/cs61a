def search(f): #找到使得f(x)为True的x值
	x = 0
	while True: #这里表示无限循环，true是一个指示，一般的结构都是while+condition
		if f(x):  #这里f(x)是一个condition，一般形式都是if+condition(如n>k)，如果语句为真就要输出，语句不对就要继续循环
			return x   #输出使得f(x)为True value 的值
		x = x + 1

"""more concise code"""
def search(f): 
	x = 0
	while not f(x):   #说明当f(x)为假的时候就进行循环，不然就输出x
		x += 1
	return x 



def is_three(x):
	return x == 3 #这个应该是表示‘x == 3’ 这个表述的正确或错误，之前的def是return到例如return x * 3，输出的结果应该是ture/false

def square(x):
	return x * x #这里的返回值都是数值，一般return可以是数值/函数/真假condition
 
def positive(x):
	return max(0, square(x) - 100) #在语言里，默认0-False，其他值True


def inverse(f):
	"""return g(y) such that g(f(x)) = x """
	return lambda y: search(lambda x: f(x) == y) 
	"""search(f)函数是要找到使得f(x)为真的x的值，在这里是指找到使得f(x)等于y的x的值"""
	"""写了两次lambda应该是因为要return 一个与y有关的函数，并且如果一开始没有对y进行说明，在最后用到的f(x)=y，会报错"""