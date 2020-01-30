from case import *

class Navire:
    def __init__(self, longueur, largeur, nom):
        self.longueur = longueur
        self.largeur  = largeur
        self.nom      = nom
        self.cases    = []

    def test_impact(self, x, y, z):
        for index, case in enumerate(self.cases):
            if case.x == x and case.y == y and case.z == z:
                self.cases[index].impact = True
                return True
        return False    


    def set_position(self, x, y, z, sens):
        pass

