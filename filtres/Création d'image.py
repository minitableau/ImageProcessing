import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

image = np.zeros((100, 200, 3), dtype=np.uint8)
plt.imshow(image)
plt.show()
# permet de crée une image toute noir

imagepil = Image.open("../resources/images/plage_arbre.jpg")
im = np.array(imagepil)
plt.imshow(im)
plt.show()

imageCOPY = np.copy(imagepil)


def lignes_colonnes(tableau: list) -> list:
    return tableau.shape


a = lignes_colonnes(im)[0]
b = lignes_colonnes(im)[1]
print("L'image possède", a - 1, "lignes et", b - 1, "colones")

print(im[100, 120])
print(im[200, 250])  # pixel en bas a droite blanc
# Valeur du rouge puis vert puis bleu

im[200, 250] = (0, 0, 255)
plt.imshow(im)
plt.show()
# permet de mettre le pixel en bas a gauche en bleu


imagepil = Image.fromarray(im)  # Transformation du tableau en image PIL
imagepil.save("../../test/Imagemodif.jpg")  # sauvegarde de l'image modifié
