from random import *
import time
import sys, os

#Python 3
#encoding utf-8

"""
autaire : Gabriel-le
date : décembre 2021
Jeu de trouver le mot développé en mode console et objet lors de la formation
"""

######
# 2 objets : Vue et Stock_de_variables
#####


class Vue():
	"""Objet qui gère :
	- les affichages des différentes vues du jeu
	- les demandes de choix pour passer d'une vue à l'autre
	"""

	def __init__(self):
		"""En s'initialisant, créer l'objet varibles et lance des opérations dedans"""
		self.mes_variables = Stock_de_variables()
		self.mes_variables.active_liste_de_mot()
		# Quelques variables pour l'affichage
		self.taille = 90 # tailel sur laquelle on fait l'affichage
		self.ligne_pleine = "_" * self.taille

	def vue_intro(self):
		"""
		La première qui s'affiche. C'est le menu principal d'entrée du programme.
		"""
		self.efface_console()

		titre_intro = f"{self.mes_variables.titre_du_jeu} - fenêtre principale"
		message_intro = "bienvenux sur cette superbe application en python console."
		message_input = """Que voulez vous faire :  \n \
			- lire les règles (taper 1) \n \
			- jouer avec règlage (taper 2)\n\
			- jouer rapidement (taper 3)\n\
			- lire les scores (taper 4)\n\
			- quitter (taper Q ou q)\n\
		"""
		self.zone_de_titre(titre_intro)
		print(self.ligne_avec_texte(message_intro, self.taille))
		user_answer = "a"
		user_answer = input(self.ligne_avec_texte(message_input,self.taille))
		while user_answer != "Q":
			menu = {"1":self.vue_regle, "2":self.vue_demande_pseudo,
			"3":self.preparation_rapide, "4":self.vue_score,
			"q":self.fin, "Q":self.fin}
			menu.get(user_answer,self.passer)()
			user_answer=input(message_input)

	def vue_regle(self):
		"""
		Affiche les règles et retourne au menu principal
		"""
		self.efface_console()
		titre_regle = f"{self.mes_variables.titre_du_jeu} - les règles du jeu"
		message_regle ="""Vous connaissez les règles par coeur. Donc en latin de cuisine : \n\
		Hac ita persuasione reducti intra moenia bellatores obseratis undique portarum aditibus,\n\
		propugnaculis insistebant et pinnis, congesta undique saxa telaque habentes in promptu, \n\
		ut si quis se proripuisset interius, multitudine missilium sterneretur et lapidum"""
		self.zone_de_titre(titre_regle) #affiche le titre
		print(message_regle)
		print (self.ligne_pleine)
		user_answer = "a"
		message_input = "appuyer sur entrer pour revenir au démarage\n"
		user_answer = input(message_input)

	def vue_zone_de_jeu(self):
		"""la zone de jeu au sens strict"""
		self.efface_console()

		titre_jeu = f"{self.mes_variables.titre_du_jeu} - ici on joue"
		self.zone_de_titre(titre_jeu) #affiche le titre

		#print(f"Debug : Le mot à trouver vient de la catégorie : {self.mes_variables.liste_categorie[self.mes_variables.numero_categorie]}")
		print("le mot à trouver : ")
		self.mes_variables.lettreconnues = "_"*len(self.mes_variables.mot_a_trouver)
		print(self.mes_variables.lettreconnues)
		print("\n#- - - -#\n")

		#la partie en elle meme
		partie = self.mes_variables.mecanisme_central()

		if partie == True :
			self.vue_victoire()
		else :
			self.vue_defaite()

	def vue_victoire(self):
		"""
		Affiche que l'on a gagné,
		enregistre le score et retour au menu"""
		self.efface_console()

		titre_victoire = f"{self.mes_variables.titre_du_jeu} - Victoire"
		self.zone_de_titre(titre_victoire)
		l1 = f"Et une réussite pour {self.mes_variables.pseudo_user}."
		l2 = f"La partie a été résolue en {self.mes_variables.nb_tentative} coups,"
		l3 = f"ce qui donne un score de {self.mes_variables.score} points."
		print (self.ligne_avec_texte(l1))
		print (self.ligne_avec_texte(l2))
		print (self.ligne_avec_texte(l3))
		print (self.ligne_pleine)

		self.mes_variables.enregistrer_score(self.mes_variables.pseudo_user, self.mes_variables.score)
		time.sleep(3)
		self.vue_intro()

	def vue_defaite(self):

		self.efface_console()

		titre_defaite = f"{self.mes_variables.titre_du_jeu} - Défaite"
		self.zone_de_titre(titre_defaite)
		l1 = f" "
		l2 = f"Perdu, mais on peut rejouer ?"
		l3 = f" "
		print (self.ligne_avec_texte(l1))
		print (self.ligne_avec_texte(l2))
		print (self.ligne_avec_texte(l3))
		print (self.ligne_pleine)

		time.sleep(3)
		self.vue_intro()

	def vue_demande_pseudo(self):
		"""
		Demande le pseudo de la personne, puis va vers le choix de categorie
		"""
		self.efface_console()
		print("Notre amix l'ordinateur aime savoir qui joue avec lui.")
		self.mes_variables.pseudo_user = input("Merci de donner un pseudo. Pas défaut se sera jouair\n")
		if len(self.mes_variables.pseudo_user) == 0:
			self.mes_variables.pseudo_user = "jouair"
		print(f"merci {self.mes_variables.pseudo_user}")
		self.vue_demande_categorie()

	def vue_demande_categorie(self):
		"""
		Demande la catégorie de mot, puis va vers la zone de jeu
		"""
		self.efface_console()
		print(f"""Dans ce jeu, al y a plusieurs catégorie de mot possible.
		{self.mes_variables.pseudo_user}, de quelle catégorie viendra la mot à trouver ?""")
		possible = []
		[possible.append(self.mes_variables.liste_categorie[item][0]) for item in range(len(self.mes_variables.liste_categorie))]
		print(possible)
		reponse_categorie = "a"
		while reponse_categorie not in ["0","1","2"] :
			reponse_categorie = input("Quelle catégorie ? Entre 0 et 2 \n")
		self.mes_variables.numero_categorie = int(reponse_categorie)
		self.mes_variables.tirage_mot()
		self.vue_zone_de_jeu()

	def preparation_rapide(self):
		""" choisie au hazard un mot dans une catégorie au hasard.
		attribuer un pseudo pour les score
		améne à la zone de jeu au sens strict"""
		self.mes_variables.theme_rapide()
		self.mes_variables.tirage_mot()
		self.mes_variables.pseudo_user = "jouair"
		self.vue_zone_de_jeu()

	def vue_score(self):
		self.efface_console()
		print("les scores")
		tous_les_scores = self.mes_variables.afficher_score()
		print(tous_les_scores)

	def vue_pas_pret(self):
		"""
		Le truc qui ne devrait pas être utilisé ! Mais utile pour préparer les enchainements d'écrans
		"""
		self.efface_console()
		print (self.ligne_pleine)
		message_pas_pret = "Cette partie n'est pas opérationnelle. Il faut revenir une autre fois"
		print(message_pas_pret)
		print (self.ligne_pleine)
		time.sleep(3)
		self.vue_intro()

	def efface_console(self):
		"""pour nettoyer la console entre chaque vue, et avoir quelque chose de propre"""
		if sys.platform.startswith("win"): #si windows
			os.system("cls")
		else :
			os.system("clear")

	def passer(self):
		"""Pour gérer les réponses non-valides lors input"""
		pass

	def fin(self):
		"""Pour quitter le script"""
		self.efface_console()
		print (self.ligne_pleine)
		message_fin = "Merci d'avoir utilisé mon programme. A une prochaine fois."
		print(message_fin)
		print (self.ligne_pleine)
		exit()

	def ligne_avec_texte(self, texte, total = 90):
		espace = " " * (total - len(texte)-5)
		ligne = f"| {texte} {espace} |"
		return ligne

	def zone_de_titre(self,titre):
		print(self.ligne_pleine)
		print(self.ligne_avec_texte(titre))
		print(self.ligne_pleine)


class Stock_de_variables():
	def __init__(self):
		self.score = 0
		self.nb_tentative = 0
		self.nb_echec = 0
		self.nb_tentative_autorise = 0
		self.lst_lettre_teste = []
		self.mot_a_trouver = ""
		self.lettre_propose = ""
		self.pseudo_user = ""
		self.numero_categorie = ""
		self.liste_categorie = []
		self.lettre_a_utiliser = ["a", "z", "e", "r","t","y", "u", "i", "o",
								"p","q", "s", "d", "f", "g", "h", "j" ,"k", "l",
								 "m","w", "x", "c", "v", "b", "n"]
		self.lettre_deja_utilise = []
		self.titre_du_jeu = "Trouver le mot"

	def active_liste_de_mot(self):
		self.pays = [["pays"],["france", "italie", "allemagne", "chine", "maroc", "algerie", "tunisie", "belgique"]]
		self.sport = [["sport"],["foot", "kayak", "roller", "accrobranche", "kendo", "parapente", "cyclisme"]]
		self.langague = [["langage informatique"],["python", "ada", "java", "bash", "delphi", "assembleur", "html"]]
		self.liste_categorie = [self.pays, self.sport, self.langague]

	def choisir_theme(self):
		pass

	def tirage_mot(self):
		self.mot_a_trouver = self.liste_categorie[self.numero_categorie][1][randint(0,len(self.liste_categorie[self.numero_categorie])-1)]

	def theme_rapide(self):
		self.numero_categorie = randint(0,len(self.liste_categorie)-1)

	def mecanisme_central(self):
		fini = False
		self.nb_tentative = 0
		self.nb_echec = 0
		self.nb_tentative_autorise = 8
		self.score = 0
		self.lettre_a_utiliser = ["a", "z", "e", "r","t","y", "u", "i", "o",
								"p","q", "s", "d", "f", "g", "h", "j" ,"k", "l",
								 "m","w", "x", "c", "v", "b", "n"]
		self.lettre_deja_utilise = []
		self.score_aplhabet = {"a":1, "e":1, "i":1, "l":1, "n":1, "o":1, "r":1, "s":1, "t":1, "u":1 , "d":2, "g":2, "m":2,"b":3, "c":3, "p":3, "f":4, "h":4, "v":4, "j":8, "q":8, "k":10, "w":10, "x":10, "y":10, "z":10}
		while fini == False:
			# vide l'écran, réinitilise les varibles, fait l'affichage de base
			Vue.efface_console(self)
			print(f"Debug : Le mot à trouver vient de la catégorie : {self.liste_categorie[self.numero_categorie][0]}")

			print("le mot à trouver :")
			print(self.lettreconnues)
			self.nb_tentative += 1
			print(f"Les lettres non utilisées sont : {self.lettre_a_utiliser}")
			print(f"Les lettres déjà demandées sont : {self.lettre_deja_utilise}")

			# demander de choisir la lettre avec input
			while self.lettre_propose not in self.lettre_a_utiliser:
				self.lettre_propose = input("Quelle une lettre voulez vous tenter ? appyuez sur entrer pour la valider. \n")

			# actualiser les tableaux de lettres possibles/impossibles
			self.lettre_deja_utilise.append(self.lettre_propose)
			self.lettre_a_utiliser.remove(self.lettre_propose)

			# test si la lettre est bonne
			if self.lettre_propose in self.mot_a_trouver:
				for i in range(len(self.mot_a_trouver)):
					if self.mot_a_trouver[i] == self.lettre_propose:
						self.lettreconnues = self.lettreconnues[:i]+str(self.lettre_propose)+self.lettreconnues[i+1:]
						print(self.lettreconnues)
						self.score = self.compter_score(self.score, self.lettre_propose)
						print(f" score : {self.score}")
						if self.mot_a_trouver == self.lettreconnues:
							victoire = True
							fini = True
			else :
				self.nb_echec += 1
				print (f"faux. nb coup {self.nb_tentative}. {self.nb_echec} erreurs sur {self.nb_tentative_autorise}")
				time.sleep(1)
				if self.nb_echec == self.nb_tentative_autorise:
					victoire = False
					fini = True
		return victoire

	def compter_score(self, score_initial, lettre):
		"""Ajoute au score initiale la valeur de la lettre rentrée. Chaque lettre a comme valeur celle du scrabble
		arg :
		- score_initial (int) : score de la personne avant de piocher
		- lettre (str): la lettre trié
		return
		- nouveau score (int)"""
		#lettre = lettre.upper() #comme l'aphabet est en majuscule
		nouveau_score = score_initial + self.score_aplhabet[lettre]
		return nouveau_score

	def enregistrer_score(self, pseudo, score):
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
		texte_a_ajouter = f"{self.pseudo_user} ; {self.score}\n" #\n pour gérer les sauts de ligne
		#le mettre dans fichier, à la dernière place
		fichier.write(texte_a_ajouter)
		#fermer le fichier
		fichier.close()
		#ecrire message que ok
		print("un nouveau score vient d'être ajouté")

	def afficher_score(self):
		"""Méthode pour afficher le score enregistré dans le ficher fichier_score.txt"""
		#ouvrir le fichier, mettre un message s'il n'existe pas ou est vide !
		try:
			fichier = open('fichier_score.txt', 'r')  #essayer d'ouvrir en mode lecture
		except FileNotFoundError as e:
			message_de_sortie = "Il n'y a pas de score de connu"
			return message_de_sortie
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
		return message_de_sortie

########################
# déclancher le script
########################

def main():
	mes_vues = Vue()
	mes_vues.vue_intro()

if __name__ == "__main__":
	main()
else:
	pass