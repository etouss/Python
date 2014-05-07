train = { "Paris": ["Lyon","Marseille","Bordeaux","Nantes","Toulouse","Lille","Nancy"],
    "Lyon": ["Marseille","Nancy","Paris"],
    "Marseille": ["Toulouse","Lyon","Paris"],
    "Bordeaux": ["Nantes","Toulouse"] ,
    "Nantes": ["Paris"],
    "Toulouse": ["Marseille", "Bordeaux"],
    "Lille": ["Paris","Nancy"],
    "Nancy": ["Lille","Lyon"]
}

def voyage(s1,s2):
	return [[s1,x,s2] for x in train[s1] if s2 in train[x]]
