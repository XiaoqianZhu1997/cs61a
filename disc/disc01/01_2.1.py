def keep_ints(cond, n):  #从小到大输出
	k = 1
	while k <=n :
		if cond(k) == True:
			print(k)
		k = k + 1
 
def keep_ints(cond, n):   #变换循环赋值的位置
	k = 0
	while k <=n :
		k = k + 1
		if cond(k) == True:
			print(k)

def keep_ints(cond, n):   #从大到小输出
	k = n
	while k > 0:
		if cond(k) == True:
			print(k)
		k = k - 1
		

def is_even(x):
	return x % 2 == 0