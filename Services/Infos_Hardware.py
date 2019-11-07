#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PYTHON 3.x EDITION
#AIDES: https://pythonconverter.com/

#AIDES: https://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-sage-e-g-57-on-linux
#AIDES: https://stackoverflow.com/questions/10585978/linux-command-for-percentage-of-memory-that-is-free
#AIDES: https://docs.python.org/2/library/commands.html


import os
import sys
import datetime
import time
from nettoyage_du_cache import clear_cache


import io
import subprocess


def CPU_usage():
    #Charge CPU
    global UtilisationCPU

    LectureCommande0=subprocess.getoutput("top -bn 1 | awk 'NR>7{s+=$9} END {print s/4}'")  #On execute cette commande pour Obtenir le resultat depuis le sysytem sans passer par un programme tièrce
    UtilisationCPU = "Utilisation du Processeur: " + LectureCommande0 + " %"                #Enregistrement de la Variable reçu et Mise en forme
    print(UtilisationCPU)                                                                   #Affichage des nouvelles données reçu dans la console

    return UtilisationCPU                                                                   #Retourne les valeurs pour une prochaine utilisation.

def CPU_temp():
    #Temperature du CPU/SoC
    global tk_cputemp
        #f = open("/sys/class/thermal/thermal_zone0/temp")
        #t = f.readline ()
        #cputemp = "CPU temp: "+t
    cputemp = subprocess.getoutput("vcgencmd measure_temp")                                 #Obtention de la temperature du Processeur RPI
    print(("Temperature du Processeur: "+ cputemp))                                         #Affichage de la temperature du Processeur RPI obtenue

    #--
    tk_cputemp        = "Temperature du Processeur: " + cputemp                             #Mise en forme pour l'affichage sous Tkinter
    #--

    return tk_cputemp                                                                       #Retourne la valeur Mise en forme pour Tkinter

def SoC_info():
    global mesure_voltage
    global memoire_processeur
    global memoire_gpu

    #Voltage utilisé par le Socket CPU/GPU
    LectureCommande1=subprocess.getoutput("vcgencmd measure_volts core")                    #Obtention de la Tension utilise par le Socket CPU/GPU
    mesure_voltage = "Tension utilisé par l'ensemble CPU/GPU: " + LectureCommande1          #Enregistrement des Informations dans une Variable
    print(mesure_voltage)                                                                   #Affichage des informations dans la console

    #Indication de la Mémoire Vive alouée pour le Processeur
    LectureCommande2=subprocess.getoutput("vcgencmd get_mem arm")                           #Obtention de la memoire vive alouee pour le CPU
    memoire_processeur = "Mémoire Vive alouée pour le Processeur: " + LectureCommande2      #Enregistrement de cette information dans une variable
    print(memoire_processeur)                                                               #Affichage de l'information dans la console

    #Indication de la Mémoire Vive alouée pour le Processeur Graphique
    LectureCommande3=subprocess.getoutput("vcgencmd get_mem gpu")                           #Obtention de la memoire vive alouee pour le GPU
    memoire_gpu = "Mémoire Vive alouée pour le Processeur Graphique: " + LectureCommande3   #Enregistrement de l'information dans une variable
    print(memoire_gpu)                                                                      #Affichage de cette information dans la console

    return mesure_voltage,memoire_processeur,memoire_gpu                                    #Toutes les Informations sont retournees pour Traitement par Tkinter

def MEM_info():
    #Charge Memoire Vive
    global MemoireUtilise
    LectureCommande4=subprocess.getoutput("free | grep Mem | awk '{print $3/$2 * 100.0}'")  #Obtention de la memoire utilise par le Systeme
    MemoireUtilise = "Memoire Vive Utilise: " + LectureCommande4 + " %"                     #Enregistrement de cette information
    print(MemoireUtilise)                                                                   #Affichage de cette information

    return MemoireUtilise                                                                   #Cette information est retournee a Tkinter


if __name__ == "__main__":
    clear_cache()           #Nettoyage du Cache Python.
    CPU_usage()             #Obtention du Niveau d'utilisation du Processeur.
    CPU_temp()              #Obtention de la Temperature du Processeur.
    SoC_info()              #Obtention d'information par rapport au Couple CPU/GPU.
    MEM_info()              #Obtention d'information par rapport à la Memoire Vive.
