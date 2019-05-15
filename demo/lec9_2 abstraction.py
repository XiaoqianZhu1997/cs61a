
def gcd(m, n):
# return the largest k that divides by both integer
	"""
	>>> gcd(12, 8)
	4
	>>> gcd(16, 12)
	4
	"""
	k = min(m, n)
	while m % k != 0 or n % k!= 0:
		k = k -1
	return k

"""⚠️使用recurive，并且注意gcd(m,n)=gcd(m-n,n)"""
def gcd(m, n):
	if m == n:
		return m
	elif m < n:
		return gcd(n, m)
	else:
		return gcd(m-n, n)



def lcf(m ,n):
# 求最小公倍数
	k = max(m, n)
	while k % m != 0 or k % n != 0:
		k = k + 1
	return k