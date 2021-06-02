from gomme.utils.patch import Patch


def MAJ(image_masque_copie: list, fiabilite: list, source: list, tableau_masque: list, coordonnees_contours: list,
        pp: tuple, L: list, index: int, taille_cadre: int) -> tuple:
    """Je crée une fonction qui prend en arguments quatre tableaux, une liste, un tuple, une liste et deux entiers,
    celle-ci met à jour la plupart des fonctions (c'est elle qui modifie le tableau final) elle nous renvoie quatre
    tableaux"""

    p = coordonnees_contours[index]
    patch = Patch(image_masque_copie, taille_cadre, p)
    x1, y1 = patch[0]
    px, py = pp
    for (i, j) in L:
        image_masque_copie[y1 + i, x1 + j] = image_masque_copie[py + i, px + j]
        fiabilite[y1 + i, x1 + j] = fiabilite[py, px]
        source[y1 + i, x1 + j] = 1
        tableau_masque[y1 + i, x1 + j] = 0

    return image_masque_copie, fiabilite, source, tableau_masque
