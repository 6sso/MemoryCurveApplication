
from Classes import *




#on commence avec un compteur du Nombre de Revision à 0
NbRevision = 0

#variables d'étape de révision : à chaque révision, on passe à la case d'après
# avec des coefficients d'oublis plus faibles
p=[30,20,10]
g=[3,2,1]

#cette fonctionalité permet de dynamiser le non d'une variable :
globals()[f"revision{NbRevision}"]=Revision(p[NbRevision], g[NbRevision])


#on apelle la fonction Ecrire qui va tracer la courbe en fonction des bons coefficients
Ecrire(globals()[f"revision{NbRevision}"])


