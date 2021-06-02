from gomme.utils.patch import Patch


def calculFiabilite(fiabilite: list, image_masque_copie: list, taille_cadre: int, tableau_masque: list,
                    coordonnees_contours: list) -> list:
    """Je crée une fonction qui prend en arguments deux tableaux, un entiers, un tableau et une liste,
    celle-ci permet de modifier la fiabilité de certain pixel et de verifier que l' air du carré ne varie pas (si
    elle varié - problème liée au zoom - alors on obtenait facilement une erreur -division par zero- ), elle nous
    renvoie un tableau """

    for k in range(len(coordonnees_contours)):
        px, py = coordonnees_contours[k]
        patch = Patch(image_masque_copie, taille_cadre, coordonnees_contours[k])
        x3, y3 = patch[0]
        x2, y2 = patch[1]
        compteur = 0
        air_carre = ((x2 - x3 + 1) * (y2 - y3 + 1))
        for x in range(x3, x2 + 1):
            for y in range(y3, y2 + 1):
                if tableau_masque[y, x] == 0:
                    compteur += fiabilite[y, x]
        fiabilite[py, px] = compteur / air_carre

    return fiabilite


def calculOrdre(image_masque_copie: list, taille_cadre: int, tableau_masque: list, coordonnees_contours: list,
                fiabilite: list) -> tuple:
    """Je crée une fonction qui prend en arguments un tableau, un entiers, un tableau, une liste et un tableau,
    celle-ci permet de déterminer par quel point commencer la reconstitution, toujours le point le plus haut du masque
     elle nous renvoie un tableau et un entier """

    C = calculFiabilite(fiabilite, image_masque_copie, taille_cadre, tableau_masque, coordonnees_contours)
    index = 0
    maxi = 0
    for i in range(len(coordonnees_contours)):
        x, y = coordonnees_contours[i]
        P = C[y, x]
        if P > maxi:
            maxi = P
            index = i

    return C, index
