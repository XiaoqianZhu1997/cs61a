# question 1
def longest_increasing_suffix(n):
       
       """Return the longest increasing suffix of a positive integer n.
       >>> longest_increasing_suffix(63134)
       134
       >>> longest_increasing_suffix(233)
       3
       >>> longest_increasing_suffix(5689)
       5689
       >>> longest_increasing_suffix(568901)  # Note: 01 is the suffix, displayed as 1
       1
       """

       m, suffix, k = 10, 0, 1
       while n: # 其实就是说明此时n>10，因为当n<10时，再经过一次迭代就需要直接输出结果
              n, last = n // 10, n % 10
              if m > last:
                     m, suffix, k = last, suffix + last * k, 10 * k
              else:
                     return suffix
       return suffix


# question 2
def sandwich(n):
       """Return True if n contains a sandwich and False otherwise
       >>> sandwich(416263)    # 626
       True
       >>> sandwich(5050)      # 505 or 050
       True
       >>> sandwich(4441)      # 444
       True
       >>> sandwich(1231)
       False
       >>> sandwich(55)
       False
       >>> sandwich(4456)
       False
       """
       tens, ones = (n//10) % 10, n % 10  # 输出十位数和个位数
       n = n // 100
       while n: # 说明一开始输入的n是大于100的数
              if ones == n % 10:
                     return True
              else:
                     tens, ones = n % 10, tens
                     n = n // 10
       return False


# question 3
def luhn_sum(n):
       """Return the Luhn sum of n.
       >>> luhn_sum(135)     # 1 + 6 + 5
       12
       >>> luhn_sum(185)     # 1 + (1+6) + 5
       13
       >>> luhn_sum(138743)  # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3 
       30
       """
       def luhn_digit(digit):
              x = digit * multiplier
              return (x // 10) + (x % 10)
       total, multiplier = 0, 1 
       while n:
           n, last = n // 10, n % 10
           total = total + luhn_digit(last)
           multiplier =  3 - multiplier
       return total

# 另一种方法：
"""
def luhn_sum(n):
       n, last = n // 10, n % 10
       sum = 0
       while n:
              m = n % 10
              if m < 5:
                     sum = sum + 2 * m + last
              else:
                     ones = (2 * m) % 10
                     sum = sum + ones + 1 + last
       return sum
"""

# 使用递归
"""
def luhn_sum(n):
       remain_number, last = n // 10, n % 10
       if n < 10:
              return n
       elif n < 100:
              return ((2 * remain_number) % 10)+ ((2 * remain_number) // 10) + last
       else:
              return luhn_sum(remain_number) + last
"""


# question 4
from operator import add, mul
def square(x):
       return mul(x, x)

def dog(bird):
       def cow(tweet, moo):
              woof = bird(tweet)
              print(moo)
              return woof
       return cow

cat = dog(square)


# question 5
batman, superman, ivy = 1, -2, -3

def nanana(batman):
       while batman(superman) > ivy:
              def batman(joker):
                     return ivy
       return -ivy

def joker(superman):
       if superman(batman):
              ivy = -batman
       return nanana

joker(abs)(abs)


# question 6:
def peace(today):
       harmony = love + 2
       return harmony + today(love+1)

def joy(peace):
       peace, love = peace+2, peace+1
       return love // harmony

love, harmony = 3, 2
peace(joy)



