def double_eights(n):
    a = n
    while a >= 10:
        a, b = a // 10, a % 10 
        if a % 10 == 8 or a == 8 and b == 8:
        	return True 
    if a < 10:
    	return False