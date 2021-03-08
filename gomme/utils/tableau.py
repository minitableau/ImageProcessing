
def equals(tab1: list, tab2: list) -> bool:
    if len(tab1) != len(tab2):
        return False

    for i in range(len(tab1)):
        if tab1[i] != tab2[i]:
            return False

    return True
