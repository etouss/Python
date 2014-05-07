def IndiceMin(T,i):
    if i<0 or i>len(T)-1:
        return -1
    indice = i;
    min = T[i];  
    result = i
    for indice in range(i,len(T)):
        if T[indice] < min:
            min = T[i]
            result = indice
    return result
            
            
    