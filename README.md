1/4

# TD : Acoustique sous-marine et sonar latéral

## 1 Interprétation d’image


La figure 1 représente un extrait d’une image sonar latéral. Cette image fait 492 pixels
horizontallement et 489 pixels verticalement. Chaque pixel est un carré d’environ 20 cm de
côté. On y observe l’épave de La Perle, chalutier école coulé en baie de Douarnenez en 1985.


Figure 1 – Image 1


1. Décrire l’image et proposer des interprétations des éléments observés.

2. Pourquoi ne "voit"-on pas la coque de l’épave ? Faire un schéma.


1


2/4


3. Quelle est l’altitude du sonar au dessus du fond ?

4. Quelle est la longueur de l’épave ?

5. Quelle est la hauteur de l’épave (maximale) ?

6. En utilisant le pont avant de l’épave, calculer la largeur du bateau, et l’inclinaison de
l’épave.

## 2 Détection d’objet au sonar latéral


On suppose un sonar latéral dont l’antenne est utilisée à la fois en émission et en réception.
Cette antenne est inclinée d’un angle φ0 avec l’horizontal, positif vers le bas. Une cible sphérique
supposée ponctuelle et de rayon a = 0.5 m est posée sur un fond plat. Nous cherchons dans cet
exercice à estimer si la cible peut être détectée par le sonar ou non.
La hauteur d’eau est h = 200 m et l’altitude du sonar au dessus du fond est h0 = 30 m. La
cible est à un range r = 300 m hors de l’axe du sonar.


Les caractéristiques du sonar sont les suivantes :

  - Longueur de l’antenne : L = 2 m

  - Largeur de l’antenne : l = 3 cm

  - Inclinaison de l’antenne : φ0 = 5°

  - Fréquence du signal émis : f = 100 kHz

  - Bande du signal émis : B = 10 kHz

  - Type de signal émis : chirp de durée τ = 10 ms

  - Niveau d’émission : SL = 200 dB ref. 1µPa à 1 m, intégrant l’index de directivité

  - Ouverture équivalente : Φ = 0.005 rad



On utilisera :

 - pour la rétro-diffusion sur une sphère rigide, l’approximation géométrique (d >> λ)
suivante :  



TS = 10 log10




a2



4




(1)



avec d le diamètre de la sphère rigide, et a son rayon.

  - pour la rétro-diffusion du fond, le modèle de Lambert suivant :


BS = 10 + 20 log10(sin β) (2)
                  
avec β l’angle de rasance.

  - pour la rétro-diffusion de surface, le modèle suivant :


SR = 30 + 20 log10(sin β) (3)
                  
avec β l’angle de rasance.
Lors des acquisitions avec le sonar, le vent a une vitesse nulle.

1. Faire un schéma du problème.


2


3/4


2. Pour évaluer si la cible est détectable, nous allons calculer le rapport signal sur bruit
(RSB) de l’écho de la cible reçu par le sonar. En décibels on a :


RSB = SIGNAL − BRUIT (4)

(a) À quoi correspond le terme SIGNAL ?
(b) Quels sont phénomènes considérés comme BRUIT ?
(c) Une méthode de traitement du signal est utilisée ici pour améliorer ce rapport signal
sur bruit. Quelle est cette méthode ?


3. Écrire l’équation sonar permettant de calculer la partie SIGNAL (en décibels) du problème.

4. Écrire les équations sonar permettant de calculer chacun des phénomènes de la partie
BRUIT (en décibels).

5. Donner les expressions des angles : de la cible avec l’horizontale (φc), de la surface avec
l’horizontale (φs), et du fond marin avec l’horizontale (φf ), en fonction des hauteurs h
et h0, de la distance oblique à la cible (range) r, et du rayon de la cible a.

6. Calculer chacun des paramètres des équations sonar précédentes.

7. Calculer le rapport signal sur bruit. La sphère est-elle détectable ?

## 3 Annexes


Fonction de directivité d’une antenne linéaire
Pour une antenne de longueur L à la fréquence f on a :




π [Lf]
(θ) = [sin] c
D π [Lf]



c (5)

c [sin(][θ][)]



π [Lf]




c [sin(][θ][)]



Avec c la célérité des ondes acoustiques, et θ l’angle par rapport à l’axe de l’antenne.


Index de directivité (ou gain d’antenne) d’une antenne rectangulaire
Pour une antenne de longueur L et de largeur l à la fréquence f on a :


DIRx = [4][π][(][L][ ·][ l][)] (6)

λ [2]


3


