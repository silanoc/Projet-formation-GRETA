#! /usr/bin/env python3
# coding: utf-8

#Gabriel-le, le 20/12/2021
#Commentaires et amélioration du 3/01/2022

from tkinter import *
from typing import TextIO

"""
des claviers possibles à générer.
- Leur nom sera utilisé (directement ou indirectement) plusieurs fois dans le code qui suit
- attention, le nombre de colonne doit être le meme dans chaque ligne
mettre des espace vide au pire
- Ceci est une liste de liste correspondant aux lignes et colonnes.
- On a alors un clavier complétement modulaire
"""

azerty = [["a", "z", "e", "r","t","y", "u", "i", "o", "p"],
          ["q", "s", "d", "f", "g", "h", "j" ,"k", "l", "m"],
          ["w", "x", "c", "v", "b", "n", "", "", "", ""]]

numerique = [[1, 2, 3],
            [4, 5 ,6],
            [7, 8, 9]]



####
# Les classes objets pour faire le clavier
# la touche
# le clavier
####

class Ma_touche(Button):
    """
    Objet qui hérite de la classe bouton.
    Permet de personnaliser les touches
    """
    def __init__(self, ou_afficher,boss=None, text="a"):
        """
        initialise l'objet comme un bouton sans affichage.
        quand on appuit dessus, lance la fonction je_suis_appuye
        """
        Button.__init__(self, ou_afficher,command = self.je_suis_appuye)
        self.valeur = "" #Ce qu'il faut afficher

    def je_suis_appuye(self):
        """
        Lbl_ecrire est un label pour tester l'affichage.
        Il sera à remplacer par la variable lettre_croisie
        self étant la touche, elle devient desactivé et rouge
        """
        #Lbl_ecrire['text'] = self['text'] #ATTENTION remettre pour le test dans la fenetre
        self['state'] = DISABLED
        self['bg'] = 'red'


class Mon_clavier(Canvas):
    """
    Objet qui hérite de la classe Canvas.
    génére et contien les touches du clavier
    c'est un objet contenant des objets (les touches)
    """
    def __init__(self, ou, typeclavier, boss=None):
        "initialise un canvas dans la fenetre "
        self.ou_afficher = ou
        Canvas.__init__(self, self.ou_afficher, boss=None, width=200, height = 150)
        print("instance de Mon_clavier faite")

    def creer_et_positionner_touches(self,typeclavier):
        self.liste_touches_objet = [] # une liste ou on va stocker toutes les touches
        for i in range(len(typeclavier)): #ligne
            for j in range(len(typeclavier[0])): #colonne
                #créer un objet touche
                Touche_provisoire = Ma_touche(self.ou_afficher,Mon_clavier)
                #affiche dans le bouton touche, la valeur de la lettre
                Touche_provisoire.valeur = typeclavier[i][j]
                Touche_provisoire['text'] = Touche_provisoire.valeur
                #Gestion des touche vide
                if Touche_provisoire['text'] == "":
                    Touche_provisoire['state'] = DISABLED  #sinon normal par defaut
                #mettre l'objet touche dans le canvas avec creat_windows et avoir un affichage
                Touche_provisoire_w = self.create_window(j *25, i *30, window = Touche_provisoire)
                #mettre l'objet touche dans la liste pour pouvoir travailler avec plus tard
                self.liste_touches_objet.append(Touche_provisoire)

    def revenir_a_init(self):
        """pour tous les objets de la liste, donc toutes les touches du clavier,
        changer les valeurs pour reprendre des valeurs initiales
        """
        for item in range(len(self.liste_touches_objet)):
            if  self.liste_touches_objet[item]['state'] == DISABLED : #si la touche est désactivé
                self.liste_touches_objet[item]['state'] = NORMAL
                self.liste_touches_objet[item]['bg'] = 'grey95'
                if self.liste_touches_objet[item]['text'] == "":
                    self.liste_touches_objet[item]['state'] = DISABLED  #sinon normal par defaut


###
# Pour générer des claviers
###

if __name__ == '__main__' :

    # Création de la fenêtre
    Fenetre = Tk()
    Fenetre.title("tentative de clavier")
    Fenetre.geometry("400x400")

    lbl = Label(Fenetre, text = "clavier\n\n")
    lbl.pack(side = TOP)

    Clavier = Mon_clavier(Fenetre, azerty)
    Clavier.creer_et_positionner_touches(azerty)
    Clavier.pack()


    # label pour tester les touches
    Lbl_ecrire = Label(Fenetre, text = "ici")
    Lbl_ecrire.pack()

    # pour remettre les touches en position initiales
    Clavier.revenir_a_init()
    Btn_remise_a_zero = Button(Fenetre, text = "mise a zero", command = Clavier.revenir_a_init)
    Btn_remise_a_zero.pack()

    ####
    #Pour lancer le programme
    ####

    Fenetre.mainloop()
