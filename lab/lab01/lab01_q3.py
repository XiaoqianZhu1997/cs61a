def repeated(f, n, x):
	k = 0
	while k < n:
		x = f(x)
		k += 1
	return x