def make_withdraw(balance):
    """return a withdraw function with a starting balance"""
    def withdraw(amount):
        nonlocal balance   # 这样的话，就会改变之前的赋值
        """
        The nonlocal statement changes all of the remaining assignment statements in the definition of withdraw. 
        After executing nonlocal balance, any assignment statement with balance on the left-hand side of = 
        will not bind balance in the first frame of the current environment. 
        此时的balance不会bind一开始的值了，也就是说不会bind to 100了。
        Instead, it will find the first frame in which balance was already defined and re-bind the name in that frame. 
        If balance has not previously been bound to a value, then the nonlocal statement will give an error. --syntax error
        """
        if amount > balance:  # 本来是可以refer到balance的，但是这里后面出现了local assignment
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
withdraw = make_withdraw(100)
withdraw(25)
withdraw(25)
withdraw(60)
withdraw(15)


def make_withdraw_list(balance):
    b = [balance]   # list can be changed
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw
withdraw = make_withdraw_list(100)
withdraw(25)


def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4)
print(b(3), b(4))  # b(3) = 12, b(4) = 14.
# b(3)中，x = 7, y = 2, z = 3，结果即为7+2+3 = 12。因为x一开始是6，nonlocal后，变成了7
# 同理对于b(4)，x =8, y = 2, z = 4,结果即为8+2+4 = 14。
print(total) # 10 + 12 = 22


"""environment diagram"""
def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1, berk-1]
        bear = lambda ley: berk - ley
        return [berk, cal(berk)]
    return cal(2)
oski(abs)