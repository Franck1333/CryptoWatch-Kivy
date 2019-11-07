#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AIDES: https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

from PIL import Image                                       #Bibliotheque permettant la manipulation de fichier IMAGE

from nettoyage_du_cache import clear_cache                  #Bibliotheque permettant de nettoyer les fichiers cache PYTHON
import getpass                                              #On importe la blibliotheque "getpass"
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

def Re_tailler_une_image():
    basewidth = 300                                                                                             #Saisir la taille de base dont l'image doit etre rogner
    img = Image.open('/home/'+USERNAME+'/CryptoWatch-Kivy/Services/Telechargements/Fear_Greed_Index.png')      #On ouvre l'image concernee
    wpercent = (basewidth/float(img.size[0]))                                                                   #Calcule en pourcentage de la redimmension
    hsize = int((float(img.size[1])*float(wpercent)))                                                           #Calcule de la hauteur de l'image pour sa redimmension
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)                                                        #Traitement de l'image
    img.save('/home/'+USERNAME+'/CryptoWatch-Kivy/Services/Telechargements/Fear_Greed_Index_retailler.png')    #Enregistrement de la Modification apporte a l'image concernee

def Re_tailler_une_image_Donner(Base_de_Taille, Chemin_Image_Source , Chemin_Image_Modifiee):
    basewidth = Base_de_Taille
    img = Image.open(Chemin_Image_Source)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(Chemin_Image_Modifiee)


if __name__ == "__main__":
 clear_cache()          #Nettoyage du Cache Python.
 #Re_tailler_une_image() #Permet d'effectuer un re-taillement d'une image trop grande (ou trop petite).
 #Re_tailler_une_image_Donner(300, '/home/'+USERNAME+'/CrytpoView_Projet/Services/Telechargements/Fear_Greed_Index.png' , '/home/'+USERNAME+'/CrytpoView_Projet/Services/Telechargements/Fear_Greed_Index_retailler.png')
