import numpy as np
from numpy.core.multiarray import ndarray


def appliquer_masque(image: ndarray, masque: ndarray):
    image_copie: ndarray = np.copy(image)
    tableau_masque: ndarray = np.copy(masque)  # Transformation de l'image en tableau

    lignes, colonnes, channels = image_copie.shape

    for i in range(lignes):
        for j in range(colonnes):
            if tableau_masque[i, j] < 170:      #car les contours du masque ne sont pas totalement noir (1 seul valeur car lecture en noir|blanc)
                image_copie[i, j] = [0, 0, 0]   #[255, 255, 255] pour blanc ou [0, 0, 0] pour noir

    return image_copie
