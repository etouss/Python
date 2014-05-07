#! #Mettre ici l'interpréteur à utiliser

# Documentation
'''Module sans.py. 
   La ligne de commande:
	  ./sans.py -c 'e' s 
   imprime la chaine de caracteres s sans le caractere e
   La ligne de commande 
	  ./sans.py -h
   imprime une phrase d'aide 
'''

# Ici, on importe les modules:

import sys

# Ici, on definit les fonctions:

def sans(c,s): 
  ''' Renvoie la chaine de caractere s sans les occurences de c'''
  pass 

def main(argv): #argv est la liste des arguments passes au script
  """ teste l'option passee en argument du script et 
  retourne la chaine  de caractere a imprimer"""
  pass

def main_expt(argv):
  """ teste l'option passee en argument du script et 
      retourne la chaine  de caractere a imprimer
      leve une exception quand il n'y a pas assez d'arguments"""
  try: # On essaie de recuperer les arguments passes au script
    pass 
  except IndexError:
    # S il n y a pas assez d argument, on imprime le message d erreur:
    # "pas assez d'argument, utiliser l'aide: ./sans_.py -h"
    sys.exit(2)

# Ici, on ecrit la partie interactive du script
if __name__ == "__main__":
  print(sys.argv[1:]) # Modifier cette ligne pour afficher la chaine argument sans e
    
