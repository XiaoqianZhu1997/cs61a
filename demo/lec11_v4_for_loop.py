"""❕sequence iteration"""
def count(s, value):
	"""count the number of times that value in sequences"""
	# 计算给定的value这个变量在sequence s中出现的次数
	total = 0    # 在用while循环的时候引入了index = 0
	for element in s:
	# while index < len(s):
		# element = s[index]
		if element == value:
			total = total + 1
	# 之前还用了index = index + 1
	return total

def counts(s, value):
    list = [i for i in s if i == value]
    return len(list)


pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]

same_count = 0
for x, y in pairs:   #这里注意了❕x,y，其实是[x, y]，寻找的是pair中每一对[,]这样的元素。都是按照这个格式开始寻找
	if x == y:
		same_count = same_count + 1

def same_counts(pairs):
    list = [[x, y]for x,y in pairs if x == y]
    return len(list)


# 计算所有小于n的数相加
def sum_below(n):
	total = 0
	for i in range(n):
		total = total + i
	return total

def cheer():  # 0 positional arguments，就算写了x这样的 one positional arguments也不会影响下面的结果。因为下面的循环index与括号内的arguments是没有关系的
	for _ in range(3):   # 用_或者x都没有太大关系，仅仅是表示，在list[0, 1, 2]中即可，这些数字也就三个，意味着循环三次
		print('Go Bears!')

def divisors(n):
	return [x for x in range(1, n) if n%x == 0]
print(divisors(12))

sum(divisors(4))  # 这个sum函数在这里是把lsit里面的每个元素相加，求和

print([n for n in range(1, 1000) if sum(divisors(n)) == n])



def divisor(n):
	list = [1] + [x for x in range(2, n) if n%x == 0]
	return len(list), list

print(list)
print(divisor(12))



# 有面积和高度这两个变量，求宽度
def width(area, height):
	assert area % height == 0
	return area // height

# 求周长
def perimeter(width, height):
	return 2 * width + 2 * height

# ❕❕❕已知面积，要知道能够构成这个面积的最短的周长长度
# 思路是把所有可能的周长都计算出来再去最小值
def minimum_perimeter(area):
	height = divisors(area)   # 所有的高度组合list
	perimeters = [perimeter(width(area, h), h) for h in height]   # 列举出了所有可能的周长list
	return min(perimeters)




"""higher order functions"""
def apply_to_all(map_fn, s):
	return [map_fn(x) for x in s]
# apply_to_all = lambda  map_fn, s: list(map(map_fn, s))

def keep_if(filter_fn, s):
	return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
	reduced = initial
	for x in s:
		reduced = reduce_fn(reduced, x)
	return reduced


def divisors_of(n):
	divides_n = lambda x: n % x == 0
	return [1] + keep_if(divides_n, range(2, n))

from operator import add
def sum_of_divisors(n):
	return reduce(add, divisors_of(n), 0)

def perfect(n):  # 找到所有因子的和与本身相同的数字
	return sum_of_divisors(n) == n

