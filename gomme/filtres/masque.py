import numpy as np
from numpy.core.multiarray import ndarray


def appliquer_masque(image: ndarray, masque: ndarray) -> tuple:
    """Je crée une fonction qui prend en argument deux tableaux elle applique alors le masque a l' image et elle nous
    renvoie alors cinq tableaux (fiabilite, source, original sont des copies les uns des autres) """

    tableau_image: ndarray = np.copy(image)
    tableau_masque: ndarray = np.copy(masque)
    fiabilite = np.copy(masque)

    lignes, colonnes = tableau_image.shape[:2]

    for i in range(lignes):
        for j in range(colonnes):
            if tableau_masque[i, j] < 120:
                # Le contour du masque peut ne pas être totalement noir en fonction logiciel avec lequel il est crée
                # avec notre interface il est uniforme (au niveau de la couleur) mais il est gris d' ou le taux peut
                # élevé 120 est un valeur cohérente (1 seul valeur car le masque est lu en noir/blanc)
                tableau_image[i, j] = [255, 255, 255]  # [255, 255, 255] pour blanc ou [0, 0, 0] pour noir
                tableau_masque[i, j] = 1
                # on met dans le masque la valeur de 1 de manière a les retrouvé plus facilement que avec le taux
                fiabilite[i, j] = 0
            else:
                tableau_masque[i, j] = 0
                # on met dans le masque la valeur de 1 de manière a les retrouvé plus facilement que avec le taux
                fiabilite[i, j] = 1

        source = np.copy(fiabilite)  # copie de la liste confiance crée au dessus assigné a la valeur source
        original = np.copy(fiabilite)  # copie de la liste confiance crée au dessus assigné a la valeur original
        # Ces copies sont utiles plus tard car on va faire varier fiabilité mais on aura encore besoin de l' original
    return tableau_image, tableau_masque, fiabilite, source, original
