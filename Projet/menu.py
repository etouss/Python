from tkinter import *
from projet import*
from jouer import *
import sys

#Classe héritant, de Frame affichant le Menu.

class Menu(Frame):
	def __init__(self,tk):
		Frame.__init__(self,tk)
		self.tk = tk
		self.pack(fill="y")
		self.canvas = Canvas(self,width=400,height=400,background="white")				#Canvas Principal
		self.projet = Button(self.canvas, text="Projet", command=self.projetClick)		#Bouton provoquant l'affichage du menu Projet.
		self.jouer = Button(self.canvas, text="Jouer", command=self.jouerClick)			#Bouton provoquant l'affichage des différents niveaux
		self.quitter = Button(self.canvas, text="Quitter", command=self.quitterClick)	#Bouton provoquant l'arrêt du logiciel.
		self.projet.grid(row=0, column=0, sticky=W+N+E+S)								
		self.jouer.grid(row=1, column=0, sticky=W+N+E+S)
		self.quitter.grid(row=2, column=0, sticky=W+N+E+S)
		self.canvas.pack()																#On fait le choix d'un affichage en grid.
		self.projet.config(height=10,width=10)
		self.jouer.config(height=10,width=10)
		self.quitter.config(height=10,width=10)
		self.mainloop()
     
	def projetClick(self):
		self.destroy()																	#On détruit le menu.
		projet = Projet(self.tk)														#On creer le menu Projet.
	def jouerClick(self):
		self.destroy()																	#On détruit le menu.
		jouer = Jouer(self.tk)															#On creer la frame Jouer, les niveaux.												
	def quitterClick(self):																
		sys.exit(0)																		#Quitte le programme.
