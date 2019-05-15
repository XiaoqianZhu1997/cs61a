def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

#############
# Questions #
#############

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) == old:
            return tree(new)
        return t
    return tree(label(t), [replace_leaf(bs, old, new) for bs in branches(t)])

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        return print_move(start, end)
    else:
        midpoint = [i for i in range(1, 4) if i not in [start, end]][0]
        move_stack(n-1, start, midpoint)
        move_stack(1, start, end)
        move_stack(n-1, midpoint, end)


###########
# Mobiles #
###########
def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree('mobile', [left, right])   # return一个tree

def is_mobile(m):
    return is_tree(m) and label(m) == 'mobile'    # m是tree并且lable是mobile

def sides(m):
    """Select the sides of a mobile."""
    assert is_mobile(m), "must call sides on a mobile"
    return branches(m)

def is_side(m):
    return not is_mobile(m) and not is_weight(m) and type(label(m)) == int
# 不是is_mobile意味着，label不会是str，而是数字了。

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return label(s)  # 因为side的label就是length

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree(size)

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return label(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return is_leaf(w)

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    if is_weight(m):
        return True
    left_side, right_side = sides(m)   # 得到左右分支
    left_branch, right_branch = end(left_side), end(right_side)   # 分别得到左右分支的branch，要确定这个branch是否是weight

    left_torque = length(left_side) * total_weight(left_branch)
    right_torque = length(right_side) * total_weight(right_branch)

    return left_torque == right_torque and balanced(left_branch) and balanced(right_branch)


#######
# OOP #
#######

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        time = 0  # 这个只是在函数内部的
        while ((1+self.interest)**time) * self.balance < amount:
            time = time + 1
        return time

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2
    "*** YOUR CODE HERE ***"
    def __init__(self, account_holder):
        self.balance = 0
        self.withdraw_time = 0
        self.holder = account_holder

    def time(self):
        self.withdraw_time =  self.withdraw_time + 1
        return self.withdraw_time  # ⚠️一定要先对variable进行更新，再return，不然就没有将更新的variable传入进去

    def withdraw(self, amount):
        if self.time() <= self.free_withdrawals:
            if self.balance < amount:
                return 'Insufficient funds'
            else:
                self.balance = self.balance - amount
                return self.balance
        elif self.balance < amount + self.withdraw_fee:
            return 'Insufficient funds'
        else:
            self.balance =  self.balance - amount - self.withdraw_fee
            return self.balance


############
# Mutation #
############

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    "*** YOUR CODE HERE ***"
    def counter(x, lst=[]):
        lst.append(x)
        return lst.count(x)
    return counter
    """
    count = {}  空的dict
    def counter(s):
        count[s] = count.get(s, 0) + 1   创建了关于key为s的dict
        return count[s]   得到对应的value
    return counter
    """


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    lst = [2, -1, 1]
    def func():
        nonlocal lst
        lst[0], lst[1] = lst[1], lst[2]
        lst[2] = lst[1] + lst[0]
        return lst[2]
    return func

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    attempts, lst = 0, []
    def codes(amount, code):
        nonlocal balance, password, attempts
        if attempts < 3:
            word = [password] if type(password) == str else password  # 为了make_joint的构造方便，password使用list形式
            if code in word:   # 还是不能直接写in, 因为'a' in 'abc'：if code in [password]
                if amount > balance:
                    return 'Insufficient funds'
                balance = balance - amount
                return balance
            else:
                attempts = attempts + 1
                lst.append(code)
                return 'Incorrect password'
        else:
            return "Your account is locked. Attempts: " + str(lst)
    return codes


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    """
    attempts, code_lst = 0, []
    while attempts < 3:
        if type(withdraw(0, old_password)) == str:    # 说明old_password不对
            attempts = attempts + 1
            code_lst.append(old_password)
            return 'Incorrect password'
        balance = withdraw(0, old_password)  # 得到账户余额
        return withdraw(balance, )
    return "Your account is locked. Attempts: " + str(code_lst)
    """
    check = withdraw(0, old_password)
    if type(check) == str:  # 说明此时得到的是password不对、attempts
        return check   # 并没有改变balance

    # 这个时候old_password是对的
    def joint(amount, attempt):
        if attempt == old_password or attempt == new_password:   # 说明两个密码都可以
            return withdraw(amount, old_password)
        return withdraw(amount, attempt)  # 这个时候密码不对了，就可能输出incorrect password或者attempts

    return joint


###################
# Extra Questions #
###################

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))  # format函数，按照前面的字符，挨个输出其对应的args

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)  # 考虑了负数的情况
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - upper_bound(y)
    p2 = upper_bound(x) - lower_bound(y)
    return interval(p1, p2)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert lower_bound(y) > 0 or upper_bound(y) < 0, "Interval spans 0"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 2) # r1,r2分别不过0,r1+r2也不过0，但是r1*r2可以过0就导致矛盾
    r2 = interval(-3, -4)
    return r1, r2

def multiple_references_explanation():
    return """The multiple reference problem...because par2 asks stronger condition than par1.
    In par2, r1, r2 should meet the condition respectively and so does(r1+r2), 
    while par1 only asks (r1+r2) meets the condition.
    ⚠️Yes. Since interval is an uncertain value, the more times it
          has been referenced, the larger error bound it will produced.⚠️
          """

def quadratic(x, a, b, c):  # 给定区间x和二次函数，求值域
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    f = lambda x: a * x**2 + b * x + c
    l, u, e = lower_bound(x), upper_bound(x), -b / (2*a)
    low, upper, extreme = f(l), f(u), f(e)
    if l <= e and e <= u:
        return interval(min(low, upper, extreme), max(low, upper, extreme))
    return interval(min(low, upper), max(low, upper))


def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
    """几次多项式就有多少个根（包括重根），len(c)-1就代表的是几次多项式，
    按照这个分割区间x。在每个小区间内进行搜寻极值点，从区间中点开始搜寻"""

    ### import newton's method
    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

    def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

    def improve(update, close, guess=1, max_update=100):   # 更新函数，逼近要求，初始值，最大步数
        k = 0
        while not close(guess) and k < max_update:
            guess = update(guess)
            k = k + 1
        return guess

    ### 定义导函数
    # 所求的值域的多项式的函数表达
    def f(x, c):
        i, value = 0,  0
        while i < len(c):
            value = value + c[i] * pow(x, i)
            i = i + 1
        return value
    # 其导数表达式，仅仅变更list：c即可。
    def first_order(c):
        i = 0
        while i < len(c) - 1:
            c[i] = c[i + 1] * (i + 1)
            i = i + 1
        return c[1:]
    # 一阶导数
    def df(x, c):
        return f(x, first_order(c))
    # 要求导数函数的零点，还要知道二阶导数
    def ddf(x, c):
        return f(x, first_order(first_order(c)))

    ### 找到区间的中间点
    def midpoint(x):
        return (upper_bound(x)+lower_bound(x)) / 2

    # 将区间根据方程的幂进行分割，创造一个list包含所有的找寻区间
    step, find_interv = (lower_bound(x) + upper_bound(x)) / len(c), []
    u, l = upper_bound(x), lower_bound(x)
    for i in range(0, len(c)):
        l = l + i * step
        u = l + step
        find_interv += [interval(l, u)]
    # 将每个区间的midpoint作为guess的初始值
    guess_lst = [midpoint(x) for x in find_interv]

    # 定义找根函数
    def find_zero(f, df, guess):  # 输入初始值
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero, guess)

    extreme_lst = []
    for g in guess_lst:
        if find_zero(lambda x: f(x, c),
                     lambda x: f(x, first_order(first_order(c))), g) not in extreme_lst:
            extreme_lst += [g]

    all_possibles = [f(i, c) for i in extreme_lst] + [f(u, c), f(l, c)]

    return interval(min(all_possibles), max(all_possibles))



