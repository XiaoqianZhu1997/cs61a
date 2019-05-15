def make_adder(x):
    """ Returns a one-argument function that returns the result of
    adding x and its argument. """
    def adder(y):
        return x + y
    return adder

def make_counter():
    """Makes a counter function.

    >>> counter = make_counter()
    >>> counter()
    1
    >>> counter()
    2
    """
    count = 0
    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter

counter = make_counter()
print(counter())