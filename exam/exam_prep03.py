# question 1
x, y, z = 1, 2, 3
y = [x, [y, [z, []]]]
print(y)
x = [y[1][0], y, len(y[1][1][1])]
print(x)
z = x[2]
print(z)


"""Tree Recursion with Trees"""

# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:  # tree的种类一定是list并且len要大于0。有一个条件不满足都是错
        return False
    for branch in branches(tree):  # tree的branches也要是tree
        if not is_tree(branch):
            return False
    return True


# question 1
def sum_range(t):
    """Returns the range of the sums of t, that is, the
    difference between the largest and the smallest sums of t."""
    def helper(t):
        if is_leaf(t):
            return (label(t),label(t))
        else:
            a = min([helper(bs)[1] for bs in branches(t)])
            b = max([helper(bs)[0] for bs in branches(t)])
            x = label(t)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y
t = tree(5, [tree(1, [tree(7, [tree(4, [tree(3)])]), tree(2)]), tree(2, [tree(0), tree(9)])])
print(sum_range(t))


# question 2
def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
     """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a = no_eleven(n-1)
        return [s+[6] for s in a] + [s+[1] for s in a if s[n-2] != 1]
print(no_eleven(4))


# question 3
def eval_with_add(t):
    """Evaluate an expression tree of * and + using only addition.
    >>> plus = Tree('+', [Tree(2), Tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = Tree('*', [Tree(2), Tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = Tree('*', [Tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(Tree('*'))
    1
    """
    if is_leaf(t):
        return label(t) if label(t) not in ['+', '*'] else 1
    elif label(t) == '+':
        return sum([eval_with_add(bs) for bs in branches(t)])
    elif label(t) == '*':
        total = 1
        for bs in branches(t):
            total = total * eval_with_add(bs)
        return total

plus = tree('+', [tree(2), tree(3)])
print(eval_with_add(plus))
times = tree('*', [tree(2), tree(3)])
print(eval_with_add(times))
deep = tree('*', [tree(2), plus, times])
print(eval_with_add(deep))
print(eval_with_add(tree('*')))

