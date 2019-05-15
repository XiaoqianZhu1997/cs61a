class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

print(Clown.nose)
print(Clown.dance())
print(Clown)

class Account:

    def __init__(self, account_holder):    # constructor
        self.balance = 0         # 这两个是的instance attribute
        self.holder = account_holder
a = Account('Jim')
print(a.holder, a.balance)

a = Account('Jim')
b = Account('Jack')
print(a is a, a is not b)  # True True
c = a
print(c is a)  # binding an object to a new name using assignment does not create a new object


"""Method"""
class Account:

    interest = 0.02   # class attribute

    def __init__(self, account_holder):    # constructor
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount): # self refers to an instance in this class
        self.balance = self.balance + amount  # change the attribute with the assignment
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

tom_account = Account('Tom')
print(tom_account.deposit(100))    # 100

piggy = Account('piggy')   # ⚠️look up an attribute using a string
print(getattr(piggy, 'balance'))
print(hasattr(piggy, 'deposit'))

print(type(Account.deposit))   # 是一个function: standard two-argument
print(type(tom_account.deposit))   # 是一个method: a one-argument method
# take into deposit function and bound it to teh tom_account
"""直接call the class，要写入two arguments"""
print(Account.deposit(tom_account, 1001))


a = Account('Kirk')
print(a.balance)
b = Account('Spock')
b.balance = 200
print([acc.balance for acc in (a, b)])


kirk_account = Account('Kirk')
spock_account = Account('Spock')
kirk_account.interest = 0.08
print(kirk_account.interest)
# Account.interest = 0.05
print(kirk_account.interest, spock_account.interest)



#############################
##### lec16 Inheritance #####
#############################


print(Account.interest)
tom_account = Account('Tom')
tom_account.interest = 0.08    # instance attribute assignment
print(tom_account.interest)
print(Account.interest)
# Account.interest = 0.04   # class attribute assignment
print(Account.interest)

### base class
class CheckingAccount(Account):
    """A bank account that charges for withdrawals"""
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):   # overriden the name
        return Account.withdraw(self, amount + self.withdraw_fee)
z = CheckingAccount('zjl')



a = Account('piggy')
b = CheckingAccount('zen')
a.deposit(100)
b.deposit(100)
print(a.balance, b.balance)
a.withdraw(10)
b.withdraw(10)
print(a.balance, b.balance)



class Bank():
    """A bank *has* account.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts = []    # 列入所有的account的信息

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1   # 如果accounts list超过两个就会fail


#########################
### complicated cases ###
#########################
class A:   # base case
    z = -1
    def f(self, x):
        return B(x-1)


class B(A):
    n = 4

    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)


class C(B):
    def f(self, x):
        return x

a = A()
b = B(1)
print(b.n, b.z, b.z.z, b.z.z.z)
b.n = 5   # instance assignment
print(b.n)  # 5
print(C(2).n)   # 4
print(a.z == C.z)   # True
print(a.z == b.z)   # False


##############################
#### Multiple Inheritance ####
##############################
class SavingAccount(Account):
    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)
print(SavingAccount.deposit_fee)

class AsSeenOnYVAccount(CheckingAccount, SavingAccount):  # withdraw_fee, deposit_fee
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1   # A free dollar when open an account

such_a_deal = AsSeenOnYVAccount('John')
print(such_a_deal.balance)   # 1: free dollar
print(such_a_deal.deposit(20))   # 19: deposit_fee; SavingAccount instance
print(such_a_deal.withdraw(5))   # 13: withdraw_fee; CheckingAccount instance

def depoist_all(winners, amout=5):
    for account in winners:
        account.deposit(amout)

"""查询所有的class"""
print([c.__name__ for c in AsSeenOnYVAccount.mro()])


################################
#### Biological Inheritance ####
################################
