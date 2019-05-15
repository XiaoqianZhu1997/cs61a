negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)




def scale(f, x, k):
	return k * f(x)
"""使用lambda函数"""
scale(lambda x: x + 10, 5, 2)


"""类似make_adder"""
def multiply_by(m):
    def multiply(n):
        return n * m
    return multiply
"""使用lambda函数"""
def multiply_by(m):
	return lambda n: n * m    #使用lambda的时候，注意的是，他后面接的都是要进行运算的变量，例如这里multiply_by(m)是关于n的函数



times_three = multiply_by(3)
times_three(5)
multiply_by(3)(10)