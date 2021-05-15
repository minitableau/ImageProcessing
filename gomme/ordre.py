from gomme.utils.patch import Patch

def calculConfiance(fiabilite, image_masque_copie, taille_cadre, tableau_masque, coordonnees_contours):
    for k in range(len(coordonnees_contours)):
        px, py = coordonnees_contours[k]
        patch = Patch(image_masque_copie, taille_cadre, coordonnees_contours[k])
        x3, y3 = patch[0]
        x2, y2 = patch[1]
        compteur = 0
        taille_psi_p = ((x2 - x3 + 1) * (y2 - y3 + 1))
        for x in range(x3, x2 + 1):
            for y in range(y3, y2 + 1):
                if tableau_masque[y, x] == 0:
                    compteur += fiabilite[y, x]
        fiabilite[py, px] = compteur / taille_psi_p
    return (fiabilite)


def calculPriority(image_masque_copie, taille_cadre, tableau_masque, coordonnees_contours, fiabilite):
    C = calculConfiance(fiabilite, image_masque_copie, taille_cadre, tableau_masque, coordonnees_contours)
    index = 0
    maxi = 0
    for i in range(len(coordonnees_contours)):
        x, y = coordonnees_contours[i]
        P = C[y, x]
        if P > maxi:
            maxi = P
            index = i
    return (C, index)
