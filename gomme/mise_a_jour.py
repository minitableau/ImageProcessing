from gomme.utils.patch import Patch

def update(image_masque_copie, fiabilite, source, tableau_masque, coordonnees_contours, pp, list, index, taille_cadre):
    p = coordonnees_contours[index]
    patch = Patch(image_masque_copie, taille_cadre, p)
    x1, y1 = patch[0]
    px, py = pp
    for (i, j) in list:
        image_masque_copie[y1 + i, x1 + j] = image_masque_copie[py + i, px + j]
        fiabilite[y1 + i, x1 + j] = fiabilite[py, px]
        source[y1 + i, x1 + j] = 1
        tableau_masque[y1 + i, x1 + j] = 0
    return (image_masque_copie, fiabilite, source, tableau_masque)

