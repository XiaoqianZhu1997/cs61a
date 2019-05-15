####################
##### Mutation #####
####################

### question 1
a = [1, 2]
a.append([3, 4])
print(a)

b = list(a)
a[0] = 5
a[2][0] = 6
print(a, b)

a.extend([7])
a += [8]
print(a)

b[2][1] = a[2:]
print(b, a[2][1][0][0])


### question 2
a = [1, 2, [3]]
def mystery(s, t):
    s.pop(1)
    return t.append(s)   # ⚠️return value会是None，因为这里用到了append
b=a
a += [b[0]]
a = mystery(b, a[1:])  # ⚠️输出结果是None
print(b)


### question 3
def accumulate(lst):
    """
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    """
    accumu = 0
    for i in range(0, len(list(lst))):
        if isinstance(lst[i], list):
            inside = lst[i]   # 两个会一起变化
            accumu = accumu + accumulate(inside)   # 计算总值，同时也会改变inside
        else:
            accumu = accumu + lst[i]
            lst[i] = accumu
    return accumu



####################
##### Nonlocal #####
####################

# question 1
eggplant = 8
def vegetable(kale):
    def eggplant(spinach):
        nonlocal eggplant
        nonlocal kale
        kale = 9
        eggplant = spinach
        print(eggplant, kale)   # ⚠️eggplant函数的返回值是None
    eggplant(kale)
    return eggplant   # 此时的return value是'kale'
spinach = vegetable('kale')


# question 2
def has_seven(k): # Use this function for your answer below
    if k % 10 == 7:  # 末尾是7或者是个位数7
        return True
    elif k < 10:    # 不是7的其他个位数
        return False
    return has_seven(k // 10)


def make_pingpong_tracker():
    """ Returns a function that returns the next value in the
    pingpong sequence each time it is called.
    >>> output = []
    >>> x = make_pingpong_tracker()
    >>> for _ in range(9):
    ... output += [x()]
    >>> output
    [1, 2, 3, 4, 5, 6, 7, 6, 5]
    """
    index, current, add = 1, 0, True
    def pingpong_tracker():
        nonlocal index, current, add
        if add:   # 之前的运算方法会保持到要变化的这一位，也就是按照之前的计算方法得到这一位之后才开始改变
            current = current + 1
        else:
            current = current - 1
        if has_seven(index) or index % 7 == 0:
            add = not add
            index = index + 1
        return current
    return pingpong_tracker