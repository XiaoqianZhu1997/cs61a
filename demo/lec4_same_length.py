def same_length(a, b):
	if digits(a) == digits(b):
		return True
	else:
		return False




def digits(n):
	q, k = n, 1
	while q >= 10:
		k = k + 1
		last= n % 10
		q = q // 10
	return k
