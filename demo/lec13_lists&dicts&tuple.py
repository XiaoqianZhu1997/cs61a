from unicodedata import name, lookup
print(lookup('BABY'))
print(lookup('BABY').encode())

suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()   # pop off with no input always drop off the last elements
suits.remove('string')
print(suits)

suits.append('cup')
suits.extend(['sword', 'club'])
print(suits)

suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
print(suits, original_suits)

numerals = {'I': 1, 'V': 5, 'X': 10}
print(numerals)
print(numerals['X'])
numerals['X'] = 11
print(numerals['X'], numerals)
numerals['L'] = 50   # 添加新的key和value
print(numerals )

numerals.pop('X')
print(numerals)
numerals.get('X')

def mystery(s):
    """the return value is NONE"""
    s.pop()
    s.pop()
four = [1, 2, 3, 4]
print(len(four))
mystery(four)
print(len(four))

def mystery(s):
    s[2:] = []  # 把s中从第二位开始的元素全部去掉

def another_mystery(s):  # 其实应该是没有arguments
    four.pop()
    four.pop()


##########
# Tuples #
##########
def f(s=[]):   # the default value is mutable
    s.append(5)
    return len(s)
print(f())   # got 1
print(f())   # got 2
print(f())   # got 3


nest = list(suits)   # 现在nest还是跟suits一致，但仅仅是value一致，并不是同一个object
print(nest)