"""Q1"""
from operator import add
six = 1

def ty(one, a):
	fall = one(a, six) 
	return fall
    
six = ty(add, 6)
fall = ty(add, 6)



"""Q2"""
def curry2(h): 
	def f(x):
		def g(y):
			return h(x, y)
		return g 
	return f

make_adder = curry2(lambda x, y: x + y) 
add_three = make_adder(3)
five = add_three(2)
    


"""Q3"""
n=7
def f(x): 
	n=8
	return x + 1

def g(x): 
	n=9
	def h():
		return x + 1
	return h 

def f(f, x):
	return f(x + n)
f = f(g, n)   #此处相当于f(g, n)=g(n+n)=g(14)=h，return到了一个函数
g = (lambda y: y())(f)   #此时lambda函数的意思是，这个定义的函数形式是y()，此时的就是求f()，而f()此时即h()=14 + 1 = 15




"""Q4"""
y = "y" 
h=y   #则h=y="y"
def y(y):
	h = "h"  #此时h="h"不等于"y"
	if y == h:  
		return y + "i"
	y = lambda y:  (h) #lambda f: f(h)
	return lambda h: y(h)
y = y(y)(y)  #此时y是一个函数：y(y)(),return 到y(y)
#而后，因为y != h，所以函数y()变更为lambda y，return lambda h，但lambda h其实就是y(y)
##lambda y也是y(y)