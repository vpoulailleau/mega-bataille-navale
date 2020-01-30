from navire import *

class Carte:
    def __init__(self):
        self.navires = []

    def check_ship(self, x, y, z):
        for navire in self.navires:
            if navire.test_impact(x, y, z):
                return True
        return False
        
    def positionner_navire(self, x, y, z, sens, name):
        pass