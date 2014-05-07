def consonnes(s):
	cons= 'aeiouy'
	return {x for x in s if x not in cons}