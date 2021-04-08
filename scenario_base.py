from scenario_bdd import *
from random import *

epoque=input("Veuillez choisir votre époque : 1 - médiéval fantastique , 2 - début année 20, 3 - contemporain, 4 - cyberpunk, 5 - post apocalypse, 6 - space opéra")
nbphrase=input("Nombre de phrase à générer")

for i in range(int(nbphrase)):
    #choix perso 1
    if (int(epoque)==1):
        choixperso1=persomedieval[randint(0,len(persomedieval)-1)]
    if (int(epoque)==2):
        choixperso1=persodebutvingt[randint(0,len(persodebutvingt)-1)]
    if (int(epoque)==3):
        choixperso1=persocontenporain[randint(0,len(persocontenporain)-1)]
    if (int(epoque)==4):
        choixperso1=persocyberpunk[randint(0,len(persocyberpunk)-1)]
    if (int(epoque)==5):
        choixperso1=persopostapocalypse[randint(0,len(persopostapocalypse)-1)]
    if (int(epoque)==6):
        choixperso1=persospaceopera[randint(0,len(persospaceopera)-1)]

    
    #pile ou face interaction perso ou lieu
    choixtypeinteraction=randint(0,1)

    #choix interaction
    if choixtypeinteraction==0:
        choixinteraction=interactionperso[randint(0,len(interactionperso)-1)]
    if choixtypeinteraction==1:
        choixinteraction=interactionlieux[randint(0,len(interactionlieux)-1)]

    #choix perso 2
    if (int(epoque)==1):
        choixperso2=persomedieval[randint(0,len(persomedieval)-1)]
    if (int(epoque)==2):
        choixperso2=persodebutvingt[randint(0,len(persodebutvingt)-1)]
    if (int(epoque)==3):
        choixperso2=persocontenporain[randint(0,len(persocontenporain)-1)]
    if (int(epoque)==4):
        choixperso2=persocyberpunk[randint(0,len(persocyberpunk)-1)]
    if (int(epoque)==5):
        choixperso2=persopostapocalypse[randint(0,len(persopostapocalypse)-1)]
    if (int(epoque)==6):
        choixperso2=persospaceopera[randint(0,len(persospaceopera)-1)]

    #choix lieu
    if (int(epoque)==1):
        choixlieu=lieumedieval[randint(0,len(lieumedieval)-1)]
    if (int(epoque)==2):
        choixlieu=lieudebutvingt[randint(0,len(lieudebutvingt)-1)]
    if (int(epoque)==3):
        choixlieu=lieucontenporain[randint(0,len(lieucontenporain)-1)]
    if (int(epoque)==4):
        choixlieu=lieucyberpunk[randint(0,len(lieucyberpunk)-1)]
    if (int(epoque)==5):
        choixlieu=lieuapocalypse[randint(0,len(lieuapocalypse)-1)]
    if (int(epoque)==6):
        choixlieu=lieuspaceopera[randint(0,len(lieuspaceopera)-1)]

    #écrire la phrase
    if choixtypeinteraction==0:
        print(choixperso1+" "+choixinteraction+" "+choixperso2)
    if choixtypeinteraction==1:
        print(choixperso1+" "+choixinteraction+" "+choixlieu)
        
