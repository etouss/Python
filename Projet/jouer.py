import os
from tkinter import *
from Arbre import *

#Classe héritant, de Frame affichant les niveaux disponible

class Jouer(Frame):
	def __init__(self,tk):
		Frame.__init__(self,tk)
		self.tk = tk
		list = os.listdir("Niveaux/")																						#Parcours le contenu du dossier Niveaux et récupere tout les fichier contenant arbre.
		self.niveaux = [file for file in list if "arbre" in file]
		self.nombre = len(self.niveaux)
		self.pack(side=LEFT,fill="both")
		for x in range(0,self.nombre):
			Button(self, text=str(x), command=lambda x=x:self.jouerNiveaux(x)).grid(row=x//3, column=x%3, sticky=W+N+E+S)		#Creer un bouton pour chaques niveaux disponible
		self.mainloop()

	def jouerNiveaux(self,t):																								#Lance le niveau demandé
		self.destroy()
		main("Niveaux/"+str(t+1)+"arbre.txt",self.tk)

def main(fichier,tk):																										#Initialise un mobile depuis un Arbre contenu dans le fichier
	tableau = importer(fichier)
	arbre=Arbre(tk)
	arbre.initialisation(tableau)
	#arbre.sommet.droit.o = 0.3
	coolDyna(arbre)

def coolDyna(arbre):
	while arbre.sommet.poidsVar != 0:																						#Fonction assurant la pérénité de l'affichage tant que les poids ne sont pas tous nuls.
		arbre.update()

def importer(fichier):
    #Convertissons tableau en tableau
    return eval(open(fichier,"r").readline()) 