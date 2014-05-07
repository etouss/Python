def swap(tab,i,j) :
    tab[i],tab[j]=tab[j],tab[i]

def TriSelection (tab) :
    for i in range(0,len(tab)):
        swap(tab,IndiceMin(tab,i),i)
        
def Inserer(tab,i) :
    for x in range(0,i):
        if tab[x]>tab[i] : 
            swap(tab,i,x)

def TriInsertion(tab) :
    for i in range(0,len(tab)-1) :
        Inserer(tab,i)