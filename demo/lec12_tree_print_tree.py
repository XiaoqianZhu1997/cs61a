"""
eg. tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
label是3，也就是说现在的位置是在3，然后3这一点的branches有[1]和[2, [1],[1]]
"""
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
    # 如果是leaf的话，tree(1) = [1], branches=[]，从而branches(tree)=False
    # 不是branches就是tree

# print(tree(1, [5])) 会报错，因为branches不是tree
print(tree(1, [tree(5, [tree(7)]), tree(6)]))
# branches 是一个list，在这里是：[tree(5, [tree(7)]), tree(6)]
# for branch in branches，
# branch分别是：tree(5, [tree(7)])， tree(6)

############### eg ###############
# print(tree(3, [tree(1), tree(2, [tree(1), tree(1)])]))
# [3, [1], [2, [1], [1]]]


def fib_tree(n):
    if n <= 1:
        return tree(n)   # is just a leaf
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

print(fib_tree(4))

# recursive
def count_leaves(t):
    """count the leaves of a tree"""
    if is_leaf(t):
        return 1  # 如果已经是leaf，直接返回1
    else:  # 如果不是leaf，仍有分支，对每一个分支进行计算
        return sum([count_leaves(b) for b in branches(t)])

print(count_leaves(fib_tree(4)))


def leaves(tree):
    """return a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)] # 此时的tree已经是一个leaf了，直接返回
    else:
        return sum([leaves(b) for b in branches(tree)], [])


def increment_leaves(t):
    """return a tree like t but with leaf labels incremented"""
    # 仅仅inrease了leaf的label
    if is_leaf(t): # 如果t是一个leaf
        return tree(label(t) + 1)  # 那么返回值仍然是leaf
    else:
        bs = [increment_leaves(b) for b in branches(t)]   # 对branches中的每一个branch进行recursive
        return tree(label(t), bs)   # keep the label unchanged

def increment(t):
    """return a tree like t but with all labls incremented"""
    return tree(label(t)+1, [increment(b) for b in branches(t)])
    # 不再需要leaf statement，因为如果是leaf，就直接返回了[]


def print_trees(t):
    print(label(t))
    for b in branches(t):
        print_trees(b)

print_trees(fib_tree(4))

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))  # print label的时候是没有空格的
    for b in branches(t):   # branch才有空格
        print_tree(b, indent+1)  # 越接近leaf，就空格越多
print_tree(fib_tree(4))



"""Partition Trees"""
'A partition tree for n using parts up to size m '
'the left (index 0) branch contains all ways of partitioning n using at least one m,'
'the right (index 1) branch contains partitions using parts up to m-1, and'
'the root label is m.'
'在leaf处的labels表示从root到leaf的路径是否正确表示了n的partition'
def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

print(partition_tree(2, 2))

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):  # 说明label不是0，因为要找非0的数相加
            print(' + '.join(partition))   # join()是把string镶嵌到sequence中
    else:
        left, right = branches(tree)   # 这里的tree应该是上面abstraction过后的partition_tree
        m = str(label(tree))  # 表示最大的部分
        print_parts(left, partition + [m])    # 因为在left中，之前是剔除了一个m的
        print_parts(right, partition)
"""
leaf处的True or False表示了能否符合要求准确partitionizing
此时也是将label不停迭代，因为label其实代表的是在partition过程中，每一个部分的取值
"""
print_parts(partition_tree(2, 2))


"""
    对tree的branch进行限制
    A binarized tree has at most two branches.
    A common tree transformation called binarization finds a binarized tree with the same labels as an original tree 
by grouping together branches.
"""
def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))

# 这个函数是要将最多两个branch的限制实现
def binarize_branches(bs):   # bs是一个由多个branches组成的list
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]  # 就是将这一系列的branehs分为第一个和剩下的，先对第一个进行操作--base case
        return [right_binarize(first), binarize_branches(rest)]
    # 对于第一个，将其变成a specific tree：
    else:
        return [right_binarize(b) for b in bs]

# print(binarize_branches(branches(partition_tree(2, 2))))
print(right_binarize(tree(0, [tree(x) for x in [1, 2, 3, 4, 5]])))




####################################
########### Linked Lists ###########
####################################
'data abstraction'
# eg.1	four = [1, [2, [3, [4, 'empty']]]]
empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))
    # 要么是empty，要么有两个长度，rest部分仍旧是linked lists

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest)
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s)   # "first only applies to linked lists."
    assert s != empty  # "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s)
    assert s != empty
    return s[1]

four = link(1, link(2, link(3, link(4, empty))))
print(first(four))
print(rest(four))


def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1   # s == empty的时候不计长度
    return length

def getitem_link(s, i):  # index仍旧和list中的一致，第一个数index是0
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

print(len_link(four))
print(getitem_link(four, 1))



###############################################
########### Recursive manipulation. ###########
###############################################
"""define the above function in a recursive way"""
def len_link_recursive(s):
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    if i == 0:
        return first(s)
    return getitem_link(rest(s), i-1)


def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
print(extend_link(four, four))


def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
print(apply_to_all_link(lambda x: x**2, four))


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert  is_link(s)
    if s == empty:
        return s
    else:
        return [first(s), keep_if_link(f, rest(s))] if f(first(s)) else [keep_if_link(f, rest(s))]
    # 这样会有一个问题，empty没有输出
    # length = len_link_recursive(s)+1
    # return [getitem_link(s, i) for i in range(length) if f(getitem_link(s, i))]
print(keep_if_link(lambda x: x%2 == 0, four))


def join_link(s, separator):   # 每一次join的时候，都消除了一次[]
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return s
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
print(join_link(four, ": "))


###############################################
########### Recursive Construction. ###########
###############################################
def partitions(n, m):
    if n == 0:
        return link(empty, empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)   # 用了一个m后剩下的部分
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)   # link(m, s)中表示已经用了一个m
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)   # apply_to_all_link的返回值仍然是一个链表
    print(lists)
    print(strings)
    print(join_link(strings, "\n"))   # \n 表示换行

print_partitions(6, 4)
