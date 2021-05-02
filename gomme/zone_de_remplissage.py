import cv2
import numpy as np

Lap = np.array([[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]])
# Il s' agit la du kernel utilisé pour détecter les contours par le biais de la méthode Laplacian elle n' en utilise
# qu' un : [[0, 1, 0], [1, -4, 1], [0, 1, 0]] ou [[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]] si on veux considéré les
# diagonales pour une meilleur precision j' ai cru comprendre qui fallait rajouter des . pour montrer que cela peu
# être des flottants

# On changera probablement les valeurs des ces kernels lorsque le code sera complet de manière
# a obtenir le meilleur résultat possible il s' agit la des kernels de Sobel
kerx = np.array([[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]])

kery = np.array([[1., 2., 1.], [0., 0., 0.], [-1., -2., -1.]])


# Recherche de la zone de remplissage à partir des kernels
def zone_de_remplissage(masque, source):
    lap = cv2.filter2D(masque, cv2.CV_32F, Lap)
    lignes, colonnes = lap.shape
    GradientX = cv2.filter2D(source, cv2.CV_32F, kerx)
    GradientY = cv2.filter2D(source, cv2.CV_32F, kery)
    dOmega = []
    normale = []
    for i in range(lignes):
        for j in range(colonnes):
            if lap[i, j] > 0:
                dOmega += [(j, i)] # inversion des indices pour avoir les coordonnés(colonnes=x et ligne = y)
                dx = GradientX[i, j]
                dy = GradientY[i, j]
                N = (dy ** 2 + dx ** 2) ** 0.5
                if N != 0:
                    normale += [(dy / N, -dx / N)]
                else:
                    normale += [(dy, -dx)]
    return dOmega, normale
