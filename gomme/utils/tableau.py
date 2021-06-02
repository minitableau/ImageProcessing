def equals(tab1: list, tab2: list) -> bool:
    """Je crée une fonction qui prend en argument deux tableaux, celle-ci nous renvoie un boolean en fonction de si
    ces tableaux sont égaux (True)ou non(False) """
    if len(tab1) != len(tab2):
        return False

    for i in range(len(tab1)):
        if tab1[i] != tab2[i]:
            return False

    return True
