from PIL.Image import Image


def noir_et_blanc(image: Image) -> Image:
    colonne, ligne = image.size
    tabPixel = image.load()
    for i in range(ligne):
        for j in range(colonne):
            pixel = tabPixel[j, i]  # récupération du pixel
            # calcul du poids de chaque composante du gris dans le pixel (CIE709)
            gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])
            # gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
            p = (gris, gris, gris)
            # composition de la nouvelle image
            tabPixel[j, i] = p
    return image
