import cv2
import numpy as np

Lap = np.array([[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]])
# Il s' agit la du kernel utilisé pour détecter les contours par le biais de la méthode Laplacian elle n' en utilise
# qu' un : [[0, 1, 0], [1, -4, 1], [0, 1, 0]] ou [[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]] si on veux
# considéré les diagonales

kerx = np.array([[0., 0., 0.], [-1., 0., 1.], [0., 0., 0.]])
# [ 0, 0, 0]
# [-1, 0, 1]
# [ 0 ,0, 0]
kery = np.array([[0., -1., 0.], [0., 0., 0.], [0., 1., 0.]])
# [ 0,-1, 0]
# [ 0, 0, 0]
# [ 0, 1, 0]


# Recherche de la zone de remplissage à partir des kernels
def zone_de_remplissage(masque, source):
    lap = cv2.filter2D(masque, cv2.CV_32F, Lap)
    xsize, ysize = lap.shape
    GradientX = cv2.filter2D(source, cv2.CV_32F, kerx)
    GradientY = cv2.filter2D(source, cv2.CV_32F, kery)
    dOmega = []
    normale = []
    for x in range(xsize):
        for y in range(ysize):
            if lap[x, y] > 0:
                dOmega += [(y, x)]
                dx = GradientX[x, y]
                dy = GradientY[x, y]
                N = (dy ** 2 + dx ** 2) ** 0.5
                if N != 0:
                    normale += [(dy / N, -dx / N)]
                else:
                    normale += [(dy, -dx)]
    return dOmega, normale
