a = lambda x: x   #a是一个函数，返回值为value -- x

lambda: 3    #这个时候为一个函数，类似于def f而非def f(x)，所以要注意想看他的类型的时候，输入(lambda: 3)()，括号内不需要输入任何东西


"""lambda内还可以输入lambda"""
b = lambda x: lambda: x    #此时b是一个高维（二维）函数
#注意lambda: x，这个也是类似定义的f而非f(x)，因为lambda后面没有接任何东西
##对于b可以理解为，b = f(g())，b在第一维度定义到一个参数为x的函数，然后现在规定的这个参数x也是一个函数g,g()=x
c = b(88)  #这一层是一个函数，call了lambda x这个函数
c()    #这样会返回一个值

d = lambda f: f(4)
def square(x):
	return x * x
d(square)


z = 3
e = lambda x: lambda y: x + y + z
e(0)(1)()

f = lambda z: x + z
f(3)


higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g)    #这样的输出结果会报错，因为2是一个int，并不是一个函数，然后输入的g是一个函数，但应该为一个参数值
higher_order_lambda(g)(2)


call_thrice = lambda f: lambda x: f(f(f(x)))
call_thrice(lambda y: y + 1)(0)   #这里直接使用lambda函数来定义f


print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
print_lambda