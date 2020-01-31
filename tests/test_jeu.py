import pytest
from jeu import *

def test_recevoir_tir(self):
    jeu = Jeu()
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
    assert jeu.parse_message()
