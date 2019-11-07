#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AIDES: https://gist.github.com/Franck1333/63efdfc6c80feb981341445c2295aaee

import os
import sys
import datetime
import time
from nettoyage_du_cache import clear_cache
from Re_tailler_une_image import Re_tailler_une_image_Donner

import json         #Traitement du fichier JSON reçu
import requests     #<-- Utilisation d'une Adresse URL Normalisée
from urllib.request import urlretrieve       #Bibliotheque permettant le telechargement de ressources sur Internet via les protocoles HTTP/HTTPS

import getpass                                              #On importe la blibliotheque "getpass"
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

def Get_Marche_BTC():
    #Cette fonction permet d'Obtenir le cours du BTC du Marche actuel
    send_url = "https://blockchain.info/ticker"                   #URL a composer
    r = requests.get(send_url)                                    #<-- Ouverture de L'URL pour l'utilisation de L'API
    reponse = json.loads(r.text)                                  #Chargement des données reçu dans le fichier en format JSON
    #print(reponse)                                               #Test Debug dans la console

    Devise_Symbole = reponse["EUR"]["symbol"]                                   #Obtention du Symbole de la Monnaie FIAT concernee
    BTC_Prix_du_Marche_JSON = reponse["EUR"]["15m"]                             #Obtention de la Valeur du BTC au cour du Marche
    BTC_Prix_du_Marche = str(BTC_Prix_du_Marche_JSON)                           #On convertis la valeur FLOAT en STRING pour son enregistrement et son affichage

    print("Prix d'un BTC: "+ BTC_Prix_du_Marche+" "+Devise_Symbole)             #Affichage des resultats dans la console serie

    tk_BTC_Market = "Prix d'un BTC: "+ BTC_Prix_du_Marche+" "+Devise_Symbole    #Enregistrement des resultats pour une utilisation ultérieur

    return tk_BTC_Market                                                        #On retourne les resultats

def Get_Fear_Greed_Index():
    #Cette fonction a pour objectif de telecharger une image au format PNG du site 'alternative.me'
    print("ANNONCE: Debut du Telechargement de l'Image Fear_Greed_Index.png")

    LIEN = "https://alternative.me/crypto/fear-and-greed-index.png"                                         #Localisation de l'image sur Internet a Telecharger
    urlretrieve(LIEN,'/home/'+USERNAME+'/CryptoWatch-Kivy/Services/Telechargements/Fear_Greed_Index.png')  #Telechargement et Enregistrement de l'image
    
    print("ANNONCE: Fin du Telechargement de l'Image Fear_Greed_Index.png")

    #print("ANNONCE: Debut Modification de la taille de l'Image")
    #Re_tailler_une_image_Donner(720, '/home/'+USERNAME+'/CryptoWatch-Kivy/Services/Telechargements/Fear_Greed_Index.png' , '/home/'+USERNAME+'/CryptoWatch-Kivy/Services/Telechargements/Fear_Greed_Index.png') #Redimenssionement de l'image telechargee.
    #print("ANNONCE: Fin Modification de la taille de l'Image")



if __name__ == "__main__":
 clear_cache()          #Nettoyage du Cache Python.
 Get_Marche_BTC()       #Obtention de la Valeur d'un Bitcoin sur le Marche en Direct.
 Get_Fear_Greed_Index() #Obtention d'une image indicant les sentiments des acteurs du Marche.

