import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.signal import medfilt

def afficher_temperature(tempreel, tempmesure, erreur):
    """
    Permet l'initialisation des courbes de base entre la température réel et celle mesurée
    Et l'histogramme d'erreur de la température réelle et la temérature mesurée entre les 2 courbes
    """
    plt.plot(tempreel, label="Température réelle")
    plt.plot(tempmesure, label="Température mesurée",color="green")
    plt.bar(range(len(erreur)), erreur,label="Erreur de mesure",color="red")

def affiche_temperaturelisse(tempreel, templisse):
    """
        Permet l'initialisation de la courbe de la température après lissage
        Et l'histogramme d'erreur de la température réelle et la température mesurée et lissée entre les 2 courbes
    """
    erreur2=abs(tempreel-templisse)
    plt.plot(templisse,label="Température lissée",color="purple")
    plt.bar(range(len(erreur2)), erreur2,label="Erreur de mesure après lissage",color="orange")


def main():
    temperatures = np.load("temperatures.npy")
    tempreel = temperatures[:, 0]
    tempmesure = (temperatures[:, 1] * 10) - 10
    erreur = abs(tempreel - tempmesure)
    afficher_temperature(tempreel, tempmesure, erreur)
    templisse = medfilt(temperatures[:, 1]) * 10 - 10
    affiche_temperaturelisse(tempreel, templisse)
    plt.legend()
    plt.show()
    rmse = sqrt(sum((tempmesure - tempreel) ** 2) / len(tempreel))
    print("RMSE :", rmse) # valeur obtenue : 2.4120288344316108
    rmse = sqrt(sum((templisse - tempreel) ** 2) / len(templisse))
    print("RMSE après lissage des valeurs :", rmse) # valeur obtenue : 1.619334067780903

main()





