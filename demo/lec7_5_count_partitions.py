def count_partitions(n, m):
	"""Count the ways to partition n using parts up to m."""
	# n是要求得得总和，求和过程中用到的数字不能超过m
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = count_partitions(n-m, m)
		without_m = count_partitions(n ,m-1)
		return with_m + without_m