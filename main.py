# -*- coding: utf-8 -*-

import pickle

from Classes import *

#h0 = 1696192419.772416 #Dimanche soir 01/10/2023

try:
    with open("BDD.pkl", "rb") as fichier2:
        Matieres = pickle.load(fichier2)

except EOFError:
    Matieres=[]

button=False
button=int(input("1 : AJOUTER UNE REVISION    0 : CONSULTATION DES COURBES"))

while button==1: #si on appuie sur le bouton, on run tout le code sous cette ligne

    TabTimeVide=[]

    if len(Matieres)!=0:
        N= int(input("Nouvelle matière ?      1 : OUI   0 : NON"))
    else :
        N=1

    if N :

        nom = input("Entrez le nom de la matière à mémoriser : ")

        globals()[f"{nom}"]=Revision(1, nom, TabTimeVide)
        h=datetime.datetime.now().timestamp()
        matiere=globals()[f"{nom}"]
        matiere.TabTime.append(h)
        Matieres.append(matiere)
        print(Matieres[-1].nom)


        with open('BDD.pkl', 'wb') as fichier2:
            pickle.dump(Matieres, fichier2)

    else :
        print("Voici vos matières : ")
        for i in range(len(Matieres)):
            print(i+1, Matieres[i].nom)

        Index=int(input("Entrez le numéro de la matière : "))
        matiere=Matieres[Index-1]

        h=datetime.datetime.now().timestamp()
        matiere.TabTime.append(h)
        matiere.numero += 1
        Matieres[Index-1]=matiere #Peut être pas obligé de mettre ca, à verifier
        with open('BDD.pkl', 'wb') as fichier2:
            pickle.dump(Matieres, fichier2)
        print(f"{matiere.nom} mis à jour")


    button=int(input("Une autre matière ?      1 : OUI   0 : NON"))


try:
    with open("BDD.pkl", "rb") as fichier2:
        MatieresMaj = pickle.load(fichier2)
        for i in range(len(MatieresMaj)):
            Ecrire(MatieresMaj[i],i)

except EOFError:
    print("Fichier vide")



