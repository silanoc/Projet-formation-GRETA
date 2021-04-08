from random import *
1
class Epoque(object):
    #ceci est pour le moment un aide mémoire
    #epoque=input("Veuillez choisir votre époque : 1 - médiéval fantastique , 2 - début année 20, 3 - contemporain, 4 - cyberpunk, 5 - post apocalypse, 6 - space opéra")
    def __init__(self):
        print("coucou")

class Personnage(object):
    "pour définir les personnages à utiliser"
    "liste des possibles"
    medieval=["voleur","assassin","magicien","devin","garde","pèlerin","noble","guilde","troubadour","marchand","roi","monstre","dieu","prêtre","pj","scribe","enfant","gitan","guerrier"]
    debutvingt=["cambrioleur","tueur à gages","savant fou","directeur de cirque","commissaire","adorateur","nnalité","pègre","musicien de jazz","boutiquier","tête couronnée","créature","dieu","médecin","pj","chroniqueur","dilettante","médium","colonialiste"]
    contemporain=["maître-chanteur","terroriste","scientifique","routier","détective privée","secte","milliardaire","organisation criminelle","acteur","firme d'import-export","chef d'état","parapsychologue","informaticien","chirurgien","pj","grand reporteur","top modèle","espion","militaire"]
    cyberpunk=["dealer","solo","scientifique","nomade","flic","secte","corporatiste","gang","rock star","megacorpo","« huile »","androïde","IA","charcudoc","pj","media","netrunner","indic","mercenaire"]
    postapocalypse=["récupérateur","psychopathe","savant fou","traître","milicien","pèlerin","leader","tribu","solitaire","marchand","amazone","mutant","médium","médecin","pj","vieil érudit","enfant","mécano","robot"]
    spaceopera=["pirate","aventurier","scientifique","mercenaire","militaire","organisation","chef de guerre","hors la loi","espion","corporation","dirigeant politique","extraterrestre","télépathe","médecin","pj","technicien","chasseur de prime","pilote","droïde"]
    def __init__(self,epoque):
        if (int(epoque)==1):
            self.occupation=Personnage.medieval[randint(0,len(Personnage.medieval)-1)]
        elif (int(epoque)==2):
            self.occupation=Personnage.debutvingt[randint(0,len(Personnage.debutvingt)-1)]
        elif (int(epoque)==3):
            self.occupation=Personnage.contemporain[randint(0,len(Personnage.contemporain)-1)]
        elif (int(epoque)==4):
            self.occupation=Personnage.cyberpunk[randint(0,len(Personnage.cyberpunk)-1)]
        elif (int(epoque)==5):
            self.occupation=Personnage.postapocalypse[randint(0,len(Personnage.postapocalypse)-1)]
        elif (int(epoque)==6):
            self.occupation=Personnage.spaceopera[randint(0,len(Personnage.spaceopera)-1)]
    def affiche(self):
        print(self.occupation)

class Lieu(object):
    "liste des possibles"
    medieval=["cachot","palais","ville","officine","forêt","hospice","temple","maison close","nef","taverne","sanctuaire","oubliettes","salle du trone","échoppe","mine","antre de dragon","port","province","scriptorium"]
    debutvingt=["bagne","palace","capitale","laboratoire","fête foraine","hôpital","église","tripot","dirigeable","cabaret","cimetière","catacombes","théâtre","armurerie","fabrique","zoo","port","colonie","bibliothèque"]
    contemporain=["prison","grand hôtel","métropole","laboratoire","parc d'attraction","hôpital","secte","casino","paquebot","boite de nuit","morgue","égouts","cinéma","supermarché","centrale nucléaire","grand monument","aéroport","base militaire","médiathèque"]
    cyberpunk=["pénitencier","motel","mégalopole","banque d'organe","terrain vague","asile psychiatrique","néocathédale","salle de jeu","spaciocargo","club","crématorium","égouts","holociné","souk","usine","la Matrice","astroport","QG corporatiste","central informatique"]
    apocalypse=["prison","campement","ghetto","labo miteux","autoroute","dispensaire","ruines","arène","convoi","oasis","cimetière","ancien cinéma","bazar","hangar","salle d'archive","métro","zone irradiée","antre d'un érudit"]
    spaceopera=["bagne","satellite d'accueil","base spatiale","laboratoire","planète","vaisseau-hôpital","vaisseau fantôme","astéroïde de jeu","barge à voile","spaciobar","cryosanctorium","sanctuaire ET","conseil galactique","marché ET","station minière","astre inconnu","spatioport","lune artificielle","champs d'astéroïde"]
    def __init__(self,epoque):
        if (int(epoque)==1):
            self.label=Lieu.medieval[randint(0,len(Lieu.medieval)-1)]
        elif (int(epoque)==2):
            self.label=Lieu.debutvingt[randint(0,len(Lieu.debutvingt)-1)]
        elif (int(epoque)==3):
            self.label=Lieu.contemporain[randint(0,len(Lieu.contemporain)-1)]
        elif (int(epoque)==4):
            self.label=Lieu.cyberpunk[randint(0,len(Lieu.cyberpunk)-1)]
        elif (int(epoque)==5):
            self.label=Lieu.apocalypse[randint(0,len(Lieu.apocalypse)-1)]
        elif (int(epoque)==6):
            self.label=Lieu.spaceopera[randint(0,len(Lieu.spaceopera)-1)]
    def affiche(self):
        print(self.label)

class Interaction_avec_perso(object):
    interaction=["cherche à nuire","demande de l'aide","recherche / poursuit","veut tuer / détruire","veut soudoyer / séduire","veut (se) faire engager ","se fait passer pour","trouve / rencontre","interroge / torture","s'allie / conspire avec"]
    def __init__(self):
        self.label=Interaction_avec_perso.interaction[randint(0,len(Interaction_avec_perso.interaction)-1)]
    def affiche(self):
        print(self.label)

class Interaction_avec_lieu(object):
    interaction=["veut partir / s'évade de","veut cambrioler / profaner","veut visiter / s'introduire dans","veut acheter / se saisir de","veut construire / installer","découvre","veut vendre / se débarrasser de","veut attaquer / détruire","se cacher / errer dans"]
    def __init__(self):
        self.label=Interaction_avec_lieu.interaction[randint(0,len(Interaction_avec_lieu.interaction)-1)]
    def affiche(self):
        print(self.label)

class Phrasesimple(object):
    def __init__(self,epoque):
        #pile ou face interaction perso ou lieu
        choixtypeinteraction=randint(0,1)
        #choix
        if choixtypeinteraction==0:
            p1=Personnage(epoque)
            l1=Lieu(epoque)
            i1=Interaction_avec_lieu()
            self.intitule=p1.occupation+" "+i1.label+" "+l1.label
        if choixtypeinteraction==1:
            p1=Personnage(epoque)
            p2=Personnage(epoque)
            i1=Interaction_avec_perso()
            self.intitule=p1.occupation+" "+i1.label+" "+p2.occupation
    def affiche(self):
        print(self.intitule)
    

class Test(object):
    def test_generer_10_personnages(self):
        for i in range (1,6):
            for j in range(10):
                a=Personnage(i)
                a.affiche()
            print("---")
    def test_generer_10_lieux(self):
        for i in range (1,6):
            for j in range(10):
                a=Lieu(i)
                a.affiche()
            print("---")
    def test_generer_10_interaction_perso(self):
        for i in range (10):
            a=Interaction_avec_perso()
            a.affiche()
    def test_generer_10_interaction_lieu(self):
        for i in range (10):
            a=Interaction_avec_lieu()
            a.affiche()
    def test_generer_10_phrase_simple(self):
        epoque=input("Veuillez choisir votre époque : 1 - médiéval fantastique , 2 - début année 20, 3 - contemporain, 4 - cyberpunk, 5 - post apocalypse, 6 - space opéra")
        for i in range (10):
            a=Phrasesimple(epoque)
            a.affiche()
    
testons=Test()
#testons.test_generer_10_personnages()
#testons.test_generer_10_lieux()
#testons.test_generer_10_interaction_perso()
#print("---")
#testons.test_generer_10_interaction_lieu()
testons.test_generer_10_phrase_simple()
