# Clock.py
"""Créer une horloge à cadran.
"""

# Importer Tkinter
from tkinter import *
from math import pi, cos, sin
import time

# Création d'une fenêtre, racine de l'interface
fenetre = Tk()
fenetre.title('Horloge à cadran')

# Création d'une zone de dessin (un canvas) contenant l'affichage de l'heure
clock = Canvas(fenetre, width=100, height=100, background='white')

# Création du cadran puis des aiguilles

# Centre
cx=50
cy=50
# Rayon
r=40

# Longueur des aiguilles
hl = 15
ml = 30
sl = 35

# Angle des aiguilles avec midi en fraction
ha = 1/12 # 1h
ma = 0/60 # 0min
sa = 30/60 # 30s

# Fonction calculant abscisse et ordonnée de l'extremite d'une aiguille
def extremite(l,a):
    return (cx+ l*cos(pi/2.0-a*(2.0*pi)), cy-l*sin(pi/2.0-a*(2.0*pi)))

# Dessin des elements de l'horloge
cadran = clock.create_oval(cx-r,cy-r,cx+r,cy+r)
hx,hy = extremite(hl,ha)
hd = clock.create_line(cx,cy,hx,hy, width=2)
mx,my=extremite(ml,ma)
md =  clock.create_line(cx,cy,mx,my)
sx,sy=extremite(sl,sa)
sd =  clock.create_line(cx,cy,sx,sy,fill='red')

# Fonction de mise à jour des aiguilles
def up_aig(aig,l,a):
    ex,ey = extremite(l,a)
    clock.coords(aig, cx,cy,ex,ey)
    clock.update()

# Création d'une fonction de mise à jour de l'heure
def update():
    ''' afficher l'heure courante '''
    ############ A COMPLETER #####################################
    # Avec module time, recuperer heure, minute, seconde actuelles
    seconde = time.strftime("%S",time.localtime())
    minute = time.strftime("%M",time.localtime())
    heure = time.strftime("%H",time.localtime())
    	
		

    # Updater les dessin des aiguilles
    up_aig(sd, sl, int(seconde)/60) # secondes
    up_aig(md, ml, int(minute)/60) # minutes
    up_aig(hd, hl, int(heure)/12) # heures
    ##############################################################
    # Commande qui rappelle la fonction update après 200ms
    time.sleep(0.2)
    clock.after(200,update)

# Création d'un bouton pour demarrer l'horloge
demarre = Button(fenetre, text="demarrer", command=update)
# Création d'un bouton pour quitter l'horloge
quitte = Button(fenetre, text="quitter", command=fenetre.destroy)

# Affichage du label et des boutons dans la fenêtre
clock.grid(row=0, column=0, columnspan=2)
demarre.grid(row=1, column=0)
quitte.grid(row=1, column=1)

# Démarrage de la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
