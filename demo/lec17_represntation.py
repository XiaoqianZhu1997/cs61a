from fractions import Fraction
half = Fraction(1, 2)
repr(half)   # 'Fraction(1, 2)'
half.__repr__()
eval(repr(half))   # Fraction(1, 2)

str(half)   # '1/2'
half.__str__()
eval(str(half))   # 0.5

print(half)   # 1/2


s = "Hello, World"
# eval(s) 报错
# eval(str(s))

repr(s)   # "'Hello, World'"
eval(repr(s))  # 'Hello, World'
print(repr(s))   # 'Hello, World'

repr(repr(repr(s)))    # '\'"\\\'Hello, World\\\'"\''
eval(eval(eval(repr(repr(repr(s))))))   # 'Hello, World'

str(s)  # 'Hello, World'
print(str(s))  # Hello, World



class Bear:
    def __init__(self):
        self.__repr__ = lambda : 'oski'
        self.__str__ = lambda : 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'
print(getattr(Bear, '__repr__'))
print(getattr(Bear, '__str__'))

oski = Bear()
print(type(oski))
print(oski)   # a bear

print('\n')
"repr和str ignore instance attribute，直接查看class内的method"
print(repr(oski))    # Bear()
print(str(oski))    # a bear

print('\n')
print(oski.__str__())    # this bear
print(oski.__repr__())   # oski


def repr(x):
    return type(x).__repr__(x)
print(repr(oski))

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)



class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):  # 考虑和int相加
            numer = self.numer + self.denom * other
            denom = self.denom
        elif isinstance(other, float):
            return float(self) + other
        elif isinstance(other, Ratio):
            numer = self.numer*other.denom + other.numer*self.denom
            denom = self.denom * other.denom
        g = gcd(numer, denom)
        return Ratio(numer//g, denom//g)

    __radd__ = __add__

    def __float__(self):
        return self.numer/self.denom

print(0.2 + Ratio(1, 3))

def gcd(a, b):
    while a != b:
        a, b = min(a, b), abs(b - a)
    return a

"""
def gcd(a, b):
    while b % a != 0:
        if a < b:
            a = b - a
        else:
            a, b = b, a
    return a
"""
# print(gcd(10, 12))
half = Ratio(1, 2)
print(half)

# print(Ratio(1, 3) + Ratio(1, 6))
