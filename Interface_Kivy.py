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
        Clock.schedule_interval(self.update_information_Materiel,1)                     #On indique a Kivy quand Commencer/Re-commencer l'execution d'une methode
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

        InfoPopup = BoxLayout(orientation='vertical')                                                       #On indique que l'object InfoPopup aura comme particularite d'avoir un Layout BoxLayout en orientation vertical
                                                                                                            #Donc son contenue sera tous en Vertical
        InfoPopup.add_widget(Label(text= self.Symbole_Coin_cryptonator))                                    #On peut ajouter dans Kivy, des Widgets 'On the fly' sans forcemment passer par un fichier .kv et sa lecture par consequent.                               
        InfoPopup.add_widget(Label(text= self.Prix_Actuel_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Difference_Prix_24h_cryptonator))
        InfoPopup.add_widget(Label(text= self.Volume_Monnaie_30DAY))
        InfoPopup.add_widget(Label(text= self.Prix_Moins_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Prix_Plus_Eleve_24h))
        InfoPopup.add_widget(Label(text= self.Liquidite_Achat))
        InfoPopup.add_widget(Label(text= self.Liquidite_Vente))
        
        KivyPopup = Popup(title= self.Symbole_Coin_cryptonator, content=InfoPopup, auto_dismiss=True)       #On créer un objet Popup en luo donnant plusieurs valeur , comme son titre , son contenue et un parametre d'auto-destruction

        BoutonFermeturePopup = Button(text="Fermer")                                                        #On ajoute un bouton permettant de fermer soi-meme le popup afficher a l'ecran
        BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)                                               #On joint la fonctionnaliter de fermeture au bouton
        InfoPopup.add_widget(BoutonFermeturePopup)                                                          #Puis on ajoute ce bouton dans le pop comme etant un contenue
        
        KivyPopup.open()                                                                                    #Et pour terminer on demande a Kivy d'afficher ce popup a cet instant
        

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
    #---Variables a Mettre a jour---
    #--Surveillance--
    Annonce_0 = StringProperty()     #Quand cette variable changera, toute les elements comportant cette variable se mettront a jour lorsque sa valeurs changera car elle est specifie 'StringProperty'
    Annonce_1 = StringProperty()
    Message_Personnaliser = StringProperty()
    Recuperation_Paire = StringProperty()
    Recuperation_Montant = StringProperty()
    Recuperation_Message_Personnaliser = StringProperty()
    #--Surveillance-- 

    def __init__(self, **kwargs):
        super(Surveillance_Du_Marche, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)XLM-EUR
        #Clock.schedule_interval(self.get_Recuperation_Paire ,1)
        #Clock.schedule_interval(self.get_Recuperation_Montant ,1)
        #Clock.schedule_interval(self.get_Recuperation_Message_Personnaliser ,1)
        #---Elements a Mettre a jour---

        #Getter object
        #self.Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text
        #self.Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text
        #self.Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text

    #Traitement du Resultat et de son affichage
    def Affichage_Etat_Surveillance(self, *args):
        #Recuperation des Entrees
        self.Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text                                                                                  #Recuperation de la Valeur saisie dans la boite a texte qui detient ce meme identifiant
        self.Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text                                                                                #Recuperation de la Valeur saisie dans la boite a texte
        self.Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text                                                                  #Recuperation de la Valeur saisie dans la boite a texte
        print("Affichage_Etat_Surveillance: " + self.Recuperation_Paire +" " + self.Recuperation_Montant +" "+ self.Recuperation_Message_Personnaliser)                                                  #Affichage de cette valeur dans la console

        #Recuperation des Informations
        self.Annonce_0 , self.Annonce_1 , self.Message_Personnaliser, boolean_popup = Recherche_Et_Surveillance_Coin(self.Recuperation_Paire,self.Recuperation_Montant,self.Recuperation_Message_Personnaliser)

        if boolean_popup == True :                                      #Si la variable booleenne est VRAI, alors on affiche un popup a l'ecran
            InfoPopup = BoxLayout(orientation='vertical')
            
            InfoPopup.add_widget(Label(text= "On a un Résultat pour: "))
            InfoPopup.add_widget(Label(text= self.Recuperation_Paire))
            
            KivyPopup = Popup(title= self.Recuperation_Paire, content=InfoPopup, auto_dismiss=True,size_hint=(None, None), size=(200, 200))

            BoutonFermeturePopup = Button(text="Fermer")
            BoutonFermeturePopup.bind(on_press=KivyPopup.dismiss)
            InfoPopup.add_widget(BoutonFermeturePopup)
            
            KivyPopup.open()
        
    def Lancement_Surveillance(self):                                   #Cette fonction est utiliser par un bouton dans le fichier .kv pour lancer une surveillance et sa mise a jour
        Surveillance_Du_Marche.Affichage_Etat_Surveillance(self)
        Clock.schedule_interval(self.Affichage_Etat_Surveillance ,5)
        #sm.current = 'PageAlerte'

    def Stop_Affichage_Etat_Surveillance(self):                         #Cette fonction est utiliser aussi par un autre bouton dans la meme interface pour arreter la mise a jour de la surveillance concernee
        Clock.unschedule(self.Affichage_Etat_Surveillance)

    #C'etait une partie utiliser par la classe 'PageAlerte' qui a ete passer en commentaire car elle ne fonctionne pas comme prevue.
    #Le but ici etait de transmettre a cette classe les valeurs saisie dans les champs de texte remplie par l'utilisateur.
    #def get_Recup(self, *args):
    #    self.Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text                                                                                  #Recuperation de la Valeur saisie dans la boite a texte
    #    self.Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text                                                                                #Recuperation de la Valeur saisie dans la boite a texte
    #    self.Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text                                                                  #Recuperation de la Valeur saisie dans la boite a texte
    #    print("get_Recup: " + self.Recuperation_Paire +" " + self.Recuperation_Montant +" "+ self.Recuperation_Message_Personnaliser)                                                  #Affichage de cette valeur dans la console

        #Surveillance_Du_Marche.Affichage_Etat_Surveillance(self)   #Traitement
        #return self.Recuperation_Paire,self.Recuperation_Montant,self.Recuperation_Message_Personnaliser

    #def get_Recuperation_Paire(self, *args):
        #self.Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text
        #print("get_Recuperation_Paire: " + self.Recuperation_Paire)
        #return self.Recuperation_Paire

    #def get_Recuperation_Montant(self, *args):
        #self.Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text
        #print("get_Recuperation_Montant: " + self.Recuperation_Montant)
        #return self.Recuperation_Montant

    #def get_Recuperation_Message_Personnaliser(self, *args):
        #self.Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text
        #print("get_Recuperation_Message_Personnaliser: " + self.Recuperation_Message_Personnaliser)
        #return self.Recuperation_Message_Personnaliser


#-----------------------------------
#class PageAlerte(BoxLayout, Screen):
#AIDES : https://www.geeksforgeeks.org/getter-and-setter-in-python/

#L'objectif de cette classe etait d'afficher les resultats reçue par rapport a une alerte mise en place d'une alerte sur une crypto plutot par la classe 'Surveillance_Du_Marche'
#...Mais je n'ai pas reussie a trouver un moyen qui fonctionne.
#Le probleme etait qu'une fois que les donnes saisie par l'utilisateur sont reçue par cette classe une fois que l'utilisateur appuiyais sur un bouton pour lancer la surveillance, les données saisie se voit remplacer par celle qui sont saisie par défaut dans les Text_Input.

    #---Variables a Mettre a jour---
    #--Surveillance--
    #Annonce_0 = StringProperty()     #Quand cette variable changera, toute les elements comportant cette variable se mettront a jour lorsque sa valeurs changera car elle est specifie 'StringProperty'
    #Annonce_1 = StringProperty()
    #Message_Personnaliser = StringProperty()
    #--Surveillance--
                
    #def __init__(self, **kwargs):
    #    super(PageAlerte, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)
        #---Elements a Mettre a jour---


    #def update_Affichage_Etat_Surveillance(self, *args):
    #    getter = Surveillance_Du_Marche()
    #    self.Recuperation_Paire = getter.get_Recuperation_Paire()                                                          #Recuperation de la Valeur saisie dans la boite a texte
    #    self.Recuperation_Montant = getter.get_Recuperation_Montant()                                                      #Recuperation de la Valeur saisie dans la boite a texte
    #    self.Recuperation_Message_Personnaliser = getter.get_Recuperation_Message_Personnaliser()                          #Recuperation de la Valeur saisie dans la boite a texte
    #    print("update_Affichage_Etat_Surveillance:" + self.Recuperation_Paire,self.Recuperation_Montant,self.Recuperation_Message_Personnaliser)
        #self.Recuperation_Paire,self.Recuperation_Montant,self.Recuperation_Message_Personnaliser = getter.get_Recup()

        #Recuperation_Paire = self.ids.Entree_texte_SURVEILLANCE01.text                                                                                  #Recuperation de la Valeur saisie dans la boite a texte
        #Recuperation_Montant = self.ids.Entree_texte_SURVEILLANCE02.text                                                                                #Recuperation de la Valeur saisie dans la boite a texte
        #Recuperation_Message_Personnaliser = self.ids.Entree_texte_SURVEILLANCE03.text                                                                  #Recuperation de la Valeur saisie dans la boite a texte
        #print(Recuperation_Paire +" " + Recuperation_Montant +" "+ Recuperation_Message_Personnaliser)                                                  #Affichage de cette valeur dans la console       

        #MAJ des Informations
    #    self.Annonce_0 , self.Annonce_1 , self.Message_Personnaliser, boolean_popup = Recherche_Et_Surveillance_Coin(self.Recuperation_Paire,self.Recuperation_Montant,self.Recuperation_Message_Personnaliser)
    #    print("update_Affichage_Etat_Surveillance: "+self.Recuperation_Paire,self.Recuperation_Montant,self.Recuperation_Message_Personnaliser)
    #    Clock.schedule_once(self.update_Affichage_Etat_Surveillance)
    
    #def Stop_update_Affichage_Etat_Surveillance(self):
     #   Clock.unschedule(self.update_Affichage_Etat_Surveillance)

    #LE PROBLEME PRINCIPAL DANS CETTE CLASSE le 24/11/2019:
    #Lorsque schedule_once est lancer , le programme obtient la valeur saisie par l'utilisateur
    #Alors que schedule_interval est lancer, le programme obtient la valeur par défaut
    #Ce qui n'est pas NORMAL ... a chercher !!!
                
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class Visualiser_Cours_Du_Marche(BoxLayout, Screen):
    #En vue d'un problème technique qui doit etre resolue par les dev de l'API responsable d'obtenir les Historique sur CMC, cette partie ne sera pas developper car il n'y a pour le moment pas de moyen de debug si des problème il-y-a.
    #Lien: https://tinyurl.com/bugCMC19
    pass
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------Creation du Screen Manager---------------------------------------------
#HELP: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
#Dans cette partie du code, on indique les differents 'ecrans' ou fenetres que dispose ce logiciel sous Kivy
sm = ScreenManager()
sm.add_widget(MaDisposition(name ='Accueil'))
sm.add_widget(En_Direct_Du_Marche(name='En Direct du Marche'))
sm.add_widget(Surveillance_Du_Marche(name='Surveillance du Marche'))
#sm.add_widget(PageAlerte(name='PageAlerte'))
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
