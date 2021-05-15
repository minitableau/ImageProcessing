from gomme.utils.patch import Patch

def update(im, confiance, source, masque, dOmega, point, list, index, taillecadre):
    p = dOmega[index]
    patch = Patch(im, taillecadre, p)
    x1, y1 = patch[0]
    px, py = point
    for (i, j) in list:
        im[y1 + i, x1 + j] = im[py + i, px + j]
        confiance[y1 + i, x1 + j] = confiance[py, px]
        source[y1 + i, x1 + j] = 1
        masque[y1 + i, x1 + j] = 0
    return (im, confiance, source, masque)

