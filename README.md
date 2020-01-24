# Mega bataille navale

## Jeu

* Méga bataille navale
  * Inspiré de la bataille navale classique
  * 3 niveaux de grille superposées : les bateaux, les sous-marins de surface, les sous-marins profonds
  * Un missile tire à la verticale et s'arrête au premier obstacle
* En réseau (TCP/IP)
  * Un joueur par PC
  * Protocole défini : interopérabilité des logiciels que vous créez
* Mode manuel, et mode intelligence artificielle
* Autres règles supplémentaires à discuter
  * Ce document est public, il sera régulièrement mis à jour, proposez une pull request pour l'améliorer (par exemple pour ajouter un lien vers votre dépôt GitHub)
  * Nombre de vaisseaux, types de vaisseaux, longeur des vaisseaux
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
  * Interface graphique en Qt (avec Python)
  * Tests unitaires faits
  * Intégration continue (TravisCI, Azure Pipelines, GitHub Actions…)
* Rapport
  * Planification (prévisionnelle et réelle)
  * Petit mode d'emploi
  * Description de qui a fait quoi, et quelles ont été les difficultés/réussites de cette réalisation

## Documentation

### Protocole réseau

TBD

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