"""从右往左找n，找到和d一样的数字就停止"""

def end(n, d):
	while n > 0:
		last, n = n % 10, n // 10
		print(last)
		if last == d:
			return None #如果输入的是return last，那么输出程序结果的时候d也就是last会输出两遍