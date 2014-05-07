import math
import os

class Algo:
    def __init__(self):
        pass

    def importer(self,fichier):
        #Convertissons les poids en tableau
        return [int(i) for i in open(fichier,"r").readlines()]
    
    def creer(self,fichier,arbre):
        f = open(fichier,"w")
        f.write(arbre)
    
    #renvoie l'indice du minimum de la liste.
    def indiceMini(self,list):
        i = 0
        min = list[0]
        for j,k in enumerate(list):
            if k < min:
                min=k
                i = j
        return i
    
    #insert un à sa place dans une liste trié.
    def insertTri(self,list,somme):
        i=0
        for j,k in enumerate(list):
            if k < somme:
                i = j
            else: 
                break
        list.insert(i+1,somme)
        return list

    
    #algorithme récursif associant les deux valeur les plus proche ensemble et insérant leur somme dans le reste de la liste.
    def algoMinImmediat(self,list):
        if len(list) > 2:
            listDiff = [list[i+1] - list[i] for i in range(0,len(list)-1)]
            i = self.indiceMini(listDiff)
            somme = list[i] + list[i+1]
            newList = [k for j,k in enumerate(list) if j != i and j-1 != i]
            newList = self.insertTri(newList,somme)
            arbre = self.algoMinImmediat(newList)
            arbre = arbre.replace(str(somme),str([list[i],list[i+1]]),1)
            return arbre
        else : 
            return str(list)

    #algorithme récursif associant les deux valeur les plus disemblable ensemble et insérant leur somme dans le reste de la liste.
    def algoMax(self,list):
        if len(list) > 2:
            somme = list[len(list)-1] + list[0]
            newList = list[1:-1]
            newList.append(somme)
            arbre = self.algoMax(newList)
            arbre = arbre.replace(str(somme),str([list[0],list[len(list)-1]]),1)
            return arbre
        elif len(list) == 2:
            return str(list)
        else :
            return str(list[0])
            
    #algorithme récursif associant les deux plus petit élement ensemble et insérant leur somme dans le reste de la liste.
    def algoMinFutur(self,list):
        if len(list) > 2:
            somme = list[0]+list[1]
            newList = list[2::]
            newList = self.insertTri(newList,somme)
            arbre = self.algoMinFutur(newList)
            arbre = arbre.replace(str(somme),str([list[0],list[1]]),1)
            return arbre
        elif len(list) == 2:
            return str(list)
        else :
            return str(list[0])

    #Tente de creer un mobile joli en faisant un arbre binaire parfait a droite et le reste a gauche.
    def algoEsthet(self,list):
        if len(list) > 2:
            h = int(math.log(len(list),2))
            n = 2**h
            if 2**h == len(list):
                n = 2**(h-1)
            arbre = '['+self.algoEsthet(list[:n])+','+self.algoEsthet(list[n:])+']'
            return arbre
        elif len(list) == 2:
            return str(list)
        else :
            return str(list[0])

    #Tente de creer un mobile joli en faisant un arbre binaire parfait et ajoutant sur les étiquette les plus basse les élément restant.
    def algoEsthetParfait(self,list):
        if len(list) > 2:
            h = int(math.log(len(list),2))
            reste = len(list)-2**h
            if(reste > 2**h-1):
                list1 = list[:2*h]
                list2 = list[2*h:]
            else :
                list1 = list[:2*(h-1)+reste]
                list2 = list[2*(h-1)+reste:]
            arbre = '['+self.algoEsthet(list1)+','+self.algoEsthet(list2)+']'
            return arbre
        elif len(list) == 2:
            return str(list)
        else :
            return str(list[0])
            
    #Fonction créant le fichier arbre associer a la liste avec l'algorithme demander.
    def run(self,fichier,type):
        list = self.importer(fichier)
        list.sort()
        if type == 0:
            arbre = self.algoMinImmediat(list)
        elif type == 1:
            arbre = self.algoMax(list)
        elif type == 2:
            arbre = self.algoMinFutur(list)
        elif type == 3:
            arbre = self.algoEsthet(list)
        elif type == 4:
            arbre = self.algoEsthetParfait(list)
        list = os.listdir("Niveaux/")
        nb = len([file for file in list if "arbre" in file])
        self.creer("Niveaux/"+str(nb+1)+"arbre.txt",arbre)
        return "Niveaux/"+str(nb+1)+"arbre.txt"
    
    

