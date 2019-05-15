def sum_digits(n):
	a, c = n, 0
	while a >= 10:
		a, b = a // 10, a % 10
		c += b
	if a < 10:
		c += a
	return c