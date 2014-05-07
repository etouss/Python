from tkinter import *
from tkinter.filedialog import *
from Arbre import *
from Algo import*
import menu

#Classe héritant de Frame affichant les option liéer au projet:
#Ouverture d'un arbre.
#Ouverture d'une liste de poids et génération d'un arbre a partir d'un algorithme au choix.

class Projet(Frame):
	def __init__(self,tk):
		Frame.__init__(self,tk)
		self.tk = tk
		self.algo = StringVar()
		self.algo.set("AlgoMinImmediat")																										#AlgoMinImmediat par défault
		self.pack(side=LEFT,fill="both")																										
		self.bouton_arbre = Button(self, text="Ouvrir fichier Arbre", fg="white", bg="#7F7F7F",
			highlightbackground='#303030', highlightthickness=3,																				#Bouton permetant d'ouvrir un fichier Arbre
                                   command=self.openfile_Arbre) 

		self.bouton_arbre.grid(row=0, column=0, sticky=W+N+E+S)

		self.bouton_liste = Button(self, text="Ouvrir fichier Liste", fg="white", bg="#7F7F7F",
			highlightbackground='#303030', highlightthickness=3,																				#Bouton permetant d'ouvrir un fichier Liste
			command=self.openfile_Liste)
		self.listeMethode = OptionMenu(self, self.algo, *{"AlgoMinImmediat","AlgoMinFutur","AlgoMax","AlgoEsthet","AlgoEsthetParfait"})			#Liste déroulante permantant le choix de l'algo à utiliser
		self.listeMethode.grid(row=2, column=0, sticky=W+N+E+S)
		self.bouton_liste.grid(row=1,  column=0, sticky=W+N+E+S)


		self.bouton_retour = Button(self, text="Retour", fg="white", bg="#7F7F7F",
			highlightbackground='#303030', highlightthickness=3,																				#Bouton permetant le retour au menu
			command=self.retour)
		self.bouton_retour.grid(row=3,  column=0, sticky=W+N+E+S)
		self.bouton_arbre.config(height=5,width=20)
		self.bouton_liste.config(height=5,width=20)
		self.bouton_retour.config(height=5,width=20)

	def openfile_Arbre(self):
		self.filename = askopenfilename(parent=self)  # boite de dialogue																		#Appelle systeme pour trouver le chemin du fichier
		try:
			open(self.filename)
		except IOError:
			return
		for child in self.tk.winfo_children():																									#Detruit toutes les Frame de la fênetre
			child.destroy()
		main(self.filename,self.tk)

	def openfile_Liste(self):
		self.filename = askopenfilename(parent=self)  # boite de dialogue
		try:
			open(self.filename)
		except IOError:
			return
		for child in self.tk.winfo_children():
			child.destroy()
		if self.algo.get() == "AlgoMinImmediat":
			creer(self.filename,0,self.tk)																										#Appelle la fonction creer sur une liste avec un argument dépendant de l'algo utilisé
		elif self.algo.get() == "AlgoMinFutur":
			creer(self.filename,2,self.tk)
		elif self.algo.get() == "AlgoMax":
			creer(self.filename,1,self.tk)
		elif self.algo.get() == "AlgoEsthet":
			creer(self.filename,3,self.tk)
		elif self.algo.get() == "AlgoEsthetParfait":
			creer(self.filename,4,self.tk)
		else:
			pass

	def retour(self):
		for child in self.tk.winfo_children():
			child.destroy()
		menu.Menu(self.tk)



def creer(fichier,type,tk):
    algo = Algo()
    f = algo.run(fichier,type)																													#Creer une instance de Algo, et l'utilise pour creer un arbre avec l'algo demander.
    main(f,tk)

def main(fichier,tk):
    tableau = importer(fichier)
    arbre=Arbre(tk)																																#Initialise un mobile depuis un Arbre contenu dans le fichier
    arbre.initialisation(tableau)
    #arbre.sommet.droit.o = 0.3
    coolDyna(arbre)
    
def importer(fichier):
    #Convertissons tableau en tableau
    return eval(open(fichier,"r").readline()) 
     
def coolDyna(arbre):
    while arbre.sommet.poidsVar != 0:																											#Fonction assurant la pérénité de l'affichage tant que les poids ne sont pas tous nuls.
        arbre.update()