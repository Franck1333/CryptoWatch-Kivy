# -*- coding: utf-8 -*-


#pip3 install numpy && pip3 install matplotlib
import numpy as np
import matplotlib.pyplot as plt

#Exemple du BTC-USD
#Time-Frame pour test : DAILY
#Plus tard, on choisira la Time-Frame
#Pour ce faire, il nous faut:
#                               -Une liste contenant les 30 derniers prix du BTC sur l'axe X 
#                               -Une liste contenant les 30 derniers prix du USD

x = np.array([1, 3, 4, 6])                  #Definition des valeurs a demontrer sous forme de liste python
y = np.array([2, 3, 5, 1])                  #Definition des valeurs a demontrer sous forme de liste python

plt.plot(x, y)                              #Comparaison des deux valeurs
plt.title("Paire: BTC-USD")                 #Affichage du Titre du document
plt.xlabel("Abscisses")                     #On peut donner des Noms a l'axe X
plt.ylabel("Ordonnees")                     #On peut donner des Noms a l'axe Y
plt.plot(x, y, label="Prix du Marché")      #Saisie de la Legende
plt.legend()                                #Insertion d'une Legende
plt.show()                                  #Affiche la figure a l'ecran
