"""question 1"""
def kbonacci(n, k):
	"""Return element N of a K-bonacci sequence.
    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
	"""
	if n < k - 1:
		return 0 
	elif n == k - 1: 
		return 1
	else:
		total = 0 
		i = n - k
		while i < n:
			total = total + kbonacci(i, k)
			i = i + 1
		return total

"""question 2"""
def combine(left, right):
	"""Return all of LEFT's digits followed by all of RIGHT'sdigits."""
	factor = 1
	while factor <= right:
		factor = factor * 10 
	return left * factor + right

def reverse(n):
	"""Return the digits of N in reverse. 
	>>> reverse(122543)
	345221
	"""
	if n < 10:
		return n 
	else:
		return combine(n % 10, reverse(n // 10))

def remove(n, digit):
	"""Return all digits of N that are not DIGIT, for DIGITless than 10.
	>>> remove(243132, 3)
	2412
	>>> remove(remove(243132, 1), 2)
	433
	"""
	removed = 0
	while n != 0:
		n, last = n // 10, n % 10
		if last != digit:
			removed = combine(removed, last)
	return reverse(removed)


"""question 3"""
lamb = lambda lamb: lambda: lamb + lamb
lamb(1000)() + (lambda b, c: b * b - c)(lamb(2)(), 1)



"""question 4"""
def mouse(n):
	if n >= 10:
		squeak = n // 100
		n = frog(squeak) + n % 10
	return n

def frog(croak):
	if croak == 0:
		return 1
	else:
		return 10 * mouse(croak+1)

mouse(357)


"""quetsion 5"""
from operator import add

avenger = 6

def vision(avengers):
	print(avengers)
	return avengers + 1

def hawkeye(thor, hulk):
	love = lambda black_vidov: add(black_vidov, hulk)
	return thor(love)

def hammer(worthy, stone):
	if worthy(stone) < stone:
		return stone
	elif worthy(stone) > stone:
		return -stone
	return 0

capt = lambda iron_man: iron_man(avengers)


