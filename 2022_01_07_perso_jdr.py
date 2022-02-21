#! /usr/bin/env python3
# coding: utf-8

#Gabriel-le, le 07/01/2022

""" Exercices sur les classes"""


"""Hierarchies des classes :
- Personnage : la plus générique. C'est elle qui doit contenir le maximun de chose qui sera communes à tous. C'est la classe dont toutes les autres hérites.
- Les classes "races" : humain, elfe... sont héritières de Personne"
- Les classes "metiers": magicie, guerreir... n'ont pas d'héritage.
- Les classes Métiers/races ont le double héritage Métiers et Races (et donc de Personnage)"""


class Personnage():
    """La classe de base, avec tous les attributs commun et méthode communes"""
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        self.vie = vie
        self.nom = nom
        self.force = force
        self.endurance = endurance
        self.rapidite = rapidite
        self.intelligence = intelligence
        self.estMort()

    def estMort(self):
        """fonction a utiliser à chaque fois que l'on veut vérifier
        si les personnes impliqués dans une actions peuvent le faire ou pas"""
        if self.vie > 0:
            self.mort = False
        else:
            self.mort = True

    def afficheEtat(self):
        self.estMort()
        if self.mort: #inutile de mettre == True !
            msg = f"{self.nom} est mort !"
        else:
            msg = f"Il reste {self.vie} PV à {self.nom}"
        print(msg)

    def afficheCaracteristique(self):
        msg1 = f"{self.nom} à une force de {self.force}, une endurance de {self.endurance}, une rapidité de {self.rapidite} et une intelligence de {self.intelligence}"
        msg2 = f" {self.nom} est de race : {self.race} et exerce le métier de {self.metier}"
        if self.metier == "magicien":
            msg3 = f"sont nombre de point de magie est de : {self.pointsDeMagie}"
        else:
            msg3 = ""
        print(msg1)
        print(msg2)
        print(msg3)

    def perdVie(self, nbPointsDeViePerdus):
        msg1 = f"{self.nom} subit une attaque, il perd {nbPointsDeViePerdus} points de vie"
        print(msg1)
        self.vie -= nbPointsDeViePerdus
        self.estMort()
        if self.mort:
            msg2 = f"{self.nom} a subi une attaque mortelle !!!"
            print(msg2)

    def gagneVie(self, nbPointVieGagne):
        self.estMort()
        if self.mort == False:
            self.vie += nbPointVieGagne
            msg = f"{self.nom} a été soigné. Ses points de vies valent maintenant {self.vie}"
        else:
            msg = f"{self.nom} ne peut être soigné par Gandalf, car {self.nom} est mort !"
        print(msg)

    def soigne(self, autrePersonnage, pointsDeSoin):
        if self.mort == False and autrePersonnage.mort == False:
            autrePersonnage.vie += pointsDeSoin
            msg = f"{self.nom} soigne {autrePersonnage.nom}. {self.nom} restaure {pointsDeSoin} point de vie."
        elif self.mort == False and autrePersonnage.mort:
            msg = f"{self.nom} ne peut soigner {autrePersonnage.nom} , car {autrePersonnage.nom} est mort !"
        else:
            msg = f"{autrePersonnage.nom} ne peut pas être soigné par {self.nom}, {self.nom} est mort !"
        print(msg)

    def seDeplace(self, pointsDeDeplacement):
        pass

    def attaque(self, autrePersonnage):
        if self.mort == False and autrePersonnage.mort == False:
            autrePersonnage.esquiveAttaque(self)
            if autrePersonnage.esquive == False:
                pointsDeDegats = int(0.6 * self.force)
                autrePersonnage.perdVie(pointsDeDegats)
        else:
            msg = "un des deux perso (ou les deux) est mort. Combat impossible"
            print(msg)

    def esquiveAttaque(self, autrePersonnage):
        #comme la méthode est appelé si les deux person son vivant, pas besoin de le retester
        if int(self.rapidite * 1.2) > autrePersonnage.force:
            self.esquive = True
            msg = f"""{self.nom} esquive l'attaque de {autrePersonnage.nom} le méchant
            calcul de rapidité de {self.nom} : {self.rapidite * 1.2} contre {autrePersonnage.force} pour {autrePersonnage.nom} """
        else:
            self.esquive = False
            msg = f"""{self.nom} ne peut pas esquiver l'attaque de {autrePersonnage.nom} le méchant
            calcul de rapidité de {self.nom} : {self.rapidite * 1.2} contre {autrePersonnage.force} pour {autrePersonnage.nom} """
        print(msg)

####
# les classe "races"
###

class Humain(Personnage):
    """pour la "race" : humain, une des nombreuses dans les terres du milieu"""
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        Personnage.__init__(self, nom, vie, force, endurance, rapidite, intelligence)
        self.race= "humain"

class Hobbit(Personnage):
    """pour la "race" : hobbit, une des nombreuses dans les terres du milieu"""
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        Personnage.__init__(self, nom, vie, force, endurance, rapidite, intelligence)
        self.race= "hobbit"

class Elfe(Personnage):
    """pour la "race" : elfe, une des nombreuses dans les terres du milieu"""
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        Personnage.__init__(self, nom, vie, force, endurance, rapidite, intelligence)
        self.race= "elfe"

####
# les classes "metiers"
###

class Magicien():
    """pour les magiciens, un métier parmi tant d'autre"""
    def __init__(self, magie):
        self.metier = "magicien"
        self.pointsDeMagie = magie

    def faireMagie(self, autrePersonnage, degatmagique):
        """une methode et donc action réservé aux magiciens,
        lancer un sort qui modifie en + ou - les pv d'une personne"""
        msg = "Je viens de lancer un sort"
        print(msg)
        if degatmagique > 0:
            autrePersonnage.perdVie(degatmagique)
        else:
            autrePersonnage.gagneVie(abs(degatmagique))

class Guerrier():
    """pour les guerriers, un métier parmi tant d'autre"""
    def __init__(self):
        self.metier = "guerrier"

class Aventurier():
    """pour les aventuriers, un métier parmi tant d'autre"""
    def __init__(self):
        self.metier = "aventurier"

######
# les classes metier/races
######

class MagicienHumain(Magicien, Humain):
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence, magie):
        Magicien.__init__(self, magie)
        Humain.__init__(self, nom, vie, force, endurance, rapidite, intelligence)

class MagicienElfe(Magicien, Elfe):
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence, magie):
        Magicien.__init__(self, magie)
        Elfe.__init__(self, nom, vie, force, endurance, rapidite, intelligence)

class AventurierHobbit(Aventurier, Hobbit):
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        Aventurier.__init__(self)
        Hobbit.__init__(self, nom, vie, force, endurance, rapidite, intelligence)

class GuerrierHumain(Guerrier, Humain):
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence):
        Guerrier.__init__(self)
        Humain.__init__(self, nom, vie, force, endurance, rapidite, intelligence)



###########
# Zones de test
###########

gollum = AventurierHobbit("Gollum", 10, 7, 20, 8, 25)
gollum.afficheEtat()
gollum.afficheCaracteristique()
print("----")
frodon = AventurierHobbit("Frodon", -7, 11, 12, 8, 29)
frodon.afficheEtat()
frodon.afficheCaracteristique()
print("----")
gandalf = MagicienHumain ("Gandalf", 45, 10, 20, 8, 50, 20)
gandalf.afficheCaracteristique()
print("----")
grand_pas = GuerrierHumain ("Grand pas", 50, 20, 30, 10, 20)
grand_pas.afficheCaracteristique()

print("----")
gollum.perdVie(6)
#gollum.perdVie(6)
print("----")
gandalf.gagneVie(10)
frodon.gagneVie(10)
print("----")
gandalf.soigne(frodon, 10)
gandalf.soigne(gollum, 10)
gollum.afficheEtat()
frodon.soigne(gandalf,10)
print("----")
gandalf.seDeplace(10)
print("----")
gandalf.attaque(gollum)
gollum.attaque(gandalf)
gandalf.attaque(gollum)
gollum.attaque(gandalf)
gollum.afficheEtat()
gandalf.afficheEtat()
gandalf.attaque(gollum)
print("----")
gollum.attaque(gandalf)
frodon.attaque(gollum)
gandalf.attaque(gollum)
print("----")
gandalf.faireMagie(grand_pas, -10)
gandalf.faireMagie(grand_pas, +10)
print("--petit soucis, l'argument autre_personnage peut etre = à self, et un perso peut s'attaquer lui meme !--")
gandalf.soigne(gandalf, 10)
gandalf.attaque(gandalf)

grand_pas.perdVie(50)
grand_pas.afficheEtat()
