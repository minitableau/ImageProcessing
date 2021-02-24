import numpy as np
from PIL import Image

from src.utilitaire.tableau import equals


def appliquer_masque(image: Image, masque: Image) -> Image:
    image_copie = np.copy(image)
    tableau_masque = np.array(masque)  # Transformation de l'image en tableau
    tableau_image = np.array(image_copie)
    lignes = tableau_masque.shape[0]
    colonnes = tableau_masque.shape[1]
    for x in range(0, lignes):
        for j in range(0, colonnes):
            if equals(tableau_masque[x, j], [0, 0, 0, 255]):  # la 4ème valeur correspond a la transparence
                tableau_image[x, j] = (0, 0, 0)

    image_copie = Image.fromarray(tableau_image)  # Transformation du tableau en image PIL
    return image_copie
