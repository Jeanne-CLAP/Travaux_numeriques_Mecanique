import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Etape 1 : On part de l'équation différentielle d'un oscillateur du 2nd ordre : m.(d²x/dt²) + gamma.(dx/dt) + k.x = 0.
#           On transforme cette équation en un système de 2 équations du 1er ordre.

def equa_diff(y, t, m, gamma, k):
    x, v = y # Attribution des valeurs de y aux variables x (la position) et v (la vitesse)
    dxdt = v # Première équation (par définition, la vitesse)
    dvdt = -(gamma/m)*v-(k/m)*x # Deuxième équation (expression de l'accélération)
    return [dxdt, dvdt] # On renvoie les dérivées (vitesse et accélération)


# Etape 2 : Création d'une fonction pour calculer la solution de l'équation différentielle et identifier le régime

def oscillateur(m, gamma, k, t):
    y0 = [1.0, 0.0] # Conditions initiales : l'objet est lâché à 1m de hauteur et sans vitesse initiale
    sol = odeint(equa_diff, y0, t, args=(m, gamma, k)) # Calcul de la trajectoire
    position = sol[:, 0] # On récupère uniquement la première colonne (position x au cours du temps)


    # Etape 3 : Analyse des régimes

    gamma_critique = 2*np.sqrt(m*k) # Calcul du coefficient d'amortissement en régime critique

    # Détermination du régime selon la valeur de gamma
    if gamma == 0 :
        regime = "Périodique (pas d'amortissement)"
        couleur = "blue"
    elif gamma < gamma_critique :
        regime = "Pseudo-périodique (amortissement faible)"
        couleur = "green"
    elif np.isclose(gamma, gamma_critique, atol=0.1) : # Si gamma est très proche du critique
        regime = "Critique (amortissement optimal)"
        couleur = "red"
    else :
        regime = "Apériodique (amortissement fort)"
        couleur = "orange"

    plt.plot(t, position, color=couleur, lw=2, label=regime) # On trace la courbe sur une même fenêtre


# Etape 4 : Création du graphique

plt.figure(figsize=(10, 6))
t = np.linspace(0, 20, 1000) # Axe de temps : 20 s, 1000 pts
m_fixe = 1.0 # Valeur de la masse (1.0 kg)
k_fixe = 10.0 # Valeur de la raideur du ressort (10.0 N/m)
g_crit = 2*np.sqrt(m_fixe*k_fixe) # Calcul coeff d'amortissement critique

# On apelle la fonction dans les 4 cas
oscillateur(m_fixe, 0, k_fixe, t)
oscillateur(m_fixe, 0.8, k_fixe, t)
oscillateur(m_fixe, g_crit, k_fixe, t)
oscillateur(m_fixe, 15.0, k_fixe, t)

# Paramétrage et légende du graphique
plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.title("Comparaison des 4 régimes de l'oscillateur harmonique")
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.grid(True, alpha=0.3)
plt.legend()

# Affichage
plt.show()