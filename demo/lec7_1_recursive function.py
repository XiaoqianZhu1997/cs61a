def digit_sum(a):
	total = 0
	while n > 0:
		n, last = split(n)
		total = total + last
	return total

"""sum digits without a while statement"""
def split(n):
	return n // 10, n % 10

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

"""或者我自己写成："""
def sum_digits(n):
	if n < 0:
		return n
	else:
		return n % 10 + sum_digits(n // 10)


def divide_by_9(b):
	if digit_sum(b) % 9 == 0:
		return True
	else:
		return False


def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)

 