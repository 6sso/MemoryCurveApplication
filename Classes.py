


import matplotlib.pyplot as plt
import numpy as np
import datetime

class Revision():
    def __init__(self, p, g):
        self.coeffp=p
        self.gaing=g




def Ecrire(Revision):
    start_time = 1696192419.772416 #Dimanche soir 01/10/2023
    current_time = datetime.datetime.now().timestamp()

    t = np.arange(0., current_time-start_time, 0.1)
    #t = np.arange(0., 1000000, 0.1)
    F_t = np.exp(-t/Revision.coeffp)+Revision.gaing

    plt.plot(t, F_t, label="Oubli(t) = e^-t/P + G")



    plt.legend()

    plt.xlabel('t')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    axes.set_xlim(0, 3600) #on définit l'axe sur 1 jour

    plt.ylabel('Oubli(t)')
    axes.set_ylim(3, 4)


    plt.title('Tracé de la fonction oubli')

    plt.grid(True)
    plt.show()







