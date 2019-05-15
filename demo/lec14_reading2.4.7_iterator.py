"""
>>> primes = [2, 3, 5, 7]
>>> type(primes)
<class 'list'>
>>> iterator = iter(primes)
>>> type(iterator)
<class 'list_iterator'>
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
5


>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d
{'one': 1, 'three': 3, 'two': 2}
>>> k = iter(d)
>>> next(k)
'one'
>>> next(k)
'three'
>>> v = iter(d.values())
>>> next(v)
1
>>> next(v)
3

>>> d.pop('two')
2
>>> next(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
❓RuntimeError: dictionary changed size during iteration❓



>>> r = range(3, 6)
>>> s = iter(r)
>>> next(s)  这里相当于对s进行了更改
3
>>> for x in s:
        print(x)
4
5
>>> list(s)   所有s中的元素都输出了
[]
>>> for x in r:
        print(x)
3
4
5
"""


def double_and_print(x):
    print('***', x, '=>', 2 * x, '***')
    return 2 * x
s = range(3, 7)
doubled = map(double_and_print, s)
# print(list(doubled))  # 如果仅仅print(doubled)得到的结果只是一个<map object>
next(doubled)
next(doubled)
list(doubled)


"""2.4.11   Implementing Lists and Dictionaries"""
"""
Lists need to have an identity, like any mutable value. 
⚠️In particular, we cannot use None to represent an empty mutable list, 
because two empty lists are not identical values 
(e.g., appending to one does not append to the other), but None is None. 
On the other hand, two different functions that each have empty as their local state 
will suffice to distinguish two empty lists.
"""