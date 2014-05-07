def IndiceMin(T,i):
    if i<0 or i>len(T)-1:
        return -1
    indice = i;
    min = T[i];  
    for indice in range(i,len(T)):
        if T[i] < min:
            min = T[i]
            indice = i
    return i;
            
            
    