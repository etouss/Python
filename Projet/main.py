#!/opt/local/bin/python
#coding: utf8
from menu import*

#Fichier servant simplement au demarage du programme:
#-Création du Tk()
#-Demande d'affichage du Menu.

tk = Tk()

def menuAfficher():
    menu = Menu(tk)															#Creer la frame Menu.

menuAfficher()
