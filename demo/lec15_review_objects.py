class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

print(Clown.nose)
print(Clown.dance())
print(Clown)

class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
a = Account('Jim')
print(a.holder)
print(a.balance)

b = Account('Jim')
print(a is b)

c = a
print(c is a)



class Account:

    def __init__(self, account_holder, interest=0.02):
        self.balance = 0
        self.holder = account_holder
        self.interest = interest

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
p = Account('piggy')
print(p.balance, p.holder)
print(p.deposit(20))
print(p.withdraw(5))

print(getattr)
print(getattr(p, 'deposit'))  # <bound method Account.deposit of <__main__.Account object at 0x10d39cb38>>
print(hasattr(p, 'name'))
print(hasattr(p, 'withdraw'))

print(type(Account.deposit))
print(type(p.deposit))

tom_account = Account("Tom")
jim_account = Account('Jim')
print(tom_account.balance)
print(tom_account.interest, jim_account.interest)
print(tom_account.interest == jim_account.interest)
print(tom_account.interest is jim_account.interest)

tom_account.interest = 0.05
print(tom_account.interest)
Account.interest = 0.08
print(tom_account.interest, jim_account.interest)


Account.__bool__ = lambda self: self.balance != 0
print(bool(Account('Tom')))
print(Account.__bool__(tom_account))
if not Account('Tom'):
    print('Tom has nothing')