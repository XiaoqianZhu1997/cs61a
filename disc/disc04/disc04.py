###################
### 1. Nonlocal ###
###################

# question 1
def stepper(num):
    def step():
        nonlocal num # declares num as a nonlocal variable
        num = num + 1 # modifies num in the stepper frame
        return num
    return step
s = stepper(3)
s()
s()
"""
1. Global variables cannot be modified using the nonlocal keyword.
    在上面，stepper是global frame，num在f1这个frame中，是step的parent frame

2. Variables in the current frame cannot be overridden using the nonlocal keyword. This means we cannot have 
both a local and nonlocal vari- able with the same names in a single frame.
❓是否意味着syntax error
"""


# question 2
lamb = 'da'
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ['da']
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1], 2]) + 3
da(lambda da: da(lamb))


# question 3
def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    # 注意上面的过程中，memory(10)()仍然是一个函数
    def helper(f):
        nonlocal n
        n = f(n)
        print(n)
        return memory(n)  # 或者写成helper
    return helper
f = memory(10)
f = f(lambda x: x * 2)

#######################
### 2. Mutable list ###
#######################
pizza1 = ['cheese', 'mushrooms']
pizza2 = pizza1 + ['onions']
print(pizza2, pizza1)
pizza1.append('onions')
print(pizza1)

# question 1
lst1 = [1, 2, 3]
lst2 = [1, 2 ,3]
print(lst1 == lst2)   # True 仅仅是value相等
print(lst1 is lst2)   # False 不是相同的object

lst2 = lst1
lst1.append(4)
print(lst1, lst2)

lst1 = lst1 + [5]  # 仅仅改变了lst1
print(lst1 == lst2)  # False
print(lst1, lst2)
print(lst1 is lst2)  # False


# question 2
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for i in list(lst):
        if i == x:
            lst.append(el)
lst = [1, 2, 4, 2, 1]
add_this_many(1, 5, lst)
print(lst)
add_this_many(2, 2, lst)
print(lst)


# question 3
def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    length = len(list(lst))
    for i in range(0, length):
        lst.append(lst.pop(length-1-i))
    """
    new_lst = []
    for i in list(lst):
        new_lst.append(lst.pop())
    lst = new_lst
    ⚠️这样写的时候new_lst 和 lst确实得到了想要的结果，但是参数没有传到global frame中
    ⚠️可以使用python tutor查看
    """
x = [3, 2, 4, 5, 1]
reverse(x)
print(x)


#######################
### 3. Dictionsires ###
#######################
pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
print(pokemon['pikachu'])
pokemon['jolteon'] = 135
print(pokemon)
pokemon['ditto'] = 25
print(pokemon)

# question 1
pokemon = {'jolteon': 135, 'pikachu': 25, 'dragonair': 148, 'ditto': 25, 'mew': 151}
print('mewtwo' in pokemon)   # False
print(len(pokemon))   # 5
pokemon['ditto'] = pokemon['jolteon']  # {'jolteon': 135, 'pikachu': 25, 'dragonair': 148, 'ditto': 135, 'mew': 151}
pokemon[('diglett', 'diglett', 'diglett')] = 51  # ⚠️这里是创建了一个新的key和value，这个key是一个tuple
# {'jolteon': 135, 'pikachu': 25, 'dragonair': 148, 'ditto': 25, 'mew': 151, ('diglett', 'diglett', 'diglett'): 51}
pokemon[25] = 'pikachu'   # ⚠️创建了一个新的key
# {'jolteon': 135, 'pikachu': 25, 'dragonair': 148, 'ditto': 25, 'mew': 151, ('diglett', 'diglett', 'digglett'): 51, 25: 'pikachu}
print(pokemon)
# pokemon[['firetype', 'flying']] = 146
# 会报错，因为list不能做key，key是immutable的


# question 2
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    dictionary = {}
    lst = [(i, fn(i)) for i in s]   # 使用tuple这种immutable
    for j in lst:  # 不在dict.keys的，进行添加
        if j[1] not in dictionary:
            dictionary.update({j[1]: [j[0]]})
        else:  # 更新
            dictionary[j[1]].append(j[0])
    return dictionary


# question 3
def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key in d.keys():
        if type(d[key]) == dict:  # recursive
            replace_all_deep(d[key], x, y)  # 不能使用d[ley] = replace，因为replace并没有返回值，这样赋值得到的会是None
        elif d[key] == x:
            d[key] = y



