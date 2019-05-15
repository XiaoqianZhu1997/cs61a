def wear_jacket(temp, raining):
	if temp < 60:
		return True
	elif raining == True:
		return True
	else:
		return False