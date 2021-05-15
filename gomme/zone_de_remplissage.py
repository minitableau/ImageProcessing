import cv2
import numpy as np

noyau_lap = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])


# Il s' agit la du kernel utilisé pour détecter les contours par le biais de la méthode Laplacian elle n' en utilise
# qu' un : [[0, 1, 0], [1, -4, 1], [0, 1, 0]] ou [[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]] si on veux considéré les
# diagonales pour une meilleur precision j' ai cru comprendre qui fallait rajouter des . pour montrer que cela peu
# être des flottants

# Recherche de la zone de remplissage à partir des kernels

def zone_de_remplissage(tableau_masque):
    contours = cv2.filter2D(tableau_masque, cv2.CV_32F, noyau_lap)
    lignes, colonnes = contours.shape
    coordonnees_contours = []
    for i in range(lignes):
        for j in range(colonnes):
            if contours[i, j] > 0:
                coordonnees_contours += [
                    (j, i)]  # inversion des indices pour avoir les coordonnés(colonnes=x et ligne = y)
    return coordonnees_contours
