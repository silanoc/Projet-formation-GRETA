#! /usr/bin/env python3
# coding: utf-8

#-------------------------------------------------------------------------------
# Name:        Exercie de fenetre graphique autour d'un jeu de carte
# Author:      En groupe (Abderrahim, Chaima, Gabriel-le) : class et version texte
#               puis fini en solo (Gabriel-le) : version graphique
# Created:     06/01/2022
#-------------------------------------------------------------------------------

from random import *
from tkinter import *

from PIL import *
from PIL import Image, ImageFilter, ImageTk

""" exercice d'application de la formation.
Jeu de carte en objet et TK
les images de cartes sont issues de https://www.hegerm.ch/adr_im_cards.html, la carte de fond est une de ces cartes coloriée.

la v1 avait la fentre/tk dans le main
ici, la fentre/tk de jeu est dans une class et on joue dans une instance. Nécessite deux variable globale de plus !
"""

class CJeuDeCartes():
    """classe represantant un jeu de cartes"""
    def __init__(self):
        """constructeur de notre jeu de 52 cartes :
        - crée 52 instances de carte en leur donnant les valeurs et formes issue de liste incluse
        - stock ces cartes dans une liste, carte_totale, qui sera utilisée partout après
        """

        self.valeur_carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
        self.forme_carte = ["carreau", "coeur", "pique", "trefle"]
        self.carte_totale = []
        for i in self.valeur_carte:
            for j in self.forme_carte:
                macarte = Cartes(i, j)
                self.carte_totale.append(macarte)

    def melange_carte(self):
        """se contente de melanger les cartes incluse dans carte_totale"""
        shuffle(self.carte_totale)

    def afficher_tout(self):
        """pour toutes les cartes dans carte_totale :
        - utilise leur méthode nom_carte
        - mettre cette valeur dans la StringVar le_texte pour l'afficher dans le label qui va bien
        - affiche les images des cartes """

        le_texte.set("")
        for i in range(len(self.carte_totale)):
            # Affiche la version textuelle
            txt_intermediaire = le_texte.get() + self.carte_totale[i].nom_carte() + "\n" # get sert à recupere les données qui sont à la base vides
            le_texte.set(txt_intermediaire)#Set permet de modifier le contenu recuperé par la fonction get qui lié avec la variable txt_intermediaire
            # Affiche la version image
            if mon_jeu.carte_totale[i].visible:
                mon_jeu.carte_totale[i].affiche_image(mon_jeu.carte_totale[i].mon_image, liste_case[i])
            else:
                mon_jeu.carte_totale[i].affiche_image("fond.gif", liste_case[i])


    def melange_et_affiche(self):
        """ pour mélanger les cartes dans carte_totale et les afficher après
        en utilisant les méthodes déjà existante  """
        self.melange_carte()
        self.afficher_tout()

    def tirer_carte(self):
        """ s'il reste des cartes dans la liste, affiche la première et retire la de la liste, car c'est un tirage sans remise"""
        if len(self.carte_totale) > 0 :
            # gestion textuelle
            le_texte.set("")
            text_inter_tirer = le_texte.get() + self.carte_totale[0].nom_carte()
            le_texte.set(text_inter_tirer)
            # gestion graphique
            mon_jeu.carte_totale[-1].visible = False #rend la carte non-visible/de dos
            mon_jeu.carte_totale[0].affiche_image(mon_jeu.carte_totale[0].mon_image, carte_tire)
            self.afficher_tout()
            # retirer la carte du tas / tapis
            #
            del self.carte_totale[0]
        else:
            pass


class Cartes():
    """La classe carte"""
    def __init__(self, valeur, forme):
        """ le constructeur pour la carte avec leur valeur et forme.
        Lui attribue une image .gif"""
        self.valeur = valeur
        self.forme = forme
        dico_correspondance = {(1, "carreau"): "Ad.gif",
                                (2, "carreau"): "2d.gif",
                                (3, "carreau"): "3d.gif",
                                (4, "carreau"): "4d.gif",
                                (5, "carreau"): "5d.gif",
                                (6, "carreau"): "6d.gif",
                                (7, "carreau"): "7d.gif",
                                (8, "carreau"): "8d.gif",
                                (9, "carreau"): "9d.gif",
                                (10, "carreau"): "10d.gif",
                                ("valet", "carreau"): "Jd.gif",
                                ("dame", "carreau"): "Qd.gif",
                                ("roi", "carreau"): "Kd.gif",
                                (1, "coeur"): "Ah.gif",
                                (2, "coeur"): "2h.gif",
                                (3, "coeur"): "3h.gif",
                                (4, "coeur"): "4h.gif",
                                (5, "coeur"): "5h.gif",
                                (6, "coeur"): "6h.gif",
                                (7, "coeur"): "7h.gif",
                                (8, "coeur"): "8h.gif",
                                (9, "coeur"): "9h.gif",
                                (10, "coeur"): "10h.gif",
                                ("valet", "coeur"): "Jh.gif",
                                ("dame", "coeur"): "Qh.gif",
                                ("roi", "coeur"): "Kh.gif",
                                (1, "pique"): "As.gif",
                                (2, "pique"): "2s.gif",
                                (3, "pique"): "3s.gif",
                                (4, "pique"): "4s.gif",
                                (5, "pique"): "5s.gif",
                                (6, "pique"): "6s.gif",
                                (7, "pique"): "7s.gif",
                                (8, "pique"): "8s.gif",
                                (9, "pique"): "9s.gif",
                                (10, "pique"): "10s.gif",
                                ("valet", "pique"): "Js.gif",
                                ("dame", "pique"): "Qs.gif",
                                ("roi", "pique"): "Ks.gif",
                                (1, "trefle"): "Ac.gif",
                                (2, "trefle"): "2c.gif",
                                (3, "trefle"): "3c.gif",
                                (4, "trefle"): "4c.gif",
                                (5, "trefle"): "5c.gif",
                                (6, "trefle"): "6c.gif",
                                (7, "trefle"): "7c.gif",
                                (8, "trefle"): "8c.gif",
                                (9, "trefle"): "9c.gif",
                                (10, "trefle"): "10c.gif",
                                ("valet", "trefle"): "Jc.gif",
                                ("dame", "trefle"): "Qc.gif",
                                ("roi", "trefle"): "Kc.gif"
                                }
        self.mon_image = dico_correspondance[self.valeur, self.forme]
        self.visible = True

    def nom_carte(self):
        """ return les caractéristiques de la carte"""
        text = "je suis la carte : %s de %s" %(self.valeur, self.forme) #%s  le "s" est le string en anglais
        return text

    def affiche_image(self, qui, ou):
        """méthode permattant à l'instance de carte d'afficher son image au bon endroit dans la fenetre"""
        global image_a_afficher
        # ouvrir l'image
        ImageOpened = Image.open(qui)
        # créer l'image et la mettre dans un Label appellé Photolabel
        image_a_afficher = ImageTk.PhotoImage(ImageOpened)
        ou.configure(image = image_a_afficher)
        ou.image = image_a_afficher


class Zone_de_jeu(Tk):
    """class pour gérer l'affichage du jeu"""

    def __init__(self):
        """ toute la conception est dans l'init !"""
        Tk.__init__(self)
        self.title("super jeu de carte en equipe")
        self.geometry("1300x1000")
        self.configure(bg = "#008026")

        """
        - création des boutons dans une frame pour faire "afficher", "melanger", "melanger et affiche" et "tirer"...,
        - label pour afficher le contenu de carte dans carte_totale"""

        #creation d'une frame pour séparer les bouttons et le label dand lbl_afficher
        frm_menu = Frame(self, bg = "#734F96")
        frm_menu.grid(row = 0, column = 0 , padx = 10, pady=10)

        #création des bouttons
        btn_afficher = Button(frm_menu, text = " afficher ", bg = "#3DCEFF", command = mon_jeu.afficher_tout)
        btn_melanger = Button(frm_menu, text = " melanger (pensez à afficher)", bg = "#F5A9B8", command = mon_jeu.melange_carte)
        btn_melangeretaffiche = Button(frm_menu, text = " melanger et affiche ",  bg = "#FFFFFF",command = mon_jeu.melange_et_affiche)
        btn_tirer = Button(frm_menu, text = " tirer ",  bg = "#F5A9B8",command = mon_jeu.tirer_carte)
        btn_raz = Button(frm_menu, text = "Remise à zéro (pensez à afficher)", bg = "#3DCEFF", command = mon_jeu.__init__)

        #création d'une variable le_texte qui sera utilisé dans la classe CJeuDeCartes et dans le label lbl_afficher en utilisant
        #des gets() et set()
        global le_texte
        le_texte = StringVar()

        lbl_afficher = Label(self, bg = "#FFFFFF", textvariable =le_texte)

        btn_afficher.grid(row = 0, column = 0, padx = 15, pady = 7)
        btn_melanger.grid(row = 0, column = 1, padx = 15, pady = 7)
        btn_melangeretaffiche.grid(row = 0, column = 2, padx = 15, pady = 7)
        btn_tirer.grid(row = 0, column = 3, padx = 15, pady = 7)
        btn_raz.grid(row = 0, column = 4, padx = 15, pady = 7)
        lbl_afficher.grid(row = 1, column = 5, padx = 10)

        # pour toutes les images
        frm_plein_de_carte = Frame(self, bg = "#FF8C00")
        global liste_case
        liste_case = []
        # Création des 52 zones d'affichage des cartes et liste pour interagir avec
        for i in range(4):
            for j in range(13):
                lbl_case = Label(frm_plein_de_carte)
                lbl_case.grid(row = i, column = j, padx = 3, pady = 3)
                liste_case.append(lbl_case)
        frm_plein_de_carte.grid(row = 1, column = 0, padx = 10)

        # juste l'endroit pour afficher une image appelé par le bouton "tirer carte"
        frm_tirage = Frame(self)
        global carte_tire
        carte_tire = Label(frm_tirage)
        frm_tirage.grid(row = 3, column = 0, padx = 10, pady = 10)
        carte_tire.grid(row = 0, column = 0)

        self.mainloop()

if __name__ == "__main__":

    """
    - création de l'intance du jeu de carte, et de la fenetre"""

    mon_jeu = CJeuDeCartes()
    zone = Zone_de_jeu()
    #zone2 = Zone_de_jeu() pour lancer une deuxième fenetre quand on ferm la première ! pourquoi pas !

