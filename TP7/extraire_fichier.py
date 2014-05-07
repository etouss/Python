import re

def extraire_ligne(s):
    m = re.match("(.*),(.*),(.*),(.*)",s)
    return (m.group(1),m.group(4))

def extraire_fichier(fichier):
    result = dict()
    f = open(fichier,"r")
    ligne = f.readline()
    while ligne != None and ligne!='':
        entre = extraire_ligne(ligne)
        if entre in result:
            result[entre] = result[entre]+1
        else:
            result[entre]=1
        ligne = f.readline()
    return result

def extraire_prenoms(d):
    return [key[0] for key in d.keys() if d[key] == 1]
    