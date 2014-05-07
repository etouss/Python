import grandes_lettres

def grand_message(s):
	res =''
	for i in range(0,5) :
		for c in s :
			res += grandes_lettres.grandes_lettres[c][i]
		res += '\n'
	print(res)
	