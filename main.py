import sys

import cv2

from gomme.filtres.masque import appliquer_masque

arg = sys.argv

if len(arg) != 3:
    print("Lancement du programme : py PaintMasque.py chemin_image chemin_masque")
    # ./resources/images/plage_arbre.jpg ./resources/masques/masque_arbre.jpg
    exit()

chemin_image, chemin_masque, taille_cadre = (arg[1], arg[2], 3)

image = cv2.imread(chemin_image, 1)
masque = cv2.imread(chemin_masque, 0)

# le deuxième argument permet de lire l'fenetre en noir et blanc (c'est un masque donc inutile de le lire en couleur),
# cela permet aussi donc de n'avoir que un entier dans le programme qui applique le masque

if image is None or masque is None:
    print(
        "Les chemins fournis pour l'fenetre ou pour le masque ne sont pas valides (doivent être lancés depuis le "
        "dossier source du projet)")
    exit()

x_image, y_image, channels = image.shape
x_masque, y_masque = masque.shape

if x_image != x_masque or y_image != y_masque:
    print("La taille de l'fenetre et la taille du masque sont différentes")
    exit()  # permet de sortir du programme

plage_parasol_noir = appliquer_masque(image, masque)

cv2.imshow('Image : Plage parasol noir', plage_parasol_noir)
cv2.waitKey()  # permet d'ouvrir la fenêtre
# Idée si l'fenetre est en noir et blanc passer d'abord tout les pixel noir d'un couleur puis appliquer le filtre puis
# remettre la couleur noir

# cv2.imwrite(("./resources/resultats/Plage_arbre_noir.jpg"),plage_parasol_noir)
# permet de sauvegarder l'fenetre dans le dossier résultats


# Commande de lancement : py PaintMasque.py ./resources/images/plage_parasol.jpg ./resources/masques/masque_parasol.jpg
