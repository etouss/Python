def Fusion(T,bg,m,bd):
    i = bg
    while m<bd and i<m:
        if T[i]<T[m]:
            i = i+1
        if T[i]>T[m]:
            temp = T[m]
            for k in range(i,m-2):
                T[k+2] = T[k+1]
                T[k+1] = T[k]   
            T[i] = temp
            m = m+1
            i = i+1
        
        