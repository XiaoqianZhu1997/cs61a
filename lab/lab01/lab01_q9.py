def falling(n, k):
	value, l = n, n - 1
	while l > n - k:
		value = value * l
		l = l - 1
		return value
	if k == 0:
		return 1

def falling(n, k):
	result = 1
	while k > 0
		result *= n
		n -= 1
		k -= 1
	return result