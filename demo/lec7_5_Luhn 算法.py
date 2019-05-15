"""定义函数为加上从右往左所有奇数位的数字"""
def sum_odd_digits(n):
	if n < 100:
		return n % 10
	else:
		return n % 10 + sum_odd_digits(n // 100)


def twice_digits(n):     #这个是针对于0～9的数字
	twice = 2 * n
	return twice // 10 + twice % 10
"""对从右往左数，位于偶数位子上的数字进行求和，求和的时候每个数字都乘以了2，这种乘以2的计算过程在twice_digits函数中定义"""
def sum_even_digits(n):
	first_odd = n % 10
	first_even = (n // 10) % 10
	if n < 100:
		return twice_digits(first_even)
	else: 

		return twice_digits(first_even) + sum_even_digits(n // 100)

"""按照我们定义的新运算来对每位数求和"""
def new_sum_digits(n):
	return sum_odd_digits(n) + sum_even_digits(n)



"""重新看之前的sum_odd和sum_even，其实计算过程很类似，可以更加简便的定义这个新运算"""
def new_sum_digit(n):
	first_odd = n % 10
	first_even = (n // 10) % 10
	first_two = first_odd + twice_digits(first_even)
	if n < 100:
		return first_two
	else:
		return first_two + new_sum_digit(n // 100)