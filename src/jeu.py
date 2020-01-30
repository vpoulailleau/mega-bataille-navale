from Carte import *

class Jeu:
    
    def __init__(self):
        self.carte_perso = Carte()
        self.carte_adversaire = Carte()
    
    def recevoir_tir(self, x, y):
        pass
    
    def placer_navire(self, x, y, z, sens, name):
        pass

    def recevoir_tir(self, x, y):
        pass

    def parse_message(self, trame):
        if trame[0] == 2:
            # Reception d'un tir
            x = trame[1]
            y = trame[2]
            return (x,y)
            
