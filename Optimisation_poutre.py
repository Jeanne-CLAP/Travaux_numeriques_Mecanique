import numpy as np


# Etape 1 : Saisie des données par l'utilisateur dans la console

L = float(input("Longueur L (en m) : "))
l = float(input("Largeur l (en m) : "))
h = float(input("Hauteur h (en m) : "))
F = float(input("Force F (en N) : "))


# Etape 2 :

I = (l*h**3)/12 # Calcul du moment d'inertie
sigma_max = (F*L*(h/2))/I # Calcul de la contrainte maximum
sigma_mpa = sigma_max/1e6 # Conversion de la contrainte en MPa


# Etape 3 : Données des matériaux

materiaux = {"Acier": [250, 7850, 200*1e3], "Aluminium": [150, 2700, 70*1e3], "Silice": [50, 2200, 90*1e3]}
# Ordre de saisie : limite élastique (en MPa), densité (en kg/m3), Module d'Young (en MPa)
# Données d'après "Physique des polymères tome 2 (2005), Combette et Ernoult"


# Etape 4 : Analyse de la résistance des matériaux

print("\nContrainte max : {:.2f} MPa".format(sigma_mpa)) # Affichage de la contrainte maximale
print("-"*50) # Affichage de la séparation entre la contrainte max et les données de résistance des matériaux

for nom, infos in materiaux.items():
    limite, densite, E = infos # On distribue les données de chaque matériau
    masse = (L*l*h)*densite # Calcul de la masse
    deplacement = (F*L**3)/(3*(E*1e6)*I) # Calcul du déplacement (et on convertit E en Pa)

    # Test de résistance
    if sigma_mpa < limite:
        resultat = "RESISTE"
    else:
        resultat = "CASSE"

    print("{:10} | Masse: {:5.1f} kg | Déplacement: {:5.2f} mm | {}".format(nom, masse, deplacement*1000, resultat)) #Affichage final
