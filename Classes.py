


import matplotlib.pyplot as plt
import numpy as np
import datetime

class Revision():
    def __init__(self, num, h, h0, nom, TabTime):
        self.numero=num
        self.heurerevi=h
        self.heuredebut=h0
        self.nom=nom
        self.TabTime=TabTime

class Heure(): #pas utilisée
    def __init__(self, time):
        self.time=time


def SegmentTime(Revision):
    current_time = datetime.datetime.now().timestamp()

    return np.arange(Revision.heurerevi-Revision.heuredebut, current_time-Revision.heuredebut, 0.1)

def Ecrire(Revision):
    pente=[30,20,10,10,10,10]
    gain=[2,2,2,2,2]
    colors=['r','g','b', 'c', 'm', 'y', 'k', 'w']


    for i in range(len(Revision.TabTime)):
        f = np.exp(-Revision.TabTime[i]/pente[i]) + gain[i]
        plt.plot(Revision.TabTime[i], f, label=f"Courbe{i}", color=colors[i])


    plt.legend()

    plt.xlabel('t')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    axes.set_xlim(0, 1800) #on définit l'axe sur 30 minutes

    plt.ylabel('Oubli(t)')
    axes.set_ylim(0, 10)


    plt.title(f'Tracé de la fonction oubli pour la matière {Revision.nom}')

    plt.grid(False)
    plt.show()


