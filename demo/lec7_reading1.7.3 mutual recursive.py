"""Alice always removes a single pebble
Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
Given n initial pebbles and Alice starting, who wins the game?"""

"""函数意思可能是谁拿走最后一个pebble，谁赢"""
def play_alice(n):  #函数表示，轮到alice的时候还有多少棋子
	if n == 0:   #轮到alice的时候没有棋子了，说明alice赢了
		print('alice wins')
	return play_bob(n - 1)

def play_bob(n):
	if n == 0:
		print('bob wins')
	elif n % 2 == 0:
		return play_alice(n - 2)
	else:
		return play_alice(n - 1)
