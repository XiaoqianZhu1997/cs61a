HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    st_a, ave_a = street(a), avenue(a)
    st_b, ave_b = street(b), avenue(b)
    return abs(st_a - st_b) + abs(ave_a - ave_b)


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    from math import sqrt, modf
    return [round(sqrt(i)) for i in s if modf(sqrt(i))[0] == 0]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        i = 3
        first,  second, third = 1, 2, 3
        while i < n:
            value = 3 * first + 2 * second + third
            first = second
            second = third
            third = value
            i = i + 1
        return value
    """✅solutions✅
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c
    """


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    i, value, change_time = 0, 0, 0
    while i < n:
        if change_time % 2 != 0 and (i % 7 == 0 or has_seven(i)): # 表示该位置满足reverse 的条件
            func = lambda x: x - 1
            change_time += 1
        elif change_time % 2 == 0 and (i % 7 == 0 or has_seven(i)):
            func = lambda x: x + 1
            change_time += 1
        value = func(value)
        i = i + 1 # 表示进行到了第几位置 
    return value
    """✅solutions✅
    def helper(k, direction, ret):
        if k == n:
            return ret + direction
        elif k % 7 == 0 or has_seven(k):
            return helper(k + 1, -direction, ret + direction)
        else:
            return helper(k + 1, direction, ret + direction)

    return helper(1, 1, 0)
    """

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    i = 0  # 找到amount的范围2^n ~ 2^(n+1)
    while pow(2, i) < amount:
        i += 1
    def constrain(num, index):  # 计算得到amo1nt，但是最大数字只能是pow(2, index)
        if num < 0:
            return 0
        elif num == 0:
            return 1
        elif index == 0:
            return 1
        else:
            return constrain(num-pow(2, index), index) + constrain(num, index-1)
            # 一定有pow(2, index) 和 一定没有pow(2, index)
    return constrain(amount, i-1)

    """
    ❕灵活度更高❕
    答案的思路是一定含有1，到不含1但含有2，依次增加
    ✅solutions✅
        def constrained_count(amount, smallest_coin):
        if amount == 0:
            return 1
        if smallest_coin > amount:
            return 0
        without_coin = constrained_count(amount, smallest_coin * 2)   # 从2开始
        with_coin = constrained_count(amount - smallest_coin, smallest_coin)  # 一定含有1最小的
        return without_coin + with_coin
    return constrained_count(amount, 1)
    """


###################
# Extra Questions #
###################
# ❓❓❓
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n: 1 if n == 1 else mul(n, )
