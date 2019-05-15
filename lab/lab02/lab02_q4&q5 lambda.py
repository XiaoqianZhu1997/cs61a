a = lambda x: x * 2 + 1   #a是一个lambda函数
def b(b, x):  #要注意这里换乱的表达，第一个b仅仅是函数名称，可以用其他的字母代替，而括号里面的b是变量名称，这这里是要使用函数
    return b(x + a(x))
x = 3
b(a, x)  #return到a(x + a(x))

""" x = 3,return到a(x)=2*3+1=7
然后b(a, x)就变成了a(10)，在进行lambda函数的一次运算，得到10*2+1=21"""

n = 9
def make_adder(n):
	return lambda k: k + n
add_ten = make_adder(n + 1)
result = add_ten(n)


