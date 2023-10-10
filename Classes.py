


import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import numpy as np
import datetime

class Revision():
    def __init__(self, num, nom, TabTime):
        self.numero=num
        self.nom=nom
        self.TabTime=TabTime
day = datetime.date.today()
def nbre_jours(year,month):
    if month in [4, 6, 9, 11]:
        return(30)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return(31)
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return(29)
        else:
            return(28)
def secondes_a_heures(x, pos):
    return f"{x/(3600):.2f}"
def secondes_a_jours(x, pos):
    return f"{x/(3600*24):.2f}"
def secondes_a_mois(x, pos): #algorithme incorrect
    return f"{x/(3600*24*nbre_jours(day.year, day.month)):.2f}"



def Ecrire(Matiere):
    C2 = 4 #Interval n = C2 * Interval n-1
    C1 = 3600*2 #Durée en seconde avant la première révision
    K = 0.8 #Pourcentage Minimum avant qu'on passe à la prochaine révision
    colors=['r','g','b', 'c', 'm', 'y', 'k', 'w']

    current_time = datetime.datetime.now().timestamp()
    Matiere.TabTime.append(current_time)

    for i in range(len(Matiere.TabTime)-1):
        t = np.arange(Matiere.TabTime[i]-Matiere.TabTime[0], Matiere.TabTime[i+1]-Matiere.TabTime[0], 0.1)
        f = 100*np.exp(((t-(Matiere.TabTime[i]-Matiere.TabTime[0]))*np.log(K)/(C1*C2**i)))
        plt.plot(t, f, label=f"Révision n°{i}", color=colors[i])

    x = np.linspace(0, 3600*24*7, 30)
    seuil=np.ones_like(x)*100*K
    plt.plot(x,seuil,'k--', label = "Seuil")

    timer = (C1*C2**i)-(Matiere.TabTime[i+1]-Matiere.TabTime[0])
    if timer>0 :
        plt.text(10, 10, f'Prochaine révision conseillée dans {int(timer)} secondes')
    else :
        plt.text(10, 10, f"Vous avez dépassé l'horaire idéale pour réviser la matière {Matiere.nom}",color='r')

    plt.legend()



    formatterJour = FuncFormatter(secondes_a_jours)



    plt.xlabel('temps (en jours)')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    #axes.set_xlim(0, 3600*24*7) #on définit l'axe sur 1 semaine
    axes.set_xlim(0,2*(Matiere.TabTime[-1]-Matiere.TabTime[0]))

    axes.xaxis.set_major_formatter(formatterJour)

    plt.ylabel('% Memorisé')
    axes.set_ylim(0, 100)


    plt.title(f'Tracé de la fonction oubli pour la matière {Matiere.nom}')

    plt.grid(False)
    plt.show()


#Equation de la fonction oubli : https://www.super-memory.com/english/2vm.htm
