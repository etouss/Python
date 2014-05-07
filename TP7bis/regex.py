#!/opt/local/bin/python

import re


def liste_dates(texte):
	reD1 = "\d{2}/\d{2}/\d{4}"
	reD2 = "\d{1,2}-\d{1,2}-\d{4}"
	reD3 = "\d{1,2} (?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|decembre) \d{4}"
	m=re.findall("("+reD3+")|("+reD2+")|("+reD1+")",texte)
	mReturn = [s1 for s in m for s1 in s if s1 != ""]
	return mReturn

def liste_dates_triplet(texte):
	reD1 = "(\d{2})/(\d{2})/(\d{4})"
	reD2 = "(\d{1,2})-(\d{1,2})-(\d{4})"
	reD3 = "(\d{1,2}) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|decembre) (\d{4})"
	m=re.findall("(?:"+reD3+")|(?:"+reD2+")|(?:"+reD1+")",texte)
	mReturn = [tuple([s1 for s1 in s if s1 != ""]) for s in m]
	return mReturn

def liste_dates_iter(texte):
	reD1 = "(\d{2})/(\d{2})/(\d{4})"
	reD2 = "(\d{1,2})-(\d{1,2})-(\d{4})"
	reD3 = "(\d{1,2}) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|decembre) (\d{4})"
	m=re.finditer("(?:"+reD3+")|(?:"+reD2+")|(?:"+reD1+")",texte)
	mReturn = [s.group(0) for s in m]
	return mReturn

def liste_dates_triplet_iter(texte):
	reD1 = "(\d{2})/(\d{2})/(\d{4})"
	reD2 = "(\d{1,2})-(\d{1,2})-(\d{4})"
	reD3 = "(\d{1,2}) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|decembre) (\d{4})"
	m=re.finditer("(?:"+reD3+")|(?:"+reD2+")|(?:"+reD1+")",texte)
	mReturn = [[s1 for s1 in s.group() if s1!= ""] for s in m]
	return mReturn


test = "coucou , 6 février 1978 , coucou 06/02/1978"
m=liste_dates_triplet_iter(test)
print(m)

