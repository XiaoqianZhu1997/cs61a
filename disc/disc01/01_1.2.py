def handle_overflow(s1, s2):
	if min(s1, s2) >= 30:
		print('no space left in either section')
	elif max(s1, s2) <= 30:
		print('no overflow')
	elif s2 > s1:
		print('move to section 1:', 30 - s1)
	else:
		print('move to section 2:', 30 - s2)