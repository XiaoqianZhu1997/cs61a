"""Question 2.1"""
def recur_mul(m, n):
	if n == 0:
		return 0
	elif n == 1:
		return m
	else:
		return m + recur_mul(m, n - 1)



"""Question 2.2"""
def countdown(n):
	if n == 1:        #要考虑n为负数的情形吗？
		print(n)
	else:
		print(n)
		return countdown(n - 1)
"""⚠️"""
def count_down(n):
    if n > 1:
        print(n)
        count_down(n - 1)
    print(n)
	





"""Question 2.3"""
def countup(n):
	if n <= 0:
		return
	countup(n - 1) #不能写return
	print(n)

def count_up(n):
    if n > 1:
        count_up(n - 1) 
        print(n)
    else:
        print(n)
		



"""Question 2.4"""
def sum_digits(n):
	if n < 10:
		return n
	else:
		return n % 10 + sum_digits(n // 10)