


import matplotlib.pyplot as plt
import numpy as np

class Revision():
    def __init__(self):
        self.coeffp=p
        self.gaing=g



def Ecrire(Revision):
    t = np.arange(0., 10., 0.1)
    F_t = np.exp(-t/Revision.coeffp)+Revision.gaing

    plt.plot(t, F_t, label="Oubli(t) = e^-t/P + G")

    plt.legend()

    plt.xlabel('t')
    plt.ylabel('Oubli(t)')

    plt.title('Tracé de la fonction oubli')

    plt.grid(True)
    plt.show()






