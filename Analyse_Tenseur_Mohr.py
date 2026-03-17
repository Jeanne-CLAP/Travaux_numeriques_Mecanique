import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
import sys


# Configuration du pop-up pour la saisie des données

def saisie(nom):
    message = "Entrez la valeur de {} (en MPa) :".format(nom)
    return simpledialog.askfloat("Saisie des composantes du tenseur des contraintes", message)

root = tk.Tk()
root.withdraw() # Réglage de l'affichage du pop-up (cacher fenêtre inutile)


# Etape 1 : Saisie des données

# Ligne 1
s11 = saisie("la composante de direction 1 normale à la facette 1")
s12 = saisie("la composante de direction 1 normale à la facette 2")
s13 = saisie("la composante de direction 1 normale à la facette 3")

# Ligne 2 (On ne demande que s22 et s23 car s21 = s12)
s22 = saisie("la composante de direction 2 normale à la facette 2")
s23 = saisie("la composante de direction 2 normale à la facette 3")

# Ligne 3 (On ne demande que s33 car s31 = s13 et s32 = s23)
s33 = saisie("la composante de direction 3 normale à la facette 3")


# Etape 2 : Construction de la matrice

sigma = np.array([[s11, s12, s13], [s12, s22, s23], [s13, s23, s33]])


# Etape 3 : Calcul des contraintes principales

valeurs = np.linalg.eigvals(sigma) # Calcul des valeurs propres du tenseur
valeurs.sort() # Tri par ordre croissant (sI < sII < sIII)
sI, sII, sIII = valeurs # On nomme les 3 contraintes principales obtenues

# Etape 4 : Tracé du Tricercle de Mohr

rayon_max = (sIII-sI)/2 # Calcul du rayon maximum pour adapter le cadrage

fig, ax = plt.subplots(figsize=(8, 5)) # Initialisation de la figure et définition de sa taille

cercles = [(sI, sII), (sII, sIII), (sI, sIII)]

for (a, b) in cercles:
    centre = (a+b)/2 # Centre des cercles
    rayon = abs(b-a)/2 # Rayons des cercles
    ax.add_artist(plt.Circle((centre, 0), rayon, fill=False, color='blue', lw=1.5)) # Création du cercle avec uniquement les contours

ax.set_xlim(sI - 5, sIII + 5) # Marge horizontale
ax.set_ylim(-rayon_max * 1.3, rayon_max * 1.3) # Marge verticale pour adapter le cadrage à la taille du cercle
ax.set_aspect('equal') # Force un cercle rond
ax.axhline(0, color='black', lw=1) # Axe des abscisses
ax.grid(True, linestyle=':') # Affichage de la grille

# Légende du schéma
plt.title("Tricercle de Mohr")
plt.xlabel("Contrainte normale $\sigma$ (MPa)")
plt.ylabel(r"Contrainte tangentielle $\tau$ (MPa)")

# Affichage
print("Les contraintes principales calculées sont : sI={:.2f}, sII={:.2f}, sIII={:.2f}".format(sI, sII, sIII))
plt.show()
