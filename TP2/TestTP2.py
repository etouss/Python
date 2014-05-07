''' 
TestTP2.py

Ce fichier contient quelques réponses erronées du tp2. 

Vous devez le compléter pour les tester et les corriger.
'''

# Ici, on importe les modules:

from my_test import # Compléter par les fonctions a importer

# Ici, on definit les fonctions:


def suffixe(p):
    (s,n) = p
    if len(s) >= n:
       return s[-n:]
    else:
       return False


def double(l):
  for i in l:
    t.append(i)
    return l 

# Ici, on test les fonctions lorsque le fichier n'est pas importé
if __name__ == "__main__":
   S = [( ('', 0) , ''), ( ('suffixe', 3) , 'ixe' ) , ( ('a', 0) , '') , (('a', 3) , 'False' ) ]
   #IOtest(suffixe, S)

   T = [[], [1,2,3], [0,0]]
   #Itest(double, T)

   U = [([], []), ([1,2,3], [1,2,3]), ([0,0], [0,0,0,0])]
   #IOtest(double , U)

