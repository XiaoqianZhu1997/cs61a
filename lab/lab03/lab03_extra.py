""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions
"""question 4"""
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    """ lab02 已经写过"""

"""question 5"""
## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: 10 * y + x % 10   # 就是把原数字的个位先乘以10，再加上下一位数
    while x > 0:
        x, y = x // 10, f()  # f()表示都会return到value
    return y == n



## More recursion practice
"""question 7"""
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    assert n > 0
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


"""question 8"""
def factor_num(n, k):  # 计算数字n中，因子大小不超过k的个数
    if k == 1:
        return 1
    elif n % k != 0:
        return factor_num(n, k - 1)
    else:
        return factor_num(n, k - 1) + 1

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    return factor_num(n, n - 1) == 1



"""question 9"""
# ⚠️
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    # use two helper functions
    def odd_function(i):
        if i == n:
            return odd_function(i)
        return odd_function(i) + even_function(i+1)
    def even_function(i):
        if i == n:
            return even_function(i)
        return even_function(i) + odd_function(i+1)
    return odd_function(1)

    
    # use one helper function
    def helper(i, term1, term2):
        if i == n:
            return term1(i)
        return term1(i) + helper(i+1, term2, term1)
    return helper(1, odd_term, even_term)


"""question 10"""
from operator import mul
def is_equal_then_one(n, k):
    if n == k:
        return 1
    else:
        return 0
def digit_show_times(n, k):  # 数字k在n中出现了几次
    if n < 10 and n == k:
        return 1
    elif n < 10 and n != k:
        return 0
    else:
        return digit_show_times(n // 10, k) + is_equal_then_one(n % 10, k)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    pair_1_9 = mul(digit_show_times(n, 1), digit_show_times(n, 9))
    pair_2_8 = mul(digit_show_times(n, 2), digit_show_times(n, 8))
    pair_3_7 = mul(digit_show_times(n, 3), digit_show_times(n, 7))
    pair_4_6 = mul(digit_show_times(n, 4), digit_show_times(n, 6))
    pair_5 = (digit_show_times(n, 5) * (digit_show_times(n, 5) - 1)) // 2
    return pair_5 + pair_4_6 + pair_3_7 + pair_2_8 + pair_1_9
