def commun (s1,s2):
	result = set(s1) & set(s2)
	return len(result)
	
def consonne(s):
	cons= 'aeiouy'
	return {x for x in s if x not in cons}
	