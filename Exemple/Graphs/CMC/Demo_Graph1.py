# -*- coding: utf-8 -*-

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

#pip3 install numpy && pip3 install matplotlib
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------
import sys
sys.path.append("/home/"+USERNAME+"/CryptoWatch/Services")              #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
#print(USERNAME)
from Get_historical_info_by_CMC_CoinmarketCap import Recuperation_Historique_Crypto
from Get_historical_info_by_CMC_CoinmarketCap import Recuperation_Historique_Crypto_2
#---------------------------------------------

def Dessiner_Graph():
    #Exemple du BTC-USD
    #Time-Frame pour test : DAILY
    #Plus tard, on choisira la Time-Frame
    #Pour ce faire, il nous faut:
    #                               -Une liste contenant les 30 derniers prix du BTC sur l'axe X 
    #                               -Une liste contenant les 30 derniers prix du USD

    #liste_Date , liste_Close = Recuperation_Historique_Crypto('Bitcoin')
    liste_Date , liste_Close = Recuperation_Historique_Crypto_2('Bitcoin','2016-05-13','2019-09-09')

    x = np.array(liste_Date)                    #Definition des valeurs sur l'Abcisses a demontrer sous forme de liste python
    y = np.array(liste_Close)                   #Definition des valeurs sur les Ordonnees a demontrer sous forme de liste python

    plt.plot(x, y)                              #Comparaison des deux valeurs
    plt.title("Paire: CRYPTO vs USD")           #Affichage du Titre du document
    plt.xlabel("Dates (Abscisses)")             #On peut donner des Noms a l'axe X
    plt.ylabel("Prix (Ordonnees)")              #On peut donner des Noms a l'axe Y
    plt.plot(x, y, label="Prix du Marché")      #Saisie de la Legende
    plt.legend()                                #Insertion d'une Legende
    plt.show()                                  #Affiche la figure a l'ecran

if __name__ == "__main__":
    Dessiner_Graph()
