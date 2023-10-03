


import matplotlib.pyplot as plt
import numpy as np
import datetime

class Revision():
    def __init__(self, p, g, num, h, h0):
        self.coeffp=p
        self.gaing=g
        self.numero=num
        self.heurerevi=h
        self.heuredebut=h0



def SegmentTime(Revision):
    current_time = datetime.datetime.now().timestamp()

    return np.arange(Revision.heurerevi-Revision.heuredebut, current_time-Revision.heuredebut, 0.1)

def Ecrire(Revision, Tab):#ici Revision est inutile
    pente=[30,20,10]
    gain=[2,3,4]
    colors=['r','g','b', 'c', 'm', 'y', 'k', 'w']
    for i in range(len(Tab)):
        f = np.exp(-Tab[i]/pente[i]) + gain[i]
        plt.plot(Tab[i], f, label=f"Courbe{i}", color=colors[i])


    plt.legend()

    plt.xlabel('t')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    axes.set_xlim(0, 24*7*3600) #on définit l'axe sur 1 jour

    plt.ylabel('Oubli(t)')
    axes.set_ylim(0, 10)


    plt.title('Tracé de la fonction oubli')

    plt.grid(True)
    plt.show()


