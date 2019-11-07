# -*- coding: utf-8 -*-


#pip3 install numpy && pip3 install matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 4, 6])                  #Definition des valeurs a demontrer sous forme de liste python
y = np.array([2, 3, 5, 1])                  #Definition des valeurs a demontrer sous forme de liste python

plt.plot(x, y)                              #Comparaison des deux valeurs
plt.title("Demonstration #1")               #Affichage du Titre du document
plt.xlabel("abscisses")                     #On peut donner des Noms a l'axe X
plt.ylabel("ordonnees")                     #On peut donner des Noms a l'axe Y
plt.plot(x, y, label="cos(x)")              #Saisie de la Legende
plt.legend()                                #Insertion d'une Legende
plt.show()                                  #Affiche la figure a l'ecran
