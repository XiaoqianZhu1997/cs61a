def keep_ints(n):   
	def ints(cond):
		k = 1
		while k < n:
			if cond(k) == True:
				print(k)
			k = k + 1
	return ints

#题目要求的是n固定以后，keep_ints(n)就是固定的函数，唯一的变量是cond
