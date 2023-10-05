
from Classes import *


#h0 = 1696192419.772416 #Dimanche soir 01/10/2023
h0=datetime.datetime.now().timestamp()

Matieres=[]

button=False
button=bool(input("On appui sur le bouton ? Ou vous souhaitez juste consulter vos courbes "))

while button==True: #si on appuie sur le bouton, on run tout le code sous cette ligne
    print("bouton appuyé !")




    TabTimeVide=[]


    N= int(input("Nouvelle matière ? 1OUI/0NON"))

    if N :

        nom = input("Entrez le nom de la matière à mémoriser : ")

        globals()[f"{nom}"]=Revision(1,h0, h0, nom, TabTimeVide)
        Matieres.append(globals()[f"{nom}"])
        print(Matieres[0].nom)
        matiere=globals()[f"{nom}"]
        matiere.TabTime.append(h)
    else :
        print("Voici vos matières, choisissez en entrant le numéro : ")
        for i in range(len(Matieres)):
            print(i+1, Matieres[i].nom)

        Index=int(input("Entrez le numéro de la matière : "))
        matiere=Matieres[Index-1]

        h=datetime.datetime.now().timestamp()
        matiere.heurerevi=h#1
        matiere.num+=1 #1
        matiere.TabTime.append(h) #2

    1FICHIER ECRIRE (matiere.nom, matiere.heurerevi, matiere.num)
    2FICHIER ECRIRE (matiere.nom , matiere.TabTime )







    #On apelle la fonction Ecrire qui va tracer la courbe en fonction des bons coefficients
    Ecrire(matiere)

    button=bool(input("Une autre matière ? "))

for i in range(NOMBRE DE 1 dans la colonne num du FICHIER)
    Ecrire(FICHIER.nom, .heurerevi , .num)
