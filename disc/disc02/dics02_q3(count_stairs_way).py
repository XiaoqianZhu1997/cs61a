
"""	question 3.1"""
def count_stair_ways(n):
	"""总共n个台阶，要么一次走1步，要么一次走2步，那么区别就在于：最后一次是走了一步，还是两步"""
	if n <= 0:
		return 0
	elif n <= 2:
		return n
	else:
		return count_stair_ways(n-2) + count_stair_ways(n-1)


"""	question 3.2"""
"""
前面的做法是，最后一步固定为1，然后求n-1的步数
再加上最后一步固定为2，求n-2的步数
"""

"""
这里一样的道理，最后一步固定为1，一直到最后一步固定为k全部求和
"""

def count_k(n, k):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		total = 0
		i = 1
		while i <= k:
			total = total + count_k(n-i, k)
			i += 1
		return total