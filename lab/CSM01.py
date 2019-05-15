"""tree recursion"""
# question 1
def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    n, last = n // 10, n % 10
    if n == 0:
        return True
    elif (n % 10) < last:
        return False
    else:
        return is_sorted(n)    # 不需要再考虑最后两位数的大小关系了，因为已经在前一个检验过了

print(is_sorted(9876543210))


# question 2
def mario_number(level):
    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and 0
        is
    something Mario cannot step on. >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """


# question 3
def make_change(n):
    """Write a function, make_change that takes in an integer amount, n, and returns the minimum number
    of coins we can use to make change for that n,
    using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3 2
    """
    if n == 2:
        return 0
    elif n % 4 == 0:
        return n // 4
    elif n % 4 == 1 or n % 4 == 3:
        return n // 4 + 1
    else:
        use_three = n // 4 + 1  # 用n-4除以4得到的商的整数部分，留下一个6，用两个3
        return use_three
print(make_change(6))



"""data abstraction"""
# question 1
def elephant(name, age, can_fly):
    """
    Takes in a string name, an int age, and a boolean can_fly. Constructs an elephant with these attributes.
    >>> dumbo = elephant("Dumbo", 10, True)
    >>> elephant_name(dumbo)
    "Dumbo"
    >>> elephant_age(dumbo)
    10
    >>> elephant_can_fly(dumbo)
    True
    """
    return [name, age, can_fly]

def elephant_name(e):
    return e[0]

def elephant_age(e):
    return e[1]

def elephant_can_fly(e):
    return e[2]



# question 2
def elephant_roster(elephants):
    """
    Takes in a list of elephants and returns a list of their
    names. """
    # return [elephant[0] for elephant in elephants]
    return [elephant_name(elephant) for elephant in elephants]

# question 3
def elephant(name, age, can_fly):
    return [[name, age], can_fly]

def elephant_name(e):
    return e[0][0]

def elephant_age(e):
    return e[0][1]

def elephant_can_fly(e):
    return e[1]



# question 5
def elephant(name, age, can_fly):
    """
    >>> chris = elephant("Chris Martin", 38, False)
    >>> elephant_name(chris)
        "Chris Martin"
    >>> elephant_age(chris)
        38
    >>> elephant_can_fly(chris)
    False """
    def select(command):
        if command == "name":
            return name
        elif command == "age"
            return age
        elif command == "can_fly"
            return can_fly
        return select

def elephant_name(e):
    return e("name")

def elephant_age(e):
    return e("age")

def elephant_can_fly(e):
    return e("can_fly")