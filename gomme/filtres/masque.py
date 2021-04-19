import numpy as np
from numpy.core.multiarray import ndarray


def appliquer_masque(image: ndarray, masque: ndarray):

    L=[]
    image_copie: ndarray = np.copy(image)
    tableau_masque: ndarray = np.copy(masque)  # Transformation de l'image en tableau
    fiabilité = np.copy(masque)

    lignes, colonnes, channels = image_copie.shape

    for i in range(lignes):
        for j in range(colonnes):
            if tableau_masque[i, j] < 170:  # car les contours du masque ne sont pas totalement noir (1 seul valeur car lecture en noir|blanc)

                image_copie[i, j] = [255, 255, 255]  # [255, 255, 255] pour blanc ou [0, 0, 0] pour noir
                L.append([i, j])
                tableau_masque[i, j] = 1  # on met dans le masque la valeur de 1 de maniere a les retrouvé plus facilement que avec le tau
                fiabilité[i, j] = 0  # mettre un . ? #dans la copie du masque appélé fiabilité on place des 0
            else:
                masque[i, j] = 0  # on met dans le masque la valeur de 1 de maniere a les retrouvé plus facilement que avec le tau
                fiabilité[i, j] = 1  # mettre un . ? #dans la copie du masque appélé fiabilité on place des 1

    source = np.copy(fiabilité)  # copie de la liste confiance crée au dessus assigné a la valeur source  [que des 0 ??]
    original = np.copy(fiabilité)  # copie de la liste confiance crée au dessus assigné a la valeur originial [que des 0 ??]

    return image_copie,source,original,L

# On cherchera a incruster une confiance pour ensuite pouvoir repérer les pixels qui pourront être utiliser pour
# recrée l'image

