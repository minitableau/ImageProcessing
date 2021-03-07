import numpy as np
from numpy.core.multiarray import ndarray


def appliquer_masque(image: ndarray, masque: ndarray):
    image_copie: ndarray = np.copy(image)
    tableau_masque: ndarray = np.copy(masque)  # Transformation de l'image en tableau

    lignes, colonnes = tableau_masque.shape

    for i in range(0, lignes):
        for j in range(0, colonnes):
            if tableau_masque[i, j] == 0:  # la 4ème valeur correspond a la transparence
                image_copie[i, j] = (0, 0, 0)

    return image_copie
