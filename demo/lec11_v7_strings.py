def curry(f):  # curry第一个argument是f，加上f以后是一个关于x的函数
    def g(x):  # g的第一个argument是x，加上x后，变成与y相关的函数
        def h(y):
            return f(x, y)
        return h
    return g

# curry = lambda f: lambda x: lambda  y: f(x, y)

'curry = lambda f: lambda x: lambda  y: f(x, y)'



"""dictionaries"""
{'I': 1, 'V': 5, 'X': 10}
numerals = {'I': 1, 'V': 5, 'X': 10}