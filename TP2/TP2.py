def suffixe(s,n):
	return s[n:len(s)]

def prefixe(s,n):
	return s[0:n]
	
def miroir(s):
	res = ''
	for i in range(0,len(s)):
		res = res + s[len(s)-1-i]
	return res
	
def palindrome(s):
	test = miroir(s)
	return test == s

def centre(s):
	if len(s)%2 == 0:
		return s[len(s)/2-1:(len(s)/2)+1]
	else:
		return s[len(s)/2]
		
def paire(s):
	res = ''
	for i in range(0,len(s),2):
		res = res + s[i]
	return res

def sans_e(s):
	res = ''
	temp = 0 
	for i,c in enumerate(s):
		if c == 'e':
			res = res + s[temp:i]
			temp = i+1
	res = res + s[temp:len(s)]
	return res
	
def compte_espace(s):
	res = 0
	for i,c in enumerate(s):
		if c == ' ':
			res = res+1
	return res
	
def sans_espace(s):
	res = ''
	temp = 0 
	for i,c in enumerate(s):
		if c == ' ':
			res = res + s[temp:i]
			temp = i+1
	res = res + s[temp:len(s)]
	return res
	
def palindrome_espace_espace(s):
	res = sans_espace(s)
	return palindrome(res)
	
def somme(t):
	res = 0
	for i in range(0,len(t)):
		res = res + t[i]
	return res
		
		
		
			
