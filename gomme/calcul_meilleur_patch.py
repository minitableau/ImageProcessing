import sys

from gomme.utils.patch import Patch


def patch_complet(x, y, xsize, ysize, original):
    for i in range(xsize):
        for j in range(ysize):
            if original[x + i, y + j] == 0:
                return (False)
    return (True)


def crible(xsize, ysize, x1, y1, tableau_masque):
    compteur = 0
    cibles, ciblem = [], []
    for i in range(xsize):
        for j in range(ysize):
            if tableau_masque[y1 + i, x1 + j] == 0:
                compteur += 1
                cibles += [(i, j)]
            else:
                ciblem += [(i, j)]
    return (compteur, cibles, ciblem, xsize, ysize)


def calculPatch(coordonnees_contours, cibleIndex, image_masque_copie, original, tableau_masque, taille_cadre):
    mini = minvar = sys.maxsize
    sourcePatch, sourcePatche = [], []
    coordonnees_point = coordonnees_contours[cibleIndex]
    patch = Patch(image_masque_copie, taille_cadre, coordonnees_point)
    x1, y1 = patch[0]
    x2, y2 = patch[1]
    Xsize, Ysize, c = image_masque_copie.shape
    compteur, cibles, ciblem, xsize, ysize = crible(y2 - y1 + 1, x2 - x1 + 1, x1, y1, tableau_masque)
    for x in range(Xsize - xsize):
        for y in range(Ysize - ysize):
            if patch_complet(x, y, xsize, ysize, original):
                sourcePatch += [(x, y)]
    for (y, x) in sourcePatch:
        R = V = B = ssd = 0
        for (i, j) in cibles:
            ima = image_masque_copie[y + i, x + j]
            omega = image_masque_copie[y1 + i, x1 + j]
            for k in range(3):
                difference = float(ima[k]) - float(omega[k])
                ssd += difference ** 2
            R += ima[0]
            V += ima[1]
            B += ima[2]
        ssd /= compteur
        if ssd < mini:
            variation = 0
            for (i, j) in ciblem:
                ima = image_masque_copie[y + i, x + j]
                differenceR = ima[0] - R / compteur
                differenceV = ima[1] - V / compteur
                differenceB = ima[2] - B / compteur
                variation += differenceR ** 2 + differenceV ** 2 + differenceB ** 2
            if ssd < mini or variation < minvar:
                minvar = variation
                mini = ssd
                pointPatch = (x, y)
    return (ciblem, pointPatch)
