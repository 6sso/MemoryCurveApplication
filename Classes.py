


import matplotlib.pyplot as plt
import numpy as np
import datetime

class Revision():
    def __init__(self, num, nom, TabTime):
        self.numero=num
        self.nom=nom
        self.TabTime=TabTime

class Heure(): #pas utilisée
    def __init__(self, time):
        self.time=time




def SegmentTime(Revision): #ne sert plus à rien
    current_time = datetime.datetime.now().timestamp()

    return np.arange(Revision.heurerevi-Revision.heuredebut, current_time-Revision.heuredebut, 0.1)

def Ecrire(Matiere):
    pente=[30,20,10,10,10,10]
    gain=[2,2,2,2,2]
    colors=['r','g','b', 'c', 'm', 'y', 'k', 'w']

    current_time = datetime.datetime.now().timestamp()

    for i in range(len(Matiere.TabTime)):
        t = np.arange(Matiere.TabTime[i]-Matiere.TabTime[0], current_time-Matiere.TabTime[0], 0.1)
        f = np.exp(-t/pente[i]) + gain[i]
        plt.plot(t, f, label=f"Courbe{i}", color=colors[i])


    plt.legend()

    plt.xlabel('t')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    axes.set_xlim(0, 1800) #on définit l'axe sur 30 minutes

    plt.ylabel('Oubli(t)')
    axes.set_ylim(0, 10)


    plt.title(f'Tracé de la fonction oubli pour la matière {Matiere.nom}')

    plt.grid(False)
    plt.show()


