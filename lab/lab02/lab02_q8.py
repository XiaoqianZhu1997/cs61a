def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        def g(y):
            if x == 0:
                return y
            elif x % 3 == 1:
                return f1(h(x - 1)(y))
            elif x % 3 == 2:
                return f2(f1(h(x - 2)(y)))
            else:
                return f3(f2(f1(h(x - 3)(y)))) 
        return g
    return h

def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3

my_cycle = cycle(add1, times2, add3)
identity = my_cycle(0)

add_one_then_double = my_cycle(2)

do_all_functions = my_cycle(3)

do_more_than_a_cycle = my_cycle(4)

do_two_cycles = my_cycle(6)