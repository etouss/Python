i=0
list = []
while i<100:
	list.append(100*i)
	i=i+1
	

def addiTaunt(nb1,nb2):
	j=0
	t=0
	res = nb1 + nb2
	for j in list:
		if  res > j:
			print('Difficulté',t)
			break
		else :
			print(j)
		t=t+1

addiTaunt(10,10)
