def IndiceMin(T,i):
    if i<0 or i>len(T)-1:
        return -1
    indice = i;
    min = T[i];  
    result = i
    for indice in range(i,len(T)):
        if T[indice] < min:
            min = T[indice]
            result = indice
    return result

def TriSelection(T):
    i=0
    for i in range(0,len(T)):
        indiceMin = IndiceMin(T,i)
        T[i],T[indiceMin] = T[indiceMin],T[i]
        