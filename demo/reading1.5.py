def pow(a, b):
	q, k = a, 1
	while k < b:
		a = a * q
		k = k + 1
	return a