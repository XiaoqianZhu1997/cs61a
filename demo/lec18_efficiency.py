def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

"""call_counted"""
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)  # return成了counted函数，从而可以使用.call_count
print(fib(5))
print(fib.call_count)



"""memorization"""
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

# print(fib(30))
# fib = memo(fib)
# print(fib(300))

fib = count(fib)  # return的仍然是f(n)这个结果，但是可以计算call的次数
counted_fib = fib   # 现在用counted_fib来代替（储存）fib函数
fib = memo(fib)
fib = count(fib)  # 现在count括号内的fib函数已经不是最早定义的fib函数，而是经过memo定义的fib函数了
print(fib(30))
print(fib.call_count)  # 59
print(counted_fib.call_count)  # 31


"""space"""
def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted