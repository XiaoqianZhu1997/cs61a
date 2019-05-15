def is_even(n):
	if n == 0 or n == 2:
		return True
	elif n == 1:
		return False
	else:
		return is_even(n - 2)
