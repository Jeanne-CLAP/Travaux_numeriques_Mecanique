# Travaux_numeriques_Mecanique
Répertoire de scripts Python dédié à la simulation et au calcul numérique en mécanique.

## 1. Résistance des matériaux : optimisation de poutre
L'utilisateur entre les dimensions d'une poutre ainsi que la force appliquée sur cette dernière. Le programme calcule la contrainte maximale, le déplacement des 3 matériaux choisis (Acier, Silice, Aluminium) et conclut si le matériau résiste.
* **Bibliothèques requises** : *numpy*

## 2. Tenseur des contraintes et tricercle de Mohr (MMC des solides)
L'utilisateur entre le tenseur des contraintes de son choix. Le programme calcule les contraintes principales et trace le tricercle de Mohr.
* **Bibliothèques requises** : *numpy*, *matplotlib*, *tkinter* (généralement inclus par défaut avec Python 3)

## 3. Simulateur d'un système Masse-Ressort amorti : étude des régimes
Simulateur d'un oscillateur harmonique amorti d'un système masse-ressort. Le programme résout l'équation différentielle du 2nd ordre, identifie le régime en fonction de l'amortissement et trace les 4 régimes sur le même graphique.
* **Bibliothèques requises** : *numpy*, *matplotlib*, *scipy*
