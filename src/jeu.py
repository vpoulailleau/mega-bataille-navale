from carte import *

class Jeu:
    
    def __init__(self):
        self.carte_perso = Carte()
        self.carte_adversaire = Carte()
    
    def placer_navire(self, x, y, z, sens, name):
        pass

    def recevoir_tir(self, x, y):
        etage = 1
        etat_tir = False
        while not etat_tir and etage < 4:
            etat_tir = self.carte_perso.check_ship(x, y, etage)
            etage += 1
        return (etat_tir, etage)

    def parse_message(self, trame):
        if trame[0] == 2:
            # Reception d'un tir
            x = trame[1]
            y = trame[2]
            return (x,y)
        else:
            return (None, None)
