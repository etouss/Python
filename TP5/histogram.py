
import tkinter
import time

fenetre=tkinter.Tk()
canvas = tkinter.Canvas(fenetre,width=400,height=400,background="white")
canvas.pack()

def updateTableau(T):
    canvas.delete("all")
    for i in range(0,len(T)):
        canvas.create_rectangle(i*20,400,20*(i+1),400-(10*T[i]))
    canvas.update()

def afficherTriTableauInsert(T):
    i=0
    for i in range(0,len(T)) :
        Inserer(T,i)
        updateTableau(T)
        time.sleep(1)
        
def afficherTriTableauFusion(T):
    i=0
    for i in range(0,len(T)) :
        Inserer(T,i)
        updateTableau(T)
        time.sleep(1)        
        
                
    
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
        
def fusion(T,bg,m,bd):
    res=[]
    i,j=bg,m
    while i<=m-1 and j<=bd:
        if T[i]<T[j]:
            res.append(T[i])
            i=i+1
        else:
            res.append(T[j])
            j=j+1
        print(res)
    if i==m:
        res.extend(T[j:bd+1])
    else:
        res.extend(T[i:m])
    print(res)
    for i in range(bg,bd+1):
        T[i]=res[i-bg]
        
def TriFusion(T,bg=0,bd=None): 
    if bd == None:
        bd=len(T)-1
    if bg!=bd:
        if bg+1 == bd:
            if T[bg]>T[bd]:
                T[bg],T[bd]=T[bd],T[bg]
        else:
            m=(bg+bd)//2
            TriFusion(T,bg,m)
            TriFusion(T,m+1,bd)
            fusion(T,bg,m+1,bd)
	    print(test)


     	  
        
 
