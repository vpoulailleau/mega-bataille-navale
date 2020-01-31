import sys

sys.path.insert(1, 'src')

from jeu import *

def test_recevoir_tir(self):
    jeu = src.Jeu()
    navire = Navire(3, 1, "AlainBernard")
    jeu.carte_perso.navires.append(navire)
    jeu.carte_perso.navires[0].cases.append(Case(11, 5, 1))
    jeu.carte_perso.navires[0].cases.append(Case(10, 5, 1))
    jeu.carte_perso.navires[0].cases.append(Case(9, 5, 1))

    assert jeu.recevoir_tir(-50, 20) == False
    assert jeu.recevoir_tir(-50, -20) == False
    assert jeu.recevoir_tir(50, 20) == False
    assert jeu.recevoir_tir(50, -20) == False
    assert jeu.recevoir_tir(5.5, 2.3) == False
    assert jeu.recevoir_tir(-5.5, -2.3) == False
    assert jeu.recevoir_tir(0, 0) == False
    assert jeu.recevoir_tir(4, 5) == False
    assert jeu.recevoir_tir(a, b) == False
    assert jeu.recevoir_tir(11, 5) == True

def test_parse_message(self):
    jeu = Jeu()
    trame = []
    trame[0] = 2
    trame[1] = 1
    trame[2] = 5
    assert jeu.parse_message(trame) == True
    trame1 = []
    trame1[0] = 0
    trame1[1] = 1
    trame1[2] = 5
    assert jeu.parse_message(trame1) == False
    trame2 = []
    trame2[0] = 2
    trame2[1] = 0
    trame2[2] = 5
    assert jeu.parse_message(trame2) == False
    trame3 = []
    trame3[0] = 2
    trame3[1] = 5
    trame3[2] = 17
    assert jeu.parse_message(trame3) == False
    trame4 = []
    trame4[0] = 2
    trame4[1] = 18
    trame4[2] = 0
    assert jeu.parse_message(trame4) == False
    trame5 = []
    trame5[0] = -5
    trame5[1] = 18
    trame5[2] = 0
    assert jeu.parse_message(trame4) == False
    trame5 = []
    trame5[0] = 2
    trame5[1] = -5
    trame5[2] = 15
    assert jeu.parse_message(trame5) == False
    trame6 = []
    trame6[0] = 2
    trame6[1] = -5
    trame6[2] = 15
    assert jeu.parse_message(trame6) == False
    trame7 = []
    trame7[0] = 2.0
    trame7[1] = 2.5
    trame7[2] = 5.5
    assert jeu.parse_message(trame7) == False
    trame8 = []
    trame8[0] = a
    trame8[1] = 5
    trame8[2] = b
    assert jeu.parse_message(trame8) == False