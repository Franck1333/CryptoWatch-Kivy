# -*- coding: utf-8 -*-
#Aides: https://kivy.org/doc/stable/guide/lang.html             #Documenation sur la Synthax a avoir
#Aides: https://kivy.org/doc/stable/api-kivy.uix.label.html     #Documentation sur les differents Widgets de base de Kivy
#Aides: https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html #Documentation sur le Layout (couche) dit 'BoxLayout' de Kivy

#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date
#---------------------------------------Importante LIB---------------------------------------

from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
# BoxLayout: it's in the python part, so you need to import it
from kivy.uix.widget import Widget

from kivy.properties import StringProperty
from kivy.event import EventDispatcher

from kivy.clock import Clock

from kivy.lang import Builder
Builder.load_string("""                 #Pour gérer la partie KV soit on ecrit le contenue directement dans cette methode de cette facon ou alors on renseigne de cette meme facon un fichier local avec ce contenue
                                        #Lorque le language KV est utiliser, il est pas necessaire d'importer quoi que ce soit.
<MaDisposition>
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        
        Label:                                               #WIDGET Permettant l'affichage d'un mot/phrase
            id:text_label                                    #Identifiant permettant a ce label d'etre accessible via le code python
            text_language: "fr"                              #Ligne permettant de connaitre la langue utiliser dans ce label
            text: root.Time_Horloge                        #Valeur qui doit etre afficher a l'ecran

            bold: False                                      #Parametre permettant de mettre en gras un label
            italic: False                                    #Permet de mettre en italique le contenue du label
            underline : False                                #Permet de souligner le contenue du label
            color: (13,1,1,1)                                #Parametre permettant d'ajouter de la couleur a un label

""")


class MaDisposition(AnchorLayout,EventDispatcher):

    Time_Horloge = StringProperty()

        
    def __init__(self, **kwargs):
        super(MaDisposition, self).__init__(**kwargs)
        self.Time_Horloge = MaDisposition.temps_actuel(self)
        Clock.schedule_interval(self.temps_actuel_update,1)
    
    #---------------------------------------------
    def temps_actuel(self):   
        #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
        #-- DEBUT -- Heure,Minute,Seconde
        tt = time.time()
        system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
        print(("Voici l'heure:",system_time))
        return system_time
        #-- FIN -- Heure,Minute,Seconde
    #---------------------------------------------

    def temps_actuel_update(self, *args):
        self.Time_Horloge = MaDisposition.temps_actuel(self)
    
class CryptoWatchApp(App):

    def on_start(self):
        pass
    
    def on_stop(self):
        pass
    
    def build(self):       
        return MaDisposition()
    
if __name__ == "__main__":
    CryptoWatchApp().run()
