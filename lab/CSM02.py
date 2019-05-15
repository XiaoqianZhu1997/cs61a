# question 2
def reverse(lst):
    if len(lst) <= 1:
        return lst
    return reverse(lst[1:]) + [lst[0]]
lst = [1, [2, 3], 4]
rev = reverse(lst)
print(rev)

# question 3
def is_prime(n):
    factor = [i for i in range(1, n) if n % i == 0]
    return len(factor) == 1

def all_primes(nums):
    return [i for i in nums if is_prime(i)]


# question 4
def list_of_lists(lst):
    """
    >>> list_of_lists([1, 2, 3])
    [[0], [0, 1], [0, 1, 2])
    >>>list_of_lists([1])
    [[0]]
    >>>list_of_lists([])
    []
    """
    return [[0] + lst[:i] for i in range(0, len(lst))]
# print(list_of_lists([1, 2, 3]))


"""tree"""
def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:] # returns a ⚠️list⚠️ of branches

def is_leaf(t):
    return branches(t) == []

# question 1
t0 = tree(4,
          [tree(5, []),
           tree(2,
                [tree(2, []),
                 tree(1, [])]),
           tree(1, []),
           tree(8,
                [tree(4, [])])])
tt0 = [4, [5], [2, [2], [1]], [1], [8, [4]]]
print(t0, branches(t0))
t = tree(9,
         [tree(2, []),
          tree(4,
               [tree(1, [])]),
          tree(4,
               [tree(7, []),
                tree(3, [])])])
tt = [9, [2], [4, [1]], [4, [7], [3]]]
print(t, label(t), branches(t))

# question 4
def sum_of_nodes(t):
    """
    >>> t = tree(...) # Tree from question 2.
    >>> sum_of_nodes(t) # 9 + 2 + 4 + 4 + 1 + 7 + 3 = 30
    30
    """
    """
    if is_leaf(t):
        return label(t)
    else:
        sum_bs = [sum_of_nodes(bs) for bs in branches(t)]
        return label(t) + sum(sum_bs)
    """
    return label(t) + sum([sum_of_nodes(b) for b in branches(t)])
print(sum_of_nodes(t))
