import sys

import cv2

import numpy as np

from gomme.filtres.masque import appliquer_masque

arg = sys.argv

if len(arg) != 3:
    print("Lancement du programme : py main.py chemin_image chemin_masque")
    # ./resources/images/plage_arbre.jpg ./resources/masques/masque_arbre.jpg
    exit()

chemin_image, chemin_masque, taille_cadre = (arg[1], arg[2], 3)

image = cv2.imread(chemin_image, 1)
masque = cv2.imread(chemin_masque, 0)

# le deuxième argument permet de lire l'image en noir et blanc (c'est un masque donc inutile de le lire en couleur),
# cela permet aussi donc de n'avoir que un entier dans le programme qui applique le masque

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


image_masque, source, original , omega = appliquer_masque(image, masque)

cv2.imwrite(chemin_image[:-4] + "_avec_masque.png",image_masque) # Permet d'avoir le meme chemin d'acces avec un nom explicite (on en incruste _avec_masque avant le .png)






dOmega = []  # creation d un liste vide dOmega
normale = []  # creation d un liste vide normale

image_masque_copie = np.copy(image_masque)  # on crée une copie de l'image avec les pixel mis en blanc la ou il y a le masque
result = np.ndarray(shape=image.shape)  # classe implémentait par numpy crée une matrice (mettre shape car deuxieme argument de la fonction python) xsize=ligne ,ysize=colone,channel= cette matrice et remplie de 0
data = np.ndarray(shape=image.shape[:2])  # classe implémentait par numpy crée une matrice (mettre shape car deuxieme argument de la fonction python) xsize=ligne ,ysize=colone  cette matrice et remplie de 0

Vrai_Faux = True  # pour le while
print("Démmarage de la reconstitution")  # print("Algorithme en fonctionnement") création du compteur de maniere a montrer que ca avance
Etape = 0  # initialisation de l'avancement



while Vrai_Faux:
    print(Etape) #permet de print l'avancement
    Etape += 1 #incrémente pour le prochain passage
    lignes, colonnes = source.shape


    niveau_de_gris = cv2.cvtColor(image_masque_copie, cv2.COLOR_RGB2GRAY) # permet de convertir l'image (image_masque_copie) en couleur en noir et blanc

    gradientX = cv2.convertScaleAbs(cv2.Scharr(niveau_de_gris, cv2.CV_32F, 1, 0))
    gradientY = cv2.convertScaleAbs(cv2.Scharr(niveau_de_gris, cv2.CV_32F, 0, 1))

    for i in range(lignes): # on parcours la copie de confiance  les lignes
        for j in range(colonnes): # les colonnes
            if masque[i][j] == 1: #si cela est égal a 1 c est a dire les endroit on ne met pas de masque (les endroit blanc sur le masque)
                gradientX[i][j] = 0
                gradientY[i][j] = 0
    gradientX, gradientY = gradientX / 255, gradientY / 255







    Vrai_Faux = False
    for i in range(lignes):
        for j in range(colonnes):
            if source[i, j] == 0:
                Vrai_Faux = True

        # on enregistre a chaque fois pour voir l'avancée
    cv2.imwrite(chemin_image[:-4] + "_resultat.jpg", image_masque_copie)








plage_parasol_noir = appliquer_masque(image, masque)

cv2.imshow('Image : Plage parasol noir', plage_parasol_noir)
cv2.waitKey()  # permet d'ouvrir la fenêtre
# Idée si l'image est en noir et blanc passer d'abord tout les pixel noir d'un couleur puis appliquer le filtre puis
# remettre la couleur noir

# cv2.imwrite(("./resources/resultats/Plage_arbre_noir.jpg"),plage_parasol_noir)
# permet de sauvegarder l'image dans le dossier résultats


# Commande de lancement : py main.py ./resources/images/plage_parasol.jpg ./resources/masques/masque_parasol.jpg
