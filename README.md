# Mega bataille navale

## Jeu

* Méga bataille navale
  * Inspiré de la bataille navale classique
  * 3 niveaux de grille superposées : les bateaux, les sous-marins de surface, les sous-marins profonds
  * Un missile tire à la verticale et s'arrête au premier obstacle
    * On est prévenu de la couche de l'impact (exemple : touché à la couche des sous-marins de surface)
* En réseau (TCP/IP)
  * Un joueur ou IA par PC
  * Protocole défini : interopérabilité des logiciels que vous créez, vous pourrez faire combattre les IA entre elles par exemple
* Mode manuel, et mode intelligence artificielle
* Taille carte 15×15×3
* Nombres de vaisseaux, types de vaisseaux, longUeur des vaisseaux
  * 1 porte-container 5×2
  * 2 porte-avions 5×1
  * 3 destroyers 4×1
  * 3 torpilleurs 3×2
  * 2 sous-marins nucléaires 6×1
    * À la destruction, il explose dans un rayon de 3 cases autour de lui, dans sa couche
  * 5 petits sous-marins 3×1
  * 2 mini sous-marins 2×1
* Ce document est public, il sera régulièrement mis à jour, proposez une pull request pour l'améliorer (par exemple pour ajouter un lien vers votre dépôt GitHub)

### À voir plus tard

* Missiles puissants (à acheter, ou dispo en aléatoire)
* Déplacement des bateaux et sous-marins
* Boucliers anti-missiles
* Intervention extra-terrestre
* Gestion du carburant
* …

## Contraintes

* Équipes de 4 personnes (88h de projet * 4 personnes)
* Code sur GitHub
  * Code Python
  * Interface graphique en Qt (avec Python, PySide2)
  * Tests unitaires faits
  * Intégration continue (TravisCI, Azure Pipelines, GitHub Actions…)
* Rapport
  * Planification (prévisionnelle et réelle)
  * Petit mode d'emploi
  * Description de qui a fait quoi, et quelles ont été les difficultés/réussites de cette réalisation

## Documentation

### Protocole réseau

Le protocole est ici décrit en octets. L'encodage des chaînes de caractères est UTF-8.

#### Connexion

Le client envoie au serveur le nom du joueur, le serveur répond ensuite par le nom de l'adversaire.

| Numéro d'octet | Signification / Valeur                  |
| -------------- | --------------------------------------- |
| 0              | ID de message, vaut 1                   |
| 1              | Longueur du nom de joueur en octets (N) |
| 2 à (N+1)      | Nom du joueur                           |

#### Tirs

Le client commence, il tire et reçoit ensuite une réponse du serveur, puis le serveur tire et reçoit une réponse du client. À la fin de cette séquence de 4 messages, on décide du vainqueur (ou de continuer la partie s'il reste des bateaux)

##### Lancé de missile

| Numéro d'octet | Signification / Valeur |
| -------------- | ---------------------- |
| 0              | ID de message, vaut 2  |
| 1              | Abcisse (de 1 à 15)    |
| 2              | Ordonnée (de 1 à 15)   |

##### Réponse au lancé

| Numéro d'octet | Signification / Valeur                                                                                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | ID de message, vaut 3                                                                                                                    |
| 1              | Résultat du tir (0 pour dans l'eau, 1 pour touché un bateau, 2 pour touché un sous-marin de surface, 3 pour touché un sous-marin profond |

### Liens internet

* Qt
  * Licence LGPLv3 ou GPLv3 ou commerciale
  * https://doc.qt.io/qtforpython/
  * https://doc.qt.io/qtforpython/quickstart.html
  * Je ne vous conseille pas QtQuick/QML qui necessite du JavaScript, sauf si vous savez ce que vous faites
  * https://doc.qt.io/qtforpython/tutorials/index.html
* Python
  * Tout ce site est d'excellente qualité : https://realpython.com/
  * https://docs.python.org/fr/3/library/socketserver.html
  * Tests unitaires : https://realpython.com/python-testing/ (je vous conseille pytest)
* Markdown
  * https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
* Travis CI
  * https://docs.travis-ci.com/user/tutorial/
  * https://docs.travis-ci.com/user/languages/python/
  * https://blog.travis-ci.com/2019-08-07-extensive-python-testing-on-travis-ci