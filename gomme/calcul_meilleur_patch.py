import sys

from gomme.utils.patch import Patch


def patch_complet(x: int, y: int, xsize: int, ysize: int, original: list) -> bool:
    """Je crée une fonction qui prend en arguments 4 entiers et un tableau, celle-ci détecte si il y a des pixels de
    masque dans le patch si c'est le cas elle renvoie alors le boolean False sinon elle renvoie le boolean True  """

    for i in range(xsize):
        for j in range(ysize):
            if original[x + i, y + j] == 0:
                return (False)

    return True


def cible(xsize: int, ysize: int, x1: int, y1: int, tableau_masque: list) -> tuple:
    """Je crée une fonction qui prend en arguments 4 entiers et un tableau, celle-ci parcours les pixels du patch et
    les ajoute a une des deux listes retourné en fonction de si ils appartiennent au masque ou non elle renvoie un
    entier, deux listes et deux entiers"""

    compteur = 0
    cibles, ciblem = [], []
    for i in range(xsize):
        for j in range(ysize):
            if tableau_masque[y1 + i, x1 + j] == 0:
                compteur += 1
                cibles += [(i, j)]
            else:
                ciblem += [(i, j)]

    return compteur, cibles, ciblem, xsize, ysize


def calculPatch(coordonnees_contours: list, index: int, image_masque_copie: list, original: list, tableau_masque: list,
                taille_cadre: int) -> tuple:
    """Je crée une fonction qui prend en arguments une liste, un entier, trois tableaux et un entier, celle-ci
    détermine le points le plus adéquat pour la reconstitution d' un pixel elle nous retourne une liste et un tuple """

    mini = min_var = sys.maxsize
    sourcePatch = []
    coordonnees_point = coordonnees_contours[index]
    patch = Patch(image_masque_copie, taille_cadre, coordonnees_point)
    x1, y1 = patch[0]
    x2, y2 = patch[1]
    lignes, colonnes, a = image_masque_copie.shape
    # a est inutile mais si on met image_masque_copie.shape[:2] il peu y avoir des erreurs
    compteur, cibles, ciblem, xsize, ysize = cible(y2 - y1 + 1, x2 - x1 + 1, x1, y1, tableau_masque)
    for x in range(lignes - xsize):
        for y in range(colonnes - ysize):
            if patch_complet(x, y, xsize, ysize, original):
                sourcePatch += [(x, y)]
    for (y, x) in sourcePatch:
        R = V = B = dif = 0
        for (i, j) in cibles:
            imc = image_masque_copie[y + i, x + j]
            zcmasque = image_masque_copie[y1 + i, x1 + j]
            for k in range(3):
                difference = float(imc[k]) - float(zcmasque[k])
                dif += difference ** 2
            R += imc[0]
            V += imc[1]
            B += imc[2]
        dif /= compteur
        if dif < mini:
            variation = 0
            for (i, j) in ciblem:
                imc = image_masque_copie[y + i, x + j]
                differenceR = imc[0] - R / compteur
                differenceV = imc[1] - V / compteur
                differenceB = imc[2] - B / compteur
                variation += differenceR ** 2 + differenceV ** 2 + differenceB ** 2
            if dif < mini or variation < min_var:
                min_var = variation
                mini = dif
                pointPatch = (x, y)

    return ciblem, pointPatch
