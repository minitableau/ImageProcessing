from gomme.utils.patch import Patch

def calculConfiance(confiance, im, taillecadre, masque, dOmega):
    for k in range(len(dOmega)):
        px, py = dOmega[k]
        patch = Patch(im, taillecadre, dOmega[k])
        x3, y3 = patch[0]
        x2, y2 = patch[1]
        compteur = 0
        taille_psi_p = ((x2 - x3 + 1) * (y2 - y3 + 1))
        for x in range(x3, x2 + 1):
            for y in range(y3, y2 + 1):
                if masque[y, x] == 0:
                    compteur += confiance[y, x]
        confiance[py, px] = compteur / taille_psi_p
    return (confiance)


def calculPriority(im, taillecadre, masque, dOmega, confiance):
    C = calculConfiance(confiance, im, taillecadre, masque, dOmega)
    index = 0
    maxi = 0
    for i in range(len(dOmega)):
        x, y = dOmega[i]
        P = C[y, x]
        if P > maxi:
            maxi = P
            index = i
    return (C, index)
