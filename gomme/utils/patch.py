# On crée une zone autour du point voulu. On va crée un carré pour cela on calcul les angles inférieur gauche et
# supérieur droit on pourra alors facilement en faire un carré
def Patch(image, taille_cadre, coordo_point):
    px, py = coordo_point
    lignes, colonnes, channel = image.shape
    # on repère les cas ou le point serait trop proche d' un bord de l' image
    x3 = max(px - taille_cadre, 0)
    y3 = max(py - taille_cadre, 0)
    x2 = min(px + taille_cadre, colonnes - 1)
    y2 = min(py + taille_cadre, lignes - 1)
    return (x3, y3), (x2, y2)

