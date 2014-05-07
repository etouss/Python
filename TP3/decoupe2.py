def decoupe2(s):
	res =''
	result = []
	for x in s :
		if x not in ' .,;:?!-()':
			res += x
		else :
			result.append(res)
			res = ''
	result.append(res)
	return result