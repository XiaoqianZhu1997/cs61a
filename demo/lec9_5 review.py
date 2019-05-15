def delay(arg):
	print('delayed')
	def g():
		return arg
	return g

delay(delay)()(6)()
print(delay(print)()(4)) 



def pirate(arggg):
	print('matey')
	def plunder(arggg):
		return arggg
	return plunder 
add(pirate(3)(square)(4), 1)
pirate(pirate(pirate))(5)(7)  


"""⚠️"""
def horse(mask):
	horse = mask   # 函数相等
	def mask(horse):   # identity function
		return horse
	return horse(mask)

mask = lambda horse: horse(2)
horse(mask)


"""
对于lambda的frame是global，也就是说，这里面的horse 对应global的horse
在global里horse对应mask，从而horse(2)变成了mask(2)，mask此处是一个identity function
"""