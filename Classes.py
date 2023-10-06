


import matplotlib.pyplot as plt
import numpy as np
import datetime

class Revision():
    def __init__(self, num, nom, TabTime):
        self.numero=num
        self.nom=nom
        self.TabTime=TabTime


def Ecrire(Matiere):
    C2 = 2 #Interval n = C2 * Interval n-1
    C1 = 3600 #Durée en seconde avant la première révision
    K = 0.8 #Pourcentage Minimum avant qu'on passe à la prochaine révision
    colors=['r','g','b', 'c', 'm', 'y', 'k', 'w']

    current_time = datetime.datetime.now().timestamp()
    Matiere.TabTime.append(current_time)

    for i in range(len(Matiere.TabTime)-1):
        t = np.arange(Matiere.TabTime[i]-Matiere.TabTime[0], Matiere.TabTime[i+1]-Matiere.TabTime[0], 0.1)
        f = 100*np.exp(((t-(Matiere.TabTime[i]-Matiere.TabTime[0]))*np.log(K)/(C1*C2**i)))
        plt.plot(t, f, label=f"Révision n°{i}", color=colors[i])


    timer = (C1*C2**i)-(Matiere.TabTime[i+1]-Matiere.TabTime[0])
    if timer>0 :
        plt.text(10, 10, f'Prochaine révision dans {timer} secondes')
    else :
        plt.text(10, 10, f"Vous avez dépassé l'horaire idéale pour réviser la matière {Matiere.nom}",color='r')

    plt.legend()

    plt.xlabel('temps (en seconde)')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    axes.set_xlim(0, 3600*24*7) #on définit l'axe sur 30 minutes

    plt.ylabel('% Memorisé')
    axes.set_ylim(0, 100)


    plt.title(f'Tracé de la fonction oubli pour la matière {Matiere.nom}')

    plt.grid(False)
    plt.show()


