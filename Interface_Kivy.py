# -*- coding: utf-8 -*-
#Aides: https://kivy.org/doc/stable/guide/lang.html                 #Documenation sur la Synthax a avoir
#Aides: https://kivy.org/doc/stable/api-kivy.uix.label.html         #Documentation sur les differents Widgets de base de Kivy
#Aides: https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html     #Documentation sur le Layout (couche) dit 'BoxLayout' de Kivy
#Aides: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html #Documentation sur les ScreenManagers et leurs fonctionnalités

#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date
#---------------------------------------Importante LIB---------------------------------------

#---------------------------------------Project LIB---------------------------------------
import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

from pydub import AudioSegment                              #Bibliotheque permettant de jouer des Sons et Jingles
from pydub.playback import play                             #""""""""""""""""""""""""""""""""""""""""""""""""""""

print("\n Bonjour/Bonsoir, ne pas faire fonctionner ce programme en utilisant les droits/commandes administrateur si l'utilisateur n'est pas l'Admin au quel cas le programme ne fonctionnera pas correctement. \n") #Information a lire dans la console
sys.path.append("/home/"+USERNAME+"/CryptoWatch-Kivy/Services")  #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
#print(USERNAME)                                            #Test debug

from Infos_Hardware import CPU_usage                        #Obtention de l'utilisation du Processeur par le Systeme d'exploitation et ses programmes autour
from Infos_Hardware import CPU_temp                         #Obtention de la Temperature du Processeur sur la carte mere
from Infos_Hardware import SoC_info                         #Obtention des informations concernant le package CPU+GPU
from Infos_Hardware import MEM_info                         #Obtention de l'utilisation de la Memoire Vive du Systeme

from Infos_complementaires import Get_Marche_BTC            #Obtention de la Valeur du BTC sur le Marche
from Infos_complementaires import Get_Fear_Greed_Index      #Obtention d'une image indicant les sentiments des acteurs du Marche

from Infos_Coins import Recherche_Info_Coin                 #Obtention des Informations detaillee concernant un Monnaie crypto relie a une autre monnaie (Crypto/Fiat)
from Infos_Coins import Recherche_Et_Surveillance_Coin      #Permet la Surveillance d'une paire

from Graph import Dessiner_Graph                            #Avec cette fontcion nous pouvons obtenir un graph en rapport avec la crypto-monnaie definie
#---------------------------------------Project LIB---------------------------------------


#---------------------------------------Kivy LIB---------------------------------------
from kivy.app import App                                        #Utile a Kivy
from kivy.uix.boxlayout import BoxLayout                        #Importation de la disposition BoxLayout
from kivy.uix.anchorlayout import AnchorLayout                  #Importation de la disposition AnchorLayout
# BoxLayout: it's in the python part, so you need to import it
from kivy.uix.widget import Widget                              #Importation des différents widget disponible

from kivy.properties import StringProperty                      #Importation du StringProperty permettant de faire des variables dynamiques

from kivy.clock import Clock                                    #Importation de Clock permettant de gerer les mises a jour des elements

from kivy.lang import Builder                                   #Importation de Builder pour la lecture et l'interpretation du language KV

from kivy.uix.screenmanager import ScreenManager, Screen        #Importation de ScreenManager/Screen permettant la gestion de plusieurs 'ecran'(aka Fenetre ou page).

from kivy.uix.popup import Popup                                #Importation des Popup de Kivy

from kivy.uix.label import Label                                #Importation des Label de Kivy

from kivy.uix.button import Button                              #Importation des Boutton de Kivy

#---------------------------------------Kivy LIB---------------------------------------
#Builder.load_string(""" """)           #Saisie indiquant la disposition des elements visuels

Builder.load_file('Interface_Kivy.kv')  #Chargement du fichier qui indique la disposition des elements visuels

#---------------------------------------------------------------------------------------------------------------------------------------
class MaDisposition(BoxLayout, Screen):

    #---Variables a Mettre a jour---

    #--Horloge--
    Time_Horloge = StringProperty()     #Quand cette variable changera, toute les elements comportant cette variable se mettront a jour lorsque sa valeurs changera car elle est specifie 'StringProperty'
    #--Horloge--

    #--Informations Materiels--
    UtilisationCPU = StringProperty()
    MemoireUtilise = StringProperty()
    CPUtemp = StringProperty()
    #--Informations Materiels--

    #--Informations Complementaires--
    BTC_Market = StringProperty()
    Fear_Gread_Index_path = "/home/"+USERNAME+"/CryptoWatch-Kivy/Services/Telechargements/Fear_Greed_Index.png" #Pour indiquer le chemin ou se trouve l'Image de l'index dans l'Ordinateur
    #--Informations Complementaires--

    #---Variables a Mettre a jour---    

        
    def __init__(self, **kwargs):
        super(MaDisposition, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)
        Clock.schedule_interval(self.temps_actuel_update,1)
        Clock.schedule_interval(self.update_information_Materiel,1)
        Clock.schedule_once(self.update_information_Complementaire)
        Clock.schedule_interval(self.update_information_Complementaire, 313)
        #---Elements a Mettre a jour---

    
    #---------------------------------------------
    def temps_actuel(self):   
        #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
        #-- DEBUT -- Heure,Minute,Seconde
        tt = time.time()
        system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
        print(("Voici l'heure:",system_time))
        return system_time
        #-- FIN -- Heure,Minute,Seconde
    def temps_actuel_update(self, *args):                                           #On met a jour l'Objet Time_Horloge avec l'heure de la methode precedente
        self.Time_Horloge = MaDisposition.temps_actuel(self)
    #---------------------------------------------

    #---------------------------------------------
    def information_Materiel(self):
        #Obtention des Informations Materiel de l'Ordinateur

        #--        
        self.UtilisationCPU = CPU_usage()                                           #Obtention du Niveau d'utilisation du Processeur.
        self.MemoireUtilise = MEM_info()                                            #Obtention d'information par rapport à la Memoire Vive.
        self.CPUtemp = CPU_temp()                                                   #Obtention de la Temperature du Package Processeur/GPU.
        #mesure_voltage,memoire_processeur,memoire_gpu  = SoC_info()                #Obtention d'information par rapport au Couple CPU/GPU.
        #--

    def update_information_Materiel(self, *args):
        #Mise a Jour des Informations a Propos du Materiel
        #--        
        self.UtilisationCPU = CPU_usage()                                           #Obtention du Niveau d'utilisation du Processeur.
        self.MemoireUtilise = MEM_info()                                            #Obtention d'information par rapport à la Memoire Vive.
        self.CPUtemp = CPU_temp()                                                   #Obtention de la Temperature du Package Processeur/GPU.
        #--
    #---------------------------------------------

    #---------------------------------------------
    def information_Complementaire(self):
        #Recuperation des Informations  
        self.BTC_Market = Get_Marche_BTC()                                          #On Obtient le Prix d'un BTC sur le marche en EURO
        Get_Fear_Greed_Index()                                                      #On Obtient l'index de Fear&Greed du BTC sur le Marche
        
    def update_information_Complementaire(self, *args):
        #Mise à Jour des Informations reçues
        self.BTC_Market = Get_Marche_BTC()                                          #On met a jour le prix affiche en EURO du BTC sur le Marche
        Get_Fear_Greed_Index()                                                      #On met a jour l'index Fear and Greed du BTC sur le Marche
    #---------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class En_Direct_Du_Marche(BoxLayout, Screen):

    def Rechercher_BTC_EUR(self):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin("BTC-EUR")

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()
        

    def Rechercher_BTC_USD(self):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin("BTC-USD")

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()
        
    def Rechercher_ETH_EUR(self):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin("ETH-EUR")

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()
        
    def Rechercher_ETH_USD(self):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin("ETH-USD")

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()
        
    def Rechercher_LINK_EUR(self):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin("LINK-EUR")

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()
        
    def Rechercher_LINK_USD(self):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin("LINK-USD")

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()

    def Rechercher_de_la_Paire(self,Paire_Indiquee):
        #Recuperation des Informations
        self.Symbole_Coin_cryptonator,self.Prix_Actuel_cryptonator,self.Volume_24h_cryptonator,self.Difference_Prix_24h_cryptonator,self.Volume_Monnaie_30DAY,self.Prix_Moins_Eleve_24h,self.Prix_Actuel,self.Prix_Plus_Eleve_24h,self.Liquidite_Achat,self.Liquidite_Vente = Recherche_Info_Coin(Paire_Indiquee)

        InfoPopup = BoxLayout(orientation='vertical')
        
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)

        BoutonFermeturePopup = Button(text="Fermer")
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
        InfoPopup.add_widget(BoutonFermeturePopup)
        
        KivyPopup.open()
        

    def recuperation_input(self):
        #Obtenir l'entree que l'utilisateur a saisie
        #ID INPUT : Entree_texte_RECHERCHE

        Paire_Selectionee = self.ids.Entree_texte_RECHERCHE.text                     #Accession a la valeur du widget ayant pour ID "Entree_texte_RECHERCHE"
        #print(InputUser)
        En_Direct_Du_Marche.Rechercher_de_la_Paire(self,Paire_Selectionee)           #Obtention des Informations du Coin/Token sur le marché par rapport au Informations saisie dans la boite a texte

        

        
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class Surveillance_Du_Marche(BoxLayout, Screen):
#PROBLEME DANS CETTE CLASSE:
    #1- Informations non mises a jour dans l'interface visuel alors qu'elles le sont dans la console
    #2- Un Probleme effectue la MAJ des infos alors que le POPUP est fermer... a fix!

    #---Variables a Mettre a jour---
    #--Surveillance--
    #Annonce_0 = StringProperty()     #Quand cette variable changera, toute les elements comportant cette variable se mettront a jour lorsque sa valeurs changera car elle est specifie 'StringProperty'
    #Annonce_1 = StringProperty()
    #Message_Personnaliser = StringProperty()
    #--Surveillance-- 

    def __init__(self, **kwargs):
        super(Surveillance_Du_Marche, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)
        #---Elements a Mettre a jour---

        Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text
        Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text
        Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text       

        self.Recuperation_Paire = Recuperation_Paire
        self.Recuperation_Montant = Recuperation_Montant
        self.Recuperation_Message_Personnaliser = Recuperation_Message_Personnaliser


    #Recuperation des Entrees
    def recuperation_input_surveillance(self):
        Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text                                                                                  #Recuperation de la Valeur saisie dans la boite a texte
        Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text                                                                                #Recuperation de la Valeur saisie dans la boite a texte
        Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text                                                                  #Recuperation de la Valeur saisie dans la boite a texte
        print(Recuperation_Paire +" " + Recuperation_Montant +" "+ Recuperation_Message_Personnaliser)                                                  #Affichage de cette valeur dans la console

        Surveillance_Du_Marche.Affichage_Etat_Surveillance(self,Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)                  #On donne les information saisie a cette fonction pour traitement


    #Traitement du Resultat et de son affichage
    def Affichage_Etat_Surveillance(self,Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser):
        #Recuperation des Informations
        self.Annonce_0 , self.Annonce_1 , self.Message_Personnaliser, boolean_popup = Recherche_Et_Surveillance_Coin(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)

    def Lancement_Surveillance(self):
        Surveillance_Du_Marche.recuperation_input_surveillance(self)
        sm.current = 'PageAlerte'

    def get_Recuperation_Paire(self):
        return self.Recuperation_Paire

    def get_Recuperation_Montant(self):
        return self.Recuperation_Montant

    def get_Recuperation_Message_Personnaliser(self):
        return self.Recuperation_Message_Personnaliser


#-----------------------------------
class PageAlerte(BoxLayout, Screen):
#AIDES : https://www.geeksforgeeks.org/getter-and-setter-in-python/


    #---Variables a Mettre a jour---
    #--Surveillance--
    Annonce_0 = StringProperty()     #Quand cette variable changera, toute les elements comportant cette variable se mettront a jour lorsque sa valeurs changera car elle est specifie 'StringProperty'
    Annonce_1 = StringProperty()
    Message_Personnaliser = StringProperty()

    #Recuperation_Paire = StringProperty()
    #Recuperation_Montant = StringProperty()
    #Recuperation_Message_Personnaliser = StringProperty()
    #--Surveillance--
                
    def __init__(self, **kwargs):
        super(PageAlerte, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)
        #---Elements a Mettre a jour---


    def update_Affichage_Etat_Surveillance(self, *args):
        getter = Surveillance_Du_Marche()

        Recuperation_Paire = getter.get_Recuperation_Paire()                                                          #Recuperation de la Valeur saisie dans la boite a texte
        Recuperation_Montant = getter.get_Recuperation_Montant()                                                      #Recuperation de la Valeur saisie dans la boite a texte
        Recuperation_Message_Personnaliser = getter.get_Recuperation_Message_Personnaliser()                          #Recuperation de la Valeur saisie dans la boite a texte

        #MAJ des Informations
        self.Annonce_0 , self.Annonce_1 , self.Message_Personnaliser, boolean_popup = Recherche_Et_Surveillance_Coin(Recuperation_Paire,Recuperation_Montant,Recuperation_Message_Personnaliser)

        Clock.schedule_once(self.update_Affichage_Etat_Surveillance)
        time.sleep(5)
        Clock.schedule_interval(self.update_Affichage_Etat_Surveillance, 1)

    def Stop_update_Affichage_Etat_Surveillance(self):
        Clock.unschedule(self.update_Affichage_Etat_Surveillance)

    #LE PROBLEME PRINCIPAL DANS CETTE CLASSE le 24/11/2019:
    #Lorsque schedule_once est lancer , le programme obtient la valeur saisie par l'utilisateur
    #Alors que schedule_interval est lancer, le programme obtient la valeur par défaut
    #Ce qui n'est pas NORMAL ... a chercher !!!!
                
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class Visualiser_Cours_Du_Marche(BoxLayout, Screen):
    pass
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------Creation du Screen Manager---------------------------------------------
#HELP: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
#Dans cette partie du code, on indique les differents 'ecrans' ou fenetres que dispose ce logiciel sous Kivy
sm = ScreenManager()
sm.add_widget(MaDisposition(name ='Accueil'))
sm.add_widget(En_Direct_Du_Marche(name='En Direct du Marche'))
sm.add_widget(Surveillance_Du_Marche(name='Surveillance du Marche'))
sm.add_widget(PageAlerte(name='PageAlerte'))
sm.add_widget(Visualiser_Cours_Du_Marche(name='Visualiser le cours du Marche'))
#---------------------------------------------Creation du Screen Manager---------------------------------------------
      
class CryptoWatchApp(App):

    def on_start(self):
        #Indique ce que l'on fait au demarage du logiciel.
        pass
    
    def on_stop(self):
        #Indique ce que l'on fait a l'arret du logiciel.
        pass
    
    def build(self):
        #Demarage du Logiciel Kivy.
        return sm
    
if __name__ == "__main__":
    #Demarage du Logiciel Kivy
    CryptoWatchApp().run()
