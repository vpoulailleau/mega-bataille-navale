import sys

sys.path.insert(1, 'src')

from jeu import *

def test_recevoir_tir():
    jeu = Jeu()

    navire = Navire(3, 1, "AlainBernard")
    jeu.carte_perso.navires.append(navire)
    jeu.carte_perso.navires[0].cases.append(Case(11, 5, 1))
    jeu.carte_perso.navires[0].cases.append(Case(10, 5, 1))
    jeu.carte_perso.navires[0].cases.append(Case(9, 5, 1))

    #assert jeu.recevoir_tir(-50, 20) == (False, 1)
    #assert jeu.recevoir_tir(-50, -20) == False
    assert jeu.recevoir_tir(50, 20)[0] == False
    #assert jeu.recevoir_tir(50, -20) == False
    #assert jeu.recevoir_tir(5.5, 2.3) == False
    #assert jeu.recevoir_tir(-5.5, -2.3) == False
    assert jeu.recevoir_tir(0, 0)[0] == False
    assert jeu.recevoir_tir(4, 5)[0] == False
    #assert jeu.recevoir_tir(a, b) == False
    assert jeu.recevoir_tir(11, 5) == (True, 1)

def test_parse_message():
    jeu = Jeu()

    trame = []
    trame.append(2)
    trame.append(1)
    trame.append(5)
    assert jeu.parse_message(trame) == (1, 5)

    # Bad Message ID
    trame1 = []
    trame1.append(0)
    trame1.append(1)
    trame1.append(1)
    assert jeu.parse_message(trame1) == (None, None)

    trame2 = []
    trame2.append(2)
    trame2.append(0)
    trame2.append(5)
    assert jeu.parse_message(trame2) == (0, 5)

    trame3 = []
    trame3.append(2)
    trame3.append(5)
    trame3.append(17)
    assert jeu.parse_message(trame3) == (5, 17)
 
    trame4 = []
    trame4.append(2)
    trame4.append(18)
    trame4.append(0)
    assert jeu.parse_message(trame4) == (18, 0)

    # Negative message ID
    trame5 = []
    trame5.append(-5)
    trame5.append(18)
    trame5.append(0)
    assert jeu.parse_message(trame5) == (None, None)

    trame6 = []
    trame6.append(2)
    trame6.append(-5)
    trame6.append(15)
    assert jeu.parse_message(trame6) == (-5, 15)

    trame8 = []
    trame8.append(2.0)
    trame8.append(2.5)
    trame8.append(5.5)
    assert jeu.parse_message(trame8) == (2.5, 5.5)

    #trame9 = []
    #trame9.append(a)
    #trame9.append(5)
    #trame9.append(b)
    #assert jeu.parse_message(trame9) == False
