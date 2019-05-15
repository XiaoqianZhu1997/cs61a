### question 1
a = [1, 2, 3, 4, 5]
a.pop(3)
b = a[:]   # ⚠️slicing不会mutation，和list的作用类似
a[1] = b
b[0] = a[:]
b.pop()
b.remove(2)
c = [].append(b[1])
a.insert(b.pop(1), a[-3:4:3])
b.extend(b)

if b == b[:] and b[1][1][0] is b[0][1][1]:
    a, b, c = [c] + a[-4:4:2]


# Counstructor
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



### question 2
def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain the same labels the same number of times.
    >> x = tree(1, [tree(2), tree(2), tree(3)])
    >> y = tree(3, [tree(2), tree(1), tree(2)])
    >> about_equal(x, y)
    True
    >> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >> about_equal(x, z)
    False
    """
    def label_counts(t):
        if is_leaf(t):
            return {label(t): 1}   # ❓为什么用label(t)会报错
        else:
            counts = {}
            for b in branches(t) + [tree(label(t))]:  # 包括所有的branches和label
                for lab, count in label_counts(b).items() :
                    if lab not in counts:   # 说明是一个新的
                        counts[lab] = 0    # 创建key
                    counts[lab] += count   # 在这里加进去
            return counts
    return label_counts(t1) == label_counts(t2)



### question 3
def decrypt(s, d):   # s: string & d: dictionary
    """List all possible decoded strings of s.
    >>> codes = {
    ...     'alan': 'spooky',
    ...     'al': 'drink',
    ...     'antu': 'your',
    ...     'turing': 'ghosts',
    ...     'tur': 'scary',
    ...     'ing': 'skeletons',
    ...     'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary
        skeletons']
    """
    if s == '':
        return []
    ms = []
    if s in d:   # 如果dictionary中直接有与s一致的key
        ms.append(d[s])
    for k in range(len(s)):  # 将string进行拆分
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                ms.append(d[first] + ' ' + rest)
    return ms


### question 3
def ensure_consistency(fn):
    """Returns a function that calls fn on its argument, returns fn's
    return value, and returns None if fn's return value is different
    from any of its previous return values for those same argument.
    Also returns None if more than 20 calls are made.
    >>> def consistent(x):
    >>>     return x
    >>>
    >>> lst = [1, 2, 3]
    >>> def inconsistent(x):
    >>>    return x + lst.pop()
    >>>
    >>> a = ensure_consistency(consistent)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    None
    >>> b(6)
    7
    """
    n = 0    # call 次数
    z = {}   # 存储args及其对应输出
    def helper(x):
        nonlocal n
        n = n + 1  # 对call计数
        if n > 20:
            return None
        val = fn(x)
        if x not in z:   # new args
            z[x] = val   # 创建新的key
            return val
        elif val != z[x]:   # different values
            return None
        return val
    return helper
    """
    if x not in z:   
        z[x] = val  
        return val
	if z[x] == [val]:
		return val
	else:
		z[x] = None
		return None
	return helper
    """