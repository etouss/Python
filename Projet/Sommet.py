from Configuration import *
from tkinter import *
import math

score = 0
tempsUnitaire = 0.03        #initialisateur du temps a 33 FPS
p = tempsUnitaire*k         

def setTempsUnitaire(a):
    global tempsUnitaire 
    tempsUnitaire = a
    global p 
    p = tempsUnitaire*k

def getTempsUnitaire():
    return tempsUnitaire
    
def getScore():
    return score

def setScore(i):
    global score
    score = i
    

class Sommet:
    def __init__(self):

        # La classe sommet est construite comme un arbre binaire dont l'étiquette est le poids.
        # Des attribut liée au dynamisme des boules ont était ajouté.
        self.gauche = None
        self.droit = None
        self.barycentre = None
        self.poids = None
        self.poidsVar = None
        self.longueur = None
        self.erro = False
        self.button = None
        self.tagListen = None
        
        self.x = 0
        self.y = None
        self.dodt=0
        self.o = 0

        self.color= None
        self.redOn = False
        self.clignotant=0;
    
        #Fonction calculant l'accéleration du sommet considérant par application du principe fondamental de la dynamique. 
    def accelerationO(self):
        if self.gauche.poidsVar != 0 or self.droit.poidsVar != 0:
            return ((math.cos(self.o)*g*pixelTometre/(self.poidsVar*self.longueur))*((self.gauche.poidsVar*self.barycentre)-(self.droit.poidsVar*(1-self.barycentre))))-f*self.dodt
        else :
            return -f*self.dodt
        
        #Fonction calculant la vitesse par multiplication de l'acceleration par le temps unitaire   
    def vitesseO(self):
        self.dodt += self.accelerationO()*tempsUnitaire
        
        #Fonction calculant la position par multiplication de la vitesse par le temps unitaire 
    def positionO(self):
        self.o += self.dodt*tempsUnitaire
        global score
        score += abs(self.dodt*tempsUnitaire)
        
        #Fonction de mis a jour des attributs du sommet, elle est appelé tout les temps unitaire.
    def maj(self):
        self.gauche.errosion()                                                          #met a jour poid gauche.
        self.droit.errosion()                                                           #met a jour poid droit
        self.poidsVar = self.droit.poidsVar+self.gauche.poidsVar                        #calcul son propre poid.
        self.vitesseO()                                                                 
        self.positionO()
        self.gauche.x = self.x-self.longueur*self.barycentre*math.cos(self.o)
        self.gauche.y = self.longueur*self.barycentre*math.sin(self.o)+(self.y+h)
        self.droit.x =  self.x+self.longueur*(1-self.barycentre)*math.cos(self.o)
        self.droit.y =  self.longueur*(1-self.barycentre)*math.sin(-self.o)+(self.y+h)
    
        #Parcours sufix du mobile pour mettre a jour les différents sommet en commencant par le plus profond. 
    def majAll(self):
        if self.gauche.barycentre != None:
            self.gauche.majAll()
        if self.droit.barycentre != None:
            self.droit.majAll()
        self.maj()
    
        #Fonction supprimer un poid unitaire a une boule.
    def errosion(self):
        if  self.erro:
            self.button["text"]= str(self.poidsVar)[:3]
            self.poidsVar = max(0,self.poidsVar -p)
    
        #Fonction définisant si une érosion est active ou non
    def erroClick(self,event=None):
        if self.erro:
            self.erro = False
        else:
            self.erro = True
            self.button.configure(fg="red")
            
    def calculLongueur(self,lo):
        self.longueur = ((-1/4)*self.barycentre+1/2)*lo
