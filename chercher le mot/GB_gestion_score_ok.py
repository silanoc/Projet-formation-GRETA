#! /usr/bin/env python3
# coding: utf-8

#Gabriel-le, le 20/12/2021


####
# 3 fonctions
####


def enregistrer_score(pseudo,score):
    """Méthode pour enregistrer les scores du jeu sur le fichier fichier_score.txt
    arg :
        - pseudo (str) : nom du jouair
        - score (int) : score de la personne
    """
    #ouvrir le fichier, le creer s'il n'existe pas
    try:
        fichier = open('fichier_score.txt', 'a+')  #essayer d'ouvrir en mode ajout
    except FileNotFoundError as e:
        fichier = open('fichier_score.txt', 'x')  #créer le fichier
    except PermissionError as e:
        print("droit de écriture/lecture n'existe pas ")
        exit(2)
    except Exception as e:
        print("erreur d'ouverture du fichier")
        exit(3)
    #concatener pseudo/score
    texte_a_ajouter = f"{pseudo} ; {score}\n" #\n pour gérer les sauts de ligne
    #le mettre dans fichier, à la dernière place
    fichier.write(texte_a_ajouter)
    #fermer le fichier
    fichier.close()
    #ecrire message que ok
    print("un nouveau score vient d'être ajouté")


def afficher_score():
    """Méthode pour afficher le score enregistré dans le ficher fichier_score.txt"""
    #ouvrir le fichier, mettre un message s'il n'existe pas ou est vide !
    try:
        fichier = open('fichier_score.txt', 'r')  #essayer d'ouvrir en mode lecture
    except FileNotFoundError as e:
        message_de_sortie = "Il n'y a pas de score de connu"
        return print(message_de_sortie)
    except PermissionError as e:
        print("droit de écriture/lecture n'existe pas ")
        exit(2)
    except Exception as e:
        print("erreur d'ouverture du fichier")
        exit(3)
    #extraire toutes les lignes du fichier dans un tableau
    total_score = []
    for ligne_fichier in fichier:
        ligne_score = ligne_fichier.split(";",2)
        total_score.append(ligne_score)
    #fermer le fichier
    fichier.close()
    #nettoyer le tableau
    for i in range(len(total_score)):
        intermedaire = total_score[i][1]
        intermedaire=intermedaire[1:-1] #retirer l'espace de devant et le \n
        total_score[i][1] = int(intermedaire) # plus simple de trier des entiers
    #trier le tableau - source https://www.delftstack.com/fr/howto/python/sort-list-of-lists-in-python/
    total_score = sorted(total_score, key=lambda x:x[1], reverse=True)
    #faire le texte a imprimer
    message_de_sortie = ""
    for j in range(len(total_score)):
        ligne_score = f"{j+1} la personne *{total_score[j][0]}* a fait le score de {total_score[j][1]} \n"
        message_de_sortie = message_de_sortie + ligne_score
    #afficher texte de sortie soit vide ou plein
    #print(message_de_sortie)
    return message_de_sortie


def compter_score(score_initial,lettre):
    """Ajoute au score initiale la valeur de la lettre rentrée. Chaque lettre à comem valeur celle du scrabble
    arg :
    - score_initial (int) : score de la personne avant de piocher
    - lettre (str): la lettre trié
    return
    - nouveau score (int)"""
    score_aplhabet = {"A":1, "E":1, "I":1, "L":1, "N":1, "O":1, "R":1, "S":1, "T":1, "U":1 , "D":2, "G":2, "M":2, \
        "B":3, "C":3, "P":3, "F":4, "H":4, "V":4, "J":8, "Q":8, "K":10, "W":10, "X":10, "Y":10, "Z":10}
    lettre = lettre.upper() #comme l'aphabet est en majuscule
    nouveau_score = score_initial + score_aplhabet[lettre]
    return nouveau_score

#####
# pour tester
####

if __name__ == "__main__":
    #pour tester l'enregistrement de score
    enregistrer_score("z", 155)
    enregistrer_score("y", 157)
    enregistrer_score("z", 255)
    enregistrer_score("testtk", 12)

    #pour tester l'affichage des scores
    afficher_score()
    #pour tester le comptage des scores
    print(compter_score(5,'r'))