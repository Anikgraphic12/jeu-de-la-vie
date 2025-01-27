import numpy as np
import matplotlib.pyplot as plt
import time

# Fonction pour afficher la grille
def afficher_grille(grille):
    plt.imshow(grille, cmap='binary', interpolation='nearest')  # Affiche la grille
    plt.axis('off')  # Masquer les axes
    plt.show()

# Fonction pour compter les voisins vivants d'une cellule (i, j)
def compter_voisins(grille, i, j):
    voisins = 0
    for di in range(-1, 2):  # Parcourir les 8 voisins autour de (i, j)
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue  # Ignorer la cellule elle-même
            if 0 <= i + di < grille.shape[0] and 0 <= j + dj < grille.shape[1]:
                voisins += grille[i + di, j + dj]
    return voisins

# Fonction pour mettre à jour la grille selon les règles du jeu
def iterer_grille(grille):
    N, M = grille.shape
    nouvelle_grille = np.zeros_like(grille)  # Crée une nouvelle grille vide
    
    for i in range(N):
        for j in range(M):
            voisins = compter_voisins(grille, i, j)
            
            if grille[i, j] == 1:
                # La cellule est vivante
                if voisins == 2 or voisins == 3:
                    nouvelle_grille[i, j] = 1  # La cellule reste vivante
                else:
                    nouvelle_grille[i, j] = 0  # La cellule meurt
            else:
                # La cellule est morte
                if voisins == 3:
                    nouvelle_grille[i, j] = 1  # La cellule devient vivante
                else:
                    nouvelle_grille[i, j] = 0  # La cellule reste morte
    
    return nouvelle_grille

# Fonction pour initialiser une grille aléatoire
def init_grille(N):
    # Crée une grille N x N avec des 0 (mortes) et des 1 (vivantes)
    return np.random.choice([0, 1], size=(N, N))

# Fonction principale pour lancer le jeu de la vie
def jeu_de_la_vie(N, iterations=100, afficher=True):
    grille = init_grille(N)  # Initialisation d'une grille aléatoire
    
    if afficher:
        afficher_grille(grille)
    
    for _ in range(iterations):
        grille = iterer_grille(grille)  # Mettre à jour la grille
        if afficher:
            afficher_grille(grille)  # Afficher la grille après chaque itération
            time.sleep(0.1)  # Attendre un peu avant la prochaine itération

# Lancer le jeu de la vie avec une grille de taille 20x20 pendant 50 itérations
jeu_de_la_vie(20, iterations=50)
