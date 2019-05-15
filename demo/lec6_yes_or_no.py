def get_answer(prompt):
	while True:   
		"""与下面的code相比，优点在于more concise，因为对于answer只进行了一次赋值"""
		answer = input(prompt).strip().lower()   #r如果只写到这里，就会进行无限循环，无论输入的是什么
		"""strip()是使得消除空格的影响，lower()是消除大写的影响"""
		if answer in ('yes', 'no'):   #设定条件去break the loop
			return answer    #上述条件满足的时候，就打破了循环，输出这个值


def get_answer_oringinal(prompt):
	answer = input(prompt)
	while answer not in ("yes", "no"):
		answer = input(prompt)
	return answer

print(get_answer("yes or no? "))