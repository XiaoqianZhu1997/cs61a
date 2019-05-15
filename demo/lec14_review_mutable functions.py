def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x

diff = percent_difference(40, 50)

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
print(withdraw(10))
print(withdraw(25))

def make_withdraw_list(balace):
    b = [balace]
    def withdraw(amount):
        if amount > b[0]:
            return "Insufficient amount"
        b[0] = b[0] - amount
        return b[0]
    return withdraw


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
print(total)

def oksi(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1, berk-1]
        bear = lambda ley: berk-ley
        return [berk, cal(berk)]
    return cal(2)
print(oksi(abs))