import cv2

import numpy as np
from numpy.core.multiarray import ndarray

img = cv2.imread('Images Test/plage_parasol.jpg')
mask = cv2.imread('Images Test/masque_parasolLEBON.jpg', 0)


def appliquer_masque(image: ndarray, masque: ndarray):
    L = []
    image_copie: ndarray = np.copy(image)
    tableau_masque: ndarray = np.copy(masque)  # Transformation de l' image en tableau
    fiabilite = np.copy(masque)

    lignes, colonnes, channels = image_copie.shape

    for i in range(lignes):
        for j in range(colonnes):
            if tableau_masque[i, j] < 170:
                # car les contours du masque ne sont pas totalement noir (1 seul valeur car lecture en noir|blanc)

                image_copie[i, j] = [255, 255, 255]  # [255, 255, 255] pour blanc ou [0, 0, 0] pour noir
                L.append([i, j])
                tableau_masque[i, j] = 1
                # on met dans le masque la valeur de 1 de manière a les retrouvé plus facilement que avec le tau
                fiabilite[i, j] = 0
                # mettre un . ? #dans la copie du masque appelé fiabilité on place des 0
            else:
                masque[i, j] = 0
                # on met dans le masque la valeur de 1 de manière a les retrouvé plus facilement que avec le tau
                fiabilite[i, j] = 1
                # mettre un . ? #dans la copie du masque appelé fiabilité on place des 1

    source = np.copy(fiabilite)  # copie de la liste confiance crée au dessus assigné a la valeur source
    original = np.copy(fiabilite)  # copie de la liste confiance crée au dessus assigné a la valeur original

    return image_copie, source, original, L


#
# dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
#
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image_masque, source, original, omega = appliquer_masque(img, mask)

cv2.imshow('image', image_masque)
lap = np.array([[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]])
kerx = np.array([[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]])
kery = np.array([[1., 2., 1.], [0., 0., 0.], [-1., -2., -1.]])

# GradientX = cv2.filter2D(source, cv2.CV_32F, kerx) #Utilisé dans zone de remplissage.
# GradientY = cv2.filter2D(source, cv2.CV_32F, kery)

# cv2.imshow('resultat x', GradientX)
# cv2.imshow('resultat y', GradientY)

niveau_de_gris = cv2.cvtColor(image_masque, cv2.COLOR_RGB2GRAY)
GradientX = cv2.convertScaleAbs(cv2.Scharr(niveau_de_gris, cv2.CV_32F, 1, 0))
GradientY = cv2.convertScaleAbs(cv2.Scharr(niveau_de_gris, cv2.CV_32F, 0, 1))

lignes, colonnes = source.shape

for i in range(lignes):  # on parcours la copie de source : les lignes
    for j in range(colonnes):  # les colonnes
        if mask[i][j] == 0:  # Le Zéro permet d'avoir des contour tres précis.
            # si cela est égal a 1 cad les endroit on ne met pas de masque (les endroit blanc sur le masque)

            GradientX[i][j] = 0
            GradientY[i][j] = 0

cv2.imshow('resultat x 2', GradientX)
cv2.imshow('resultat y 2', GradientY)

cv2.waitKey(0)



import cv2
import numpy as np

Lap = np.array([[1., 1., 1.], [1., -8., 1.], [1., 1., 1.]])
kerx = np.array([[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]])
kery = np.array([[1., 2., 1.], [0., 0., 0.], [-1., -2., -1.]])

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

domega, normale = zone_de_remplissage(mask, source)

a=5+3
# ajouter un vecteur associer a chauque points
#
