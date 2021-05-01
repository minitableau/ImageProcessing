import sys

import cv2
import numpy as np

from gomme import zone_de_remplissage
from gomme.filtres.masque import appliquer_masque

arg = sys.argv

if len(arg) != 3:
    print("Lancement du programme : py main.py chemin_image chemin_masque")
    # ./resources/images/plage_arbre.jpg ./resources/masques/masque_arbre.jpg
    exit()

chemin_image, chemin_masque, taille_cadre = (arg[1], arg[2], 3)

image = cv2.imread(chemin_image, 1)
masque = cv2.imread(chemin_masque, 0)

# le deuxième argument permet de lire l' image en noir et blanc (c'est un masque donc inutile de le lire en couleur),
# cela permet aussi donc de n' avoir que un entier dans le programme qui applique le masque

if image is None or masque is None:
    print(
        "Les chemins fournis pour l'image ou pour le masque ne sont pas valides (doivent être lancés depuis le "
        "dossier source du projet)")
    exit()

x_image, y_image, channels = image.shape
x_masque, y_masque = masque.shape

if x_image != x_masque or y_image != y_masque:
    print("La taille de l'image et la taille du masque sont différentes")
    exit()  # permet de sortir du programme

image_masque, source, original, omega = appliquer_masque(image, masque)
# source et original sont deux listes identiques copie de la liste fiabilite

cv2.imwrite(chemin_image[:-4] + "_avec_masque.png", image_masque)
# Permet d' avoir le meme chemin d' accès avec un nom explicite (on en incruste _avec_masque avant le .png)

image_masque_copie = np.copy(image_masque)
# on crée une copie de l' image avec les pixel mis en blanc la ou il y a le masque

result = np.ndarray(shape=image_masque.shape)

# classe implémentait par numpy crée une matrice (mettre shape car deuxième argument de la fonction python) xsize=ligne
# ,ysize=colonne,channel= cette matrice et remplie de 0

data = np.ndarray(shape=image_masque.shape[:2])

# classe implémentait par numpy crée une matrice (mettre shape car deuxième argument de la fonction python) xsize=ligne
# ,ysize=colonne  cette matrice et remplie de 0


Vrai_Faux = True  # pour le while

print("Démmarage de la reconstitution")
# print("Algorithme en fonctionnement") création du compteur de manière a montrer que ca avance

etape = 0  # initialisation de l' avancement

while Vrai_Faux:
    print(etape)  # permet de print l' avancement
    etape += 1  # incrémente pour le prochain passage
    lignes, colonnes = source.shape

    niveau_de_gris = cv2.cvtColor(image_masque_copie, cv2.COLOR_RGB2GRAY)
    # permet de convertir l' image (image_masque_copie) en couleur en noir et blanc

    gradientX = cv2.convertScaleAbs(cv2.Scharr(niveau_de_gris, cv2.CV_32F, 1, 0))
    gradientY = cv2.convertScaleAbs(cv2.Scharr(niveau_de_gris, cv2.CV_32F, 0, 1))

    for i in range(lignes):  # on parcours la copie de source : les lignes
        for j in range(colonnes):  # les colonnes
            if masque[i][j] == 1:
                # si cela est égal a 1 cad les endroit on ne met pas de masque (les endroit blanc sur le masque)

                gradientX[i][j] = 0
                gradientY[i][j] = 0

    gradientX, gradientY = gradientX / 255, gradientY / 255

    dOmega, normale = zone_de_remplissage.zone_de_remplissage(masque, source)
    # source correspond à la fiabilite (définie lors de l' application du masque)

    # ordre ( nous donnera pour savoir ou recommencer fiabilite, data) aura besoin de (image_masque_copie,
    # taille_cadre, masque, dOmega, normale, data, gradientX,gradientY, fiabilite)

    # Calcul du patch

    # Mise a jour des valeurs


    Vrai_Faux = False
    for i in range(lignes):
        for j in range(colonnes):
            if source[i, j] == 0:
                Vrai_Faux = True

    # on enregistre a chaque fois pour voir l' avancée
    cv2.imwrite(chemin_image[:-4] + "_résultat.jpg", image_masque_copie)





plage_parasol_noir = appliquer_masque(image, masque)

cv2.imshow('Image : Plage parasol noir', plage_parasol_noir)
cv2.waitKey()  # permet d' ouvrir la fenêtre

# cv2.imwrite(("./resources/resultats/Plage_arbre_noir.jpg"),plage_parasol_noir)
# permet de sauvegarder l' image dans le dossier résultats


# Commande de lancement : py main.py ./resources/images/plage_parasol.jpg ./resources/masques/masque_parasol.jpg
