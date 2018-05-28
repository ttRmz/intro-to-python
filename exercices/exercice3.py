import random
from random import randint

values = {"7","8", "9", "10", "Valet", "Dame", "Roi", "As"}
colors = {"piques", "carreau", "treffle", "coeur"}

def jeuDeCartes():
    return [(x,y) for x in values for y in colors]

Jeu = jeuDeCartes()

JeuMelange = random.sample(Jeu,32)

def tirageCarte(cartes):
    return cartes[randint(0, 31)]

def partie():
    input("Appuyez sur entrer pour tenter votre chance")
    tour = tirageCarte(JeuMelange)
    if(tour[0] == 'Roi'):
        print("Victoire :) vous avez tiré la carte : " + tour[0] + " de " + tour[1])
    else:
        print("Défaite :( vous avez tiré la carte : " + tour[0] + " de " + tour[1])
    partie()

partie()