class Account:
    interest = 0.02
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance = self.balance - amount
        return self.balance


kirk_account = Account('Kirk')
spock_account = Account('Spock')
kirk_account.interest = 0.08
print(kirk_account.interest, spock_account.interest)
Account.interest = 0.05
print(kirk_account.interest, spock_account.interest)


class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

a = Account('piggy')
b = CheckingAccount('z')
print(a, b)
print(a.balance, b.balance)
a.deposit(100)
b.deposit(100)
print(a.balance, b.balance)
CheckingAccount.withdraw_fee = 2
a.withdraw(10)
b.withdraw(10)
print(a.balance, b.balance)


class Bank:
    def __init__(self):
        self.accounts = []   # 添加账户

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            # a.balance = a.balance + a.interest * a.balance
            a.deposit(a.interest * a.balance)

    def too_big_to_fail(self):
        return len(self.accounts) > 1



bank = Bank()
john = bank.open_account('John', 10)
jack = bank.open_account('Jack', 5, CheckingAccount)
print(john.interest, jack.interest)
bank.pay_interest()
print(john.balance)


class A:
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
b.n = 5   # 仅仅改变instance attribute
print(a.z == C.z, a.z == b.z)
print(b.z, b.z.z, b.z.z.z)   # b.z.z.z.z
print(C(2).n)


########################
# Multiple Inheritance #
########################
class SavingAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

class CleverAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1

clever = CleverAccount('piggy')
print(clever.holder, clever.balance)
print(clever.deposit(100), clever.withdraw(30))


acc = Account('piggy')
print(Account.deposit(acc, 5))



########## example ###########

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized Person: {0})'.format(self.name))

    def tell(self):
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age))

a = Person('Z', 20)
Person.tell(a)  # alternative way: a.tell()

class Man(Person):  # 继承
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Man: {0})'.format(self.name))

    def tell(self):  # 重写基类方法
        Person.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))


class Woman(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score
        print('(Initialized Woman: {0})'.format(self.name))

    def tell(self):  # 重写基类方法
        Person.tell(self)
        print('score: "{0:d}"'.format(self.score))

