#! /usr/bin/env python3
# coding: utf-8

from tkinter import *
from PIL import *
from PIL import Image, ImageTk, ImageFilter

from random import *

"""
Version d'entrainement, V3.
avec des objets
Affiche 8 zones d'images pouvant chacune à la fois changer de dos à lettre
"""

""" sources images
https://commons.wikimedia.org/wiki/File:Wiki_puzzle.svg
https://commons.wikimedia.org/wiki/Category:Alphabet_by_Marie_Andersson
"""

# Stockage des images sous forme de dico
dico_image = {0 : "200px-Wiki_puzzle.svg.png",
              "a" : "A_(24596316916).jpg",
              "e" : "E_(24254739289).jpg",
              "g" : "G_(24540269861).jpg",
              "m" : "M_(24642890385).jpg",
              "o" : "O_(24659637066).jpg",
              "r" : "R_(24318162109).jpg",
              "v" : "V_(24452091420).jpg"}

# dico des zones d'affichage
# [ligne, colonne, image, état]
dico_zone = {0 : [0, 0, "g", False],
            1 : [0, 1, "a", False],
            2 : [0, 2, "m", False],
            3 : [0, 3, "e", False],
            4 : [1, 0, "o", False],
            5 : [1, 1, "v", False],
            6 : [1, 2, "e", False],
            7 : [1, 3, "r", False]}

taille_dico_zone = len (dico_zone)

class Mon_image():
    """objet image, qui affiche soit une lettre soit le dos du puzzle"""
    def __init__(self, nom, ou):
        self.image = dico_zone[nom][2]
        self.etat = dico_zone[nom][3]
        self.PhotoLabel = Label(ou)
        self.PhotoLabel.grid(row = dico_zone[nom][0], column = dico_zone[nom][1])
        if self.etat == False:
            Zone_Puzzle.affichage(0, self.PhotoLabel)
        else:
            Zone_Puzzle.affichage(self.image, self.PhotoLabel)

    def affiche_dos(self):
        if self.etat == False:
            Zone_Puzzle.affichage(0, self.PhotoLabel)

    def affiche_lettre(self):
        if self.etat == True:
            Zone_Puzzle.affichage(self.image, self.PhotoLabel)

class Zone_Puzzle():
    def __init__(self, ou):
        self.ouafficher = ou
        self.creer_zone_lettre()


    def affichage(cle_image, PhotoLabel):
        #ouvre un image issus du dictionnaire et l'affiche dans le label demandé
        #photolabel = zone d'affichage
        global image_puzzle
        ImageOpened = Image.open(dico_image[cle_image])
        image_puzzle = ImageTk.PhotoImage(ImageOpened)
        PhotoLabel.configure(image=image_puzzle)
        PhotoLabel.image = image_puzzle

    def creer_zone_lettre(self):
        """créer tous les objet lettre dans sa zone dédié"""
        global liste_objet_lettre
        self.liste_objet_lettre = []
        for i in range(taille_dico_zone):
            i = Mon_image(i, self.ouafficher)
            self.liste_objet_lettre.append(i)

        # Les deux boutons de commande
        Frm_bouton = Frame(self.ouafficher).grid(row = 1, column = 0)
        btn_dos = Button(Frm_bouton , text = "RAZ", command = self.tous_dos)
        btn_game = Button(Frm_bouton, text = "montrer 1 lettre", command = self.lettre_alea)
        btn_dos.grid(row = 3, column = 0)
        btn_game.grid(row = 3, column = 1)

    def tous_dos(self):
        """ fonction appelé par le bouton RAZ pour mettre toutes les cartes face caché"""
        for image in self.liste_objet_lettre :
            image.etat = False
            image.affiche_dos()

    def lettre_alea(self):
        list_possible = []
        #chercher les images de dos
        for image in self.liste_objet_lettre :
            if image.etat == False :
                list_possible.append(image)
        if len(list_possible) > 0:
            alea = randint(0,len(list_possible)-1)
            list_possible[alea].etat = True
            list_possible[alea].affiche_lettre()


if __name__ == "__main__":
    Fenetre = Tk()

    # Le frame contenant les zones d'affichage nommé PhotoLabel[nb]
    Frm_puzzle = Frame(Fenetre).grid(row = 0, column = 0)

    puzzle = Zone_Puzzle(Frm_puzzle)

    # Afficher les cases en position initiale
    puzzle

    Fenetre.mainloop()

