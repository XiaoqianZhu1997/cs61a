"""lambda funtion"""
x = 10
square = x * x  #evaluates to a number

square = lambda x: x * x    #evaluates to a function

(lambda x: x * x)("""自变量的值""")   #no ‘return’ word，限制must be a single expression


negate = lambda f, x: -f(x)   #negate是一个关于f和x的函数，需要两个输入
negate(lambda x: x * x, 3)   #这个时候的输入是lambda x和3，其中lambda x是函数square