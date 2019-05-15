# question 1
# 1.1
a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])
print(len(a), a[3][0], 2 in a)

# 1.2
a = [3, 1, 4, 2, 5, 3]
print(a[4:2])  # 从第四位开始到第二位，又是从左往右，invalid

# Constructor
def tree(label, branches=[]):  # branches default value is empty list
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'  # 一旦出现assertion error就不会进入循环
    return [label] + list(branches)   # create a list from a sequemce of branches

# Selectors
def label(tree):
    return tree[0]   # tree包含两种elemnts，第一个是label，第二个是branches

def branches(tree):
    return tree[1:]

# For convenience
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:  # tree的种类一定是list并且len要大于0。有一个条件不满足都是错
        return False
    for branch in branches(tree):  # tree的branches也要是tree
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


### 3.1 Write a function that returns the largest number in a tree.
def tree_max(t):
    """returns the largest number in a tree."""
    if is_leaf(t):
        return label(t)
    else:
        # 一开始写的是return max(label(t), tree_max(branches(t))).这个问题在于
        # 与链表不同的是，一个tree有多个branch，这样操作会保留仍然是lists而非int，可以比较大小
        return max([label(t)] + [tree_max(b) for b in branches(t)])

t = tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)])
# t = [1, [3, [4], [5], [6]], [2]]
print(tree_max(t))



### 3.2
def height(t):
    """Return the height of a tree"""
    """
    这样写的问题在于，一个tree的branches可能又是多个branches   
    height = 0
    while not is_leaf(t):
        t, height = branches(t), height + 1
    return height
    """
    if is_leaf(t):
        return 0
    return 1 + max(height(b) for b in branches(t))
print(height(t))  # expected 2



### 3.3
def square_tree(t):
    """Return a tree with the square of every element in t"""
    # if is_leaf(t):
        # return tree(label(t)**2)
    # else:
    return tree(label(t)**2, [square_tree(b) for b in branches(t)])
print(square_tree(t))



### 3.4❓❓❓
def find_path(tree, x):
    """ Return a path in a tree to a leaf with value X,
    None if such a leaf is not present.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 6)
    [2, 7, 6]
    >>> find_path(t, 10)
    """
    if label(tree) == x:
        return [x]
    for path in [find_path(branch, x) for branch in branches(tree)]:
        if path:
            return [label(tree)] + path   # 这样仅仅能得到第一种path，不没有输出所有可能的path
    """
    for b in branches(tree):
        for path in [find_path(b, x)]:
            if path:
                return label(tree) + path
    """
t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(11)])
# t = [2, [7, [3], [6, [5], [11]]], [15]]
print(find_path(t, 11))



### 3.5
def prune(t, k):
    """takes in a tree and a depth k and returns a new tree that contains only the first k levels of the original tree."""
    if k == 0:
        return tree(label(t))
    else:
        return tree(label(t), [prune(b, k-1) for b in branches(t)])
print(prune(t, 2))



#######################
######## extra ########
#######################
def tree_size(t):
    """returns the number of nodes in a tree."""
    if is_leaf(t):
        return 1
    else:
        return 1 + sum([tree_size(b) for b in branches(t)])
print(tree_size(t))

##### expression tree #####
"""
contains a function for each non-leaf root, which
can be either add or mul. All leaves are numbers. 
"""
def reduce(fn, s, init):
    reduced = init
    for x in s:
        reduced = fn(reduced, x)   # 反复计算
    return reduced

def apply_to_all(fn, s):
    return [fn(x) for x in s]

from operator import add, mul
def eval_tree(tree):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(tree(1))
    1
    >>> expr = tree(mul, [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree(add, [expr, tree(4)]))
    10
    """
    if is_leaf(tree):
        return label(tree)
    else:
        init = 0 if label(tree) == add else 1  # add的话从0开始，mul的话乘以1
        return reduce(label(tree), apply_to_all(eval_tree, branches(tree)), init)
# 使用recursive，label做函数，但是对于branch部分，需要时已经进行过eval过程了的。
expr = tree(mul, [tree(2), tree(3)])
print(eval_tree(tree(add, [expr, tree(4)])))


##### represent the hailstone sequence #####
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    a hailstone sequence starts with a number n, continuing to n/2
    if n is even or 3n + 1 if n is odd, ending with1
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    # assert n >= 1
    # 要注意的是，一旦得到1就要停止了
    if h == 0:
        return tree(n)
    branches = [hailstone_tree(2 * n, h - 1)]   # 一定会有的情形，base case
    if (n - 1) % 3 == 0 and (n - 1) // 3 > 1:  # 这个条件使得(n-1)//3不会等于1，就意味着前一项并不是1，不会再前一项的位置停止
        branches += [hailstone_tree((n - 1) // 3, h - 1)]  # 两种可能的结果
    return tree(n, branches)
    """
    elif n == 1:
        return tree(n, [hailstone_tree(2*n, h-1)])
    else:
        if (n-1) % 3 != 0:
            return tree(n, [hailstone_tree(2*n, h-1)])
        else:
            return tree(n, [hailstone_tree(2*n, h-1)] + [hailstone_tree((n-1)//3, h-1)])
    """
print(hailstone_tree(1, 4))