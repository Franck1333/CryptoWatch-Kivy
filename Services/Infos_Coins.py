#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AIDES: https://docs.pro.coinbase.com/
#AIDES: https://github.com/danpaquin/coinbasepro-python

from nettoyage_du_cache import clear_cache  #Nettoyage des fichiers temporaires Python

import json                                 #Traitement du fichier JSON reçu
import requests                             #<-- Utilisation d'une Adresse URL Normalisée

import cbpro                                #CoinbasePro Python Wraper
public_client = cbpro.PublicClient()        #Instanciation d'un Objet cbpro


def Recherche_Et_Surveillance_Coin(Paire,Montant,Message_Personnaliser):
    send_url = "https://api.cryptonator.com/api/ticker/"+Paire                      #URL a composer
    r = requests.get(send_url)                                                      #<-- Ouverture de L'URL pour l'utilisation de L'API
    reponse = json.loads(r.text)                                                    #Chargement des données reçu dans le fichier en format JSON

    print(reponse)                                                                  #Test Debug dans la console
    Symbole_Coin_cryptonator = reponse["ticker"]["base"]                            #Enregistrement de l'Abreviation de la Monnaie/Token concernee
    Prix_Actuel_cryptonator = reponse["ticker"]["price"]                            #Enregistrement du Prix actuel de la Monnaie/Token concernee

    if int(float(Prix_Actuel_cryptonator)) == int(float(Montant)):
        print("Surveillance Fruictueuse!")
        print(Montant)
        tk_Annonce_0 = "Surveillance Fructueuse!"
        tk_Annonce_1 = "Pour "+Paire+ " l'Alerte a été déclenchée au Prix de: "+Prix_Actuel_cryptonator
        tk_Message_Personnaliser = Message_Personnaliser
        boolean_popup = True
        print("Etat de la variable 'boolean_popup': "+ str(boolean_popup))

    if int(float(Prix_Actuel_cryptonator)) > int(float(Montant)):
        print("Surveillance en cours...")
        print("Le prix ciblé est plus petit que celui du Marché")
        print(Montant)
        tk_Annonce_0 = "La Surveillance est en cours...,\n Le prix ciblé est plus petit que celui du Marché "
        tk_Annonce_1 = "Pour "+Paire+ ", le prix est actuellement de: "+Prix_Actuel_cryptonator
        tk_Message_Personnaliser = Message_Personnaliser
        boolean_popup = False

    if int(float(Prix_Actuel_cryptonator)) < int(float(Montant)):
        print("Surveillance en cours...")
        print("Le prix ciblé est plus GRAND que celui du Marché")
        print(Montant)
        tk_Annonce_0 = "La Surveillance est en cours... ,\n Le prix ciblé est plus GRAND que celui du Marché"
        tk_Annonce_1 = "Pour "+Paire+ ", le prix est actuellement de: "+Prix_Actuel_cryptonator
        tk_Message_Personnaliser = Message_Personnaliser
        boolean_popup = False

    return tk_Annonce_0 , tk_Annonce_1 , tk_Message_Personnaliser , boolean_popup

#Cette fonction permet d'obtenir des Informations sur la Paire 'BTC-EUR' sur la plateforme d'echange 'CoinbasePro'
def Recherche_Info_CoinbasePro():
 info_coin = public_client.get_product_24hr_stats('BTC-EUR')            #Enregistrement des Informations necessaire dans une variable
 #print(info_coin)

 Volume_Monnaie_30DAY = info_coin["volume_30day"]                       #Obtention du Volume de Monnaie/Token echanger sur 30 Jours

 Prix_Moins_Eleve_24h= info_coin["low"]                                 #Obtention du Prix le plus bas de la paire sur 24h
 Prix_Actuel = info_coin["last"]                                        #Obtention du Prix actuel de la Monnaie/Token
 Prix_Plus_Eleve_24h = info_coin["high"]                                #Obtention du Prix le Plus Eleve de la paire sur 24h

 print("Volume sur 30 Jours: "+Volume_Monnaie_30DAY+","                 #Affichage des Informations dans la console
       +"Son Prix le plus faible sur 24h: "+Prix_Moins_Eleve_24h+","+
       " Son Prix Actuel: "+Prix_Actuel+","+
       "Son Prix le Plus eleve sur 24h: "+Prix_Plus_Eleve_24h)

#Cette fonction permet la Recherche d'information d'une paire precise sur plusieurs API en meme temps ;
 #Dans cette version , si une des API n'obtient pas d'information due a une erreur ou autre , les resultats renvoyer seront nuls pour eviter des bugs dans le programme.
def Recherche_Info_Coin(Paire_Selectioner):
 global Volume_Monnaie_30DAY,Prix_Moins_Eleve_24h,Prix_Actuel,Prix_Plus_Eleve_24h,Liquidite_Achat,Liquidite_Vente

 try:
     print("La Paire Selectionee est: "+Paire_Selectioner+"\n")                     #La Paire saisie est affichee dans la console
     info_coinbase = public_client.get_product_24hr_stats(Paire_Selectioner)        #Recuperation des informations concernant une paire
     print(info_coinbase)                                                           #Affichage des informations brut concernant une paire dans la console
     info_liquidite_last = public_client.get_product_order_book(Paire_Selectioner)  #Recuperations des informations concernant l'Orderbook d'une paire sur CoinbasePro
     print(info_liquidite_last)                                                     #Affichage de l'Orderbook dans la console
         
     send_url = "https://api.cryptonator.com/api/ticker/"+Paire_Selectioner         #URL a composer
     r = requests.get(send_url)                                                     #<-- Ouverture de L'URL pour l'utilisation de L'API
     reponse = json.loads(r.text)                                                   #Chargement des données reçu dans le fichier en format JSON
     print(reponse)                                                                 #Test Debug dans la console

     #--------------------Source CoinbasePro--------------------
     Volume_Monnaie_30DAY = info_coinbase["volume_30day"]                           #Obtention du Volume de Monnaie/Token echanger sur 30 Jours
     Prix_Moins_Eleve_24h= info_coinbase["low"]                                     #Obtention du Prix le plus bas de la paire sur 24h
     Prix_Actuel = info_coinbase["last"]                                            #Obtention du Prix actuel de la Monnaie/Token
     Prix_Plus_Eleve_24h = info_coinbase["high"]                                    #Obtention du Prix le Plus Eleve de la paire sur 24h

     Liquidite_Achat_JSON =  info_liquidite_last["bids"][0][0]                      #Obtention du Prix du dernier trade effectue sur le reseau en tant que Prix d'Achat
     Liquidite_Vente_JSON =  info_liquidite_last["asks"][0][0]                      #Obtention du Prix du dernier trade effectue sur le reseau en tant que Prix de Vente
     Liquidite_Achat = str(Liquidite_Achat_JSON)                                    #Enregistrement du dernier Prix d'achat
     Liquidite_Vente = str(Liquidite_Vente_JSON)                                    #Enregistrement du dernier Prix de Vente

     #print("Prix d'achat: "+Liquidite_Achat)
     #print("Prix de Vente: "+Liquidite_Vente)
     #--------------------Source CoinbasePro--------------------

     #--------------------Source Cryptonator--------------------
     global Symbole_Coin_cryptonator,Prix_Actuel_cryptonator,Volume_24h_cryptonator,Difference_Prix_24h_cryptonator
     Symbole_Coin_cryptonator = reponse["ticker"]["base"]                           #Enregistrement de l'Abreviation de la Monnaie/Token concernee
     Prix_Actuel_cryptonator = reponse["ticker"]["price"]                           #Enregistrement du Prix actuel de la Monnaie/Token concernee
     Volume_24h_cryptonator = reponse["ticker"]["volume"]                           #Enregistrement du Volume echanger sur le marche durant les derniers 24h
     Difference_Prix_24h_cryptonator = reponse["ticker"]["change"]                  #Difference du Prix entre l'Ouverture du Marchee et sa Cloture
     #--------------------Source Cryptonator--------------------

     #print("Volume sur 30 Jours: "+Volume_Monnaie_30DAY+","
     #      +" Son Prix le plus faible sur 24h: "+Prix_Moins_Eleve_24h+","+
     #      " Son Prix Actuel: "+Prix_Actuel+","+
     #      " Son Prix le Plus eleve sur 24h: "+Prix_Plus_Eleve_24h+"\n")
     #
     #print("Le Prix actuel de "+Symbole_Coin_cryptonator+" est de : "+Prix_Actuel_cryptonator+
     #      " Avec une difference de prix sur 24h de: "+Difference_Prix_24h_cryptonator+","+
     #      " Pour un volume de: "+Volume_24h_cryptonator+" sur 24 heures."+"\n")
     
     
     #---Retour Info Mise-en-Page pour TK---
     global tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator
     #Cryptonator
     tk_Symbole_Coin_cryptonator = Symbole_Coin_cryptonator
     tk_Prix_Actuel_cryptonator = "Le prix du "+Symbole_Coin_cryptonator+" est de : "+ Prix_Actuel_cryptonator +" $"
     tk_Volume_24h_cryptonator = "Le Volume du "+Symbole_Coin_cryptonator+" sur 24H est de : " +Volume_24h_cryptonator
     tk_Difference_Prix_24h_cryptonator = "La différence de Prix du Marche depuis 24H est de : "+Difference_Prix_24h_cryptonator+" $"
     #Cryptonator
     
     #Coinbase
     tk_Volume_Monnaie_30DAY= "Le Volume d'actif echanger sur 30 Jours sur CoinbasePro est de "+ Volume_Monnaie_30DAY+" "+Symbole_Coin_cryptonator
     tk_Prix_Moins_Eleve_24h= "Le Prix du "+Symbole_Coin_cryptonator+" le plus bas sur 24H est de: "+Prix_Moins_Eleve_24h+" $"
     tk_Prix_Actuel = "Le Prix actuel du "+Symbole_Coin_cryptonator+" sur CoinbasePro est de: "+Prix_Actuel+" $"
     tk_Prix_Plus_Eleve_24h = "Le Prix du "+Symbole_Coin_cryptonator+" le plus HAUT sur 24H est de: "+Prix_Plus_Eleve_24h+" $"
     tk_Liquidite_Achat = "LIQUIDITE: Prix de demande: "+Liquidite_Achat+" $"
     tk_Liquidite_Vente = "LIQUIDITE: Prix d'offre: "+Liquidite_Vente+" $"
     #Coinbase 
     #---Retour Info Mise-en-Page pour TK---
     

     return  tk_Symbole_Coin_cryptonator,tk_Prix_Actuel_cryptonator,tk_Volume_24h_cryptonator,tk_Difference_Prix_24h_cryptonator,tk_Volume_Monnaie_30DAY,tk_Prix_Moins_Eleve_24h,tk_Prix_Actuel,tk_Prix_Plus_Eleve_24h,tk_Liquidite_Achat,tk_Liquidite_Vente
     pass
    
 #Gestion des erreurs
    #Dans le cas ou il aurait des erreurs de traitement ou des erreurs provenant des API, le programme indiquera que les informations ne sont pas disponibles pour le moment
 except KeyError:
    Volume_Monnaie_30DAY = "Erreur KeyError"
    Prix_Moins_Eleve_24h = "NO DATA"
    Prix_Actuel = "AUCUNE INFORMATION"
    Prix_Plus_Eleve_24h = " / "

    Liquidite_Achat = " Dans cette version , si une des API n'obtient pas d'information due a une erreur ou autre ,"+"\n"+" les resultats renvoyer seront nuls."
    Liquidite_Vente = " In this version, if one of the API didn't get intels cause by an error,"+"\n"+" so informations section will be empty."

    Symbole_Coin_cryptonator = "Aucune informations disponible pour le moment"
    Prix_Actuel_cryptonator = "No data available for now"
    Volume_24h_cryptonator = "Aucune informations disponible pour le moment"
    Difference_Prix_24h_cryptonator = "No data available for now"

    return  Symbole_Coin_cryptonator,Prix_Actuel_cryptonator,Volume_24h_cryptonator,Difference_Prix_24h_cryptonator,Volume_Monnaie_30DAY,Prix_Moins_Eleve_24h,Prix_Actuel,Prix_Plus_Eleve_24h,Liquidite_Achat,Liquidite_Vente

 except :
    Volume_Monnaie_30DAY = "Erreur Système"
    Prix_Moins_Eleve_24h = "NO DATA"
    Prix_Actuel = "AUCUNE INFORMATION"
    Prix_Plus_Eleve_24h = " / "
    Liquidite_Achat = " / "
    Liquidite_Vente = " / "
    Symbole_Coin_cryptonator = "Aucune informations disponible pour le moment"
    Prix_Actuel_cryptonator = "No data available for now"
    Volume_24h_cryptonator = "Aucune informations disponible pour le moment"
    Difference_Prix_24h_cryptonator = "No data available for now"
    return  Symbole_Coin_cryptonator,Prix_Actuel_cryptonator,Volume_24h_cryptonator,Difference_Prix_24h_cryptonator,Volume_Monnaie_30DAY,Prix_Moins_Eleve_24h,Prix_Actuel,Prix_Plus_Eleve_24h,Liquidite_Achat,Liquidite_Vente


if __name__ == "__main__":
     clear_cache()          #Nettoyage du Cache Python.
     #Recherche_Info_CoinbasePro()  #Obtention d'Information sur un coin donner sur CoinbasePro
     #Recherche_Info_Coin("XLM-EUR")          #Obtention d'Information sur un coin donner sur tout les exchanges possibles
     Recherche_Et_Surveillance_Coin("BTC-EUR",9000,"Coucou les Lapins") #Surveillance du Montant d'une Paire
