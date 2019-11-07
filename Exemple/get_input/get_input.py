#AIDES: https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget

from tkinter import *
fenetre=Tk()

#----------------------------------------Zone de Recherche Manuel----------------------------------------
#Bar de Recherche
#Fonction permettant de recuperer la valeur écrite dans la bar de recherche par l'Utilisateur
def recuperation_input():
    Paire_Selectionee=textBox.get("1.0","end-1c")
    print(Paire_Selectionee)

Exemple_Paires = Label(fenetre, text= "Effectué une Recherche \n Ex: XLM-EUR")
Exemple_Paires.pack()
textBox=Text(fenetre,height=2, width=13)
textBox.pack()
Button(fenetre, height=1, width=13, text="Go!",command=lambda: recuperation_input()).pack()
#command=lambda: recuperation_input() >>> just means do this when i press the button
#----------------------------------------Zone de Recherche Manuel----------------------------------------


mainloop()
