
from Classes import *

#on commence avec un compteur du Nombre de Revision à 0
NbRevision = 0
h0 = 1696192419.772416 #Dimanche soir 01/10/2023
h=h0 #à modifier

#variables d'étape de révision : à chaque révision, on passe à la case d'après
# avec des coefficients d'oublis plus faibles
p=[30,20,10]
g=[2,3,4]


button=False
if button==True: #si on appuie sur le bouton, on run tout le code sous cette ligne
    NbRevision +=1
    h=datetime.datetime.now().timestamp()

francais=Revision(p[NbRevision], g[NbRevision], NbRevision,h, h0 )


TableauTime=[]
TableauTime.append(SegmentTime(francais))

#on apelle la fonction Ecrire qui va tracer la courbe en fonction des bons coefficients
Ecrire(francais, TableauTime)
