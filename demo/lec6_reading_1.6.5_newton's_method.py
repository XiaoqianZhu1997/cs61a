### for special cases:

def square_root_uodate(x, a):
    return (x + a/x) / 2

def cube_root_update(x, a):
    return (2*x + a/(x**2)) / 3

### 开始逐个更新guess
def improve(update, close, guess=1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k = k + 1
    return guess

### 设置误差
def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

### for special cases
def suqareroot(a):
    def udpdate(x):
        return square_root_uodate(x, a)
    def close(x):
        return approx_eq(x**2 ,a)
    return improve(update, close)

def cuberoot(a):
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_eq(x**3, a))


### for general cases
def newton_update(f, df):
    def update(x):   # nested function，这样做是因为还要引入新的变量x，有f(x)和df(x)
        return x - f(x) / df(x)
    return update
"""要注意的是，因为这里global frame中f和df都是关于x的函数，都是要引入x的，所以在下面会再次定义update，也是为了引入x"""


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root(a):
    def f(x):
        return x**2 - a
    def df(x):
        return 2*x
    return find_zero(f, df)

def cube_root(a):
    return find_zero(lambda x: x**3 - a,
                     lambda x: 3*x**2)

def power(x, n):
    product, k = 1, 0
    while k < n:
        product = product * x
        k = k + 1
    return product

def root(n, a):   # 关于a的n次方根
    return find_zero(lambda x: power(x, n) - a,
                     lambda x: n * power(x, n-1))