def is_prime(n):
	k = n - 1
	while k > 1:
		if n % k == 0:
			return False
		k = k - 1
	return True