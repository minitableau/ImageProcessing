import numpy as np
from numpy.core.multiarray import ndarray

from gomme.utils.tableau import equals


def appliquer_masque(image: ndarray, masque: ndarray):
    tableau_image: ndarray = np.copy(image)
    tableau_masque: ndarray = np.copy(masque)  # Transformation de l' image en tableau
    fiabilite = np.copy(masque)

    lignes, colonnes = tableau_image.shape[:2]

    for i in range(lignes):
        for j in range(colonnes):
            if equals(tableau_masque[i, j], [255, 0, 0]):
                # car les contours du masque ne sont pas totalement noir (1 seul valeur car lecture en noir|blanc)
                tableau_image[i, j] = [255, 255, 255]  # [255, 255, 255] pour blanc ou [0, 0, 0] pour noir
                tableau_masque[i, j] = 1
                # on met dans le masque la valeur de 1 de manière a les retrouvé plus facilement que avec le tau
                fiabilite[i, j] = 0
                # mettre un . ? #dans la copie du masque appelé fiabilité on place des 0
            else:
                tableau_masque[i, j] = 0
                # on met dans le masque la valeur de 1 de manière a les retrouvé plus facilement que avec le tau
                fiabilite[i, j] = 1
                # mettre un . ? #dans la copie du masque appelé fiabilité on place des 1

        source = np.copy(fiabilite)  # copie de la liste confiance crée au dessus assigné a la valeur source
        original = np.copy(fiabilite)  # copie de la liste confiance crée au dessus assigné a la valeur original

    return tableau_image, tableau_masque, fiabilite, source, original

# On cherchera a incruster une confiance pour ensuite pouvoir repérer les pixels qui pourront être utiliser pour
# recrée l'image
