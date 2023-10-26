


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

def conversiontime(secondes):
    min = int(secondes/60)
    h = int(min/60)
    j = int(h/24)
    mois = int(j/30.436875)
    restmin = min%60
    resth = h%24
    restj = int(j%30.436875)
    return mois, restj, resth, restmin






def secondes_a_heures(x, pos):
    return f"{int(x/(3600))} h {int((x%(3600))/60)} min "
def secondes_a_jours(x, pos):
    return f"{int(x/(3600*24))} j {int((x%(3600*24))/3600)} h"
def secondes_a_mois(x, pos):
    return f"{int(x/(3600*24*30.436875))} m {int((x%(3600*24*30.436875))/(3600*24))} j"
     #Avec 30,436875 la durée moyenne d'un mois




def Ecrire(Matiere,indice):

    C2 = 3 #Interval n = C2 * Interval n-1
    C1 = 3600*1.5 #Durée en seconde avant la première révision
    K = 0.8 #Pourcentage Minimum avant qu'on passe à la prochaine révision
    colors=['r','g','b', 'c', 'm', 'y', 'k', 'w']

    current_time = datetime.datetime.now().timestamp()
    Matiere.TabTime.append(current_time)
    temps_ecoule = Matiere.TabTime[-1]-Matiere.TabTime[0]

    plt.figure(figsize=(10, 8))

    #pointsy=[90,100]

    for i in range(len(Matiere.TabTime)-1):
        t = np.arange(Matiere.TabTime[i]-Matiere.TabTime[0], Matiere.TabTime[i+1]-Matiere.TabTime[0], 0.1)
        f = 100*np.exp(((t-(Matiere.TabTime[i]-Matiere.TabTime[0]))*np.log(K)/(C1*C2**i)))
        plt.plot(t, f, label=f"Révision n°{i}", color=colors[i])
        print(f)
        if (i==0):
            pass
        else :
            binf = 100*np.exp(((Matiere.TabTime[i]-Matiere.TabTime[i-1])*np.log(K)/(C1*C2**(i-1))))

            pointsy=[binf,100]
            tconst = int(Matiere.TabTime[i]-Matiere.TabTime[0])
            plt.plot( [tconst,tconst] , pointsy, f'{colors[i]}--')
            timer = (C1*C2**i)-(temps_ecoule)






    x = np.linspace(0, 2*(temps_ecoule), 30)
    seuil=np.ones_like(x)*100*K
    plt.plot(x,seuil,'k--', label = "Seuil")



    if timer>0 :
        plt.text((temps_ecoule/10), 10, f"prochaine révision conseillée dans {conversiontime(int(timer))[0]} mois, {conversiontime(int(timer))[1]} jours, {conversiontime(int(timer))[2]} heures, {conversiontime(int(timer))[3]} minutes ")
    else :
        plt.text((temps_ecoule/3), 10, f"Vous avez dépassé l'horaire idéale pour réviser la matière {Matiere.nom}",color='r')

    plt.legend(loc = 'upper right')


    if temps_ecoule < 3600*12 :
        print("affichage heure")
        format = FuncFormatter(secondes_a_heures)
    elif temps_ecoule < 1.5 * 3600*24*30.436875 : #après 1 mois et demi l'unité de légende du temps devient le mois
        format = FuncFormatter(secondes_a_jours)
        print("affichage jour")

    else :
        format = FuncFormatter(secondes_a_mois)




    plt.xlabel('temps')
    axes = plt.gca()
    #axes.set_xlim(0, 3153600) #on définit l'axe x sur 1 an : 3153600 secondes
    #axes.set_xlim(0, 3600*24*7) #on définit l'axe sur 1 semaine
    axes.set_xlim(0,1*(temps_ecoule))

    axes.xaxis.set_major_formatter(format)

    plt.ylabel('% Memorisé')
    axes.set_ylim(0, 100)


    plt.title(f'Tracé de la fonction oubli pour la matière {Matiere.nom}')

    plt.grid(False)
    plt.savefig(f"static/images/chart{indice}.png", transparent = True, edgecolor = "r")
    plt.show()



#Equation de la fonction oubli : https://www.super-memory.com/english/2vm.htm
