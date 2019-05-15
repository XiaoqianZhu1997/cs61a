def go(n):
	while n % 2 == 0 and n > 0:
		n = n / 2
		print(n)
	if n % 2 == 0 and n <= 0:
		return None
	else:
		return n / 2

#这里想的是对于偶数，大于0的就进行循环，小于0的输出none；对于奇数直接输出。
