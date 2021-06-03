import time

import cv2
import numpy as np

from gomme.calcul_meilleur_patch import calculPatch
from gomme.filtres.masque import appliquer_masque
from gomme.gui import PartieRendu
from gomme.mise_a_jour import MAJ
from gomme.ordre import calculFiabilite
from gomme.zone_de_remplissage import zone_de_remplissage

start_time = time.thread_time()


# arguments = sys.argv
#
# if len(arguments) != 3:
#     print("Lancement du programme : py main.py chemin_image chemin_masque")
#     # ./resources/images/plage_arbre.jpg ./resources/masques/masque_arbre.jpg
#     exit()
#
# chemin_image, chemin_masque, taille_cadre = (arguments[1], arguments[2], 3)
#
# image = cv2.imread(chemin_image, 1)
# masque = cv2.imread(chemin_masque, 0)
#
# # le deuxième argument permet de lire l' image en noir et blanc (c'est un masque donc inutile de le lire en couleur),
# # cela permet aussi donc de n' avoir que un entier dans le programme qui applique le masque
#
# if image is None or masque is None:
#     print(
#         "Les chemins fournis pour l' image ou pour le masque ne sont pas valides (doivent être lancés depuis le "
#         "dossier source du projet)")
#     exit()
#
# lignes_image, colonnes_image, channels = image.shape
# lignes_masque, colonnes_masque = masque.shape
#
# if lignes_image != lignes_masque or colonnes_image != colonnes_masque:
#     print("La taille de l' image et la taille du masque sont différentes")
#     exit()  # permet de sortir du programme

# Cela permet de délier l' interface

def processus(zone_rendu: PartieRendu, image, masque) -> None:
    """Je crée une fonction qui prend en argument un class et deux images, celle-ci appelle toutes les autres
    fonction, il s' agit de la fonction principale , elle ne retourne rien mais elle enregistre le résultat au fur est
    à mesure (en écrasant l' ancient) dans le dossier ressources resultat. """

    taille_cadre = 3

    open_cv_image = np.array(image)

# Permet d' enlever la composante transparente

    if len(open_cv_image[0][0]) != 3:
        open_cv_image2=[]
        for i in range(len(open_cv_image)):
            L2=[]
            for j in range(len(open_cv_image[i])):
                L = []
                for k in range(3):
                    L.append(open_cv_image[i][j][k])
                L2+=[L]
            open_cv_image2+=[L2]

    open_cv_image2 = np.array(open_cv_image2)

    image = open_cv_image2[:, :, ::-1].copy()
    # Permet de passer une image PIL RGB a un BGR lu par open CV (ajout de l' interface ne supportant uniquement des
    # PIL d' ou la conversion)

    image_avec_masque, tableau_masque, fiabilite, source, original = appliquer_masque(image, masque)
    # source et original sont deux listes identiques copie de la liste fiabilite

    cv2.imwrite("../../resources/masques/" + str(start_time) + "_avec_masque.png", image_avec_masque)
    # Permet d' avoir le meme chemin d' accès avec un nom explicite (on en incruste _avec_masque avant le .png)

    image_masque_copie = np.copy(image_avec_masque)
    # on crée une copie de l' image avec les pixel mis en blanc la ou il y a le masque

    Vrai_Faux = True  # pour le while

    print("Démarrage de la reconstitution \nSoyez patient ne fermé pas l' interface")

    etape = 0  # initialisation de l' avancement
    index = 0

    while Vrai_Faux:
        print(etape)  # permet de print l' avancement
        etape += 1  # incrémente pour le prochain passage
        lignes, colonnes = source.shape

        # Methode avec laquelle nous obtenions un meilleur résultat mais beaucoup plus longue
        # Celle-ci est incomplète mais donne une idée de comment nous procédions

        # image_noir_et_blanc = cv2.cvtColor(image_masque_copie, cv2.COLOR_RGB2GRAY)
        # # permet de convertir l' image (image_masque_copie) en couleur en noir et blanc
        #
        # gradientX = cv2.convertScaleAbs(cv2.Scharr(image_noir_et_blanc, cv2.CV_32F, 1, 0))
        # gradientY = cv2.convertScaleAbs(cv2.Scharr(image_noir_et_blanc, cv2.CV_32F, 0, 1))
        #
        # for i in range(lignes):
        #     for j in range(colonnes):
        #         if tableau_masque[i][j] == 0:
        #             gradientX[i][j] = 0
        #             gradientY[i][j] = 0

        coordonnees_contours = zone_de_remplissage(tableau_masque)

        fiabilite = calculFiabilite(fiabilite, image_masque_copie, taille_cadre, tableau_masque, coordonnees_contours)

        ciblem, pp = calculPatch(coordonnees_contours, index, image_masque_copie, original, tableau_masque,
                                 taille_cadre)

        image_masque_copie, fiabilite, source, tableau_masque = MAJ(image_masque_copie, fiabilite, source,
                                                                    tableau_masque, coordonnees_contours, pp, ciblem,
                                                                    index, taille_cadre)

        Vrai_Faux = False
        for i in range(lignes):
            for j in range(colonnes):
                if source[i, j] == 0:
                    Vrai_Faux = True

        # on enregistre a chaque fois pour voir l' avancée
        cv2.imwrite("../../resources/resultats/" + str(start_time) + "_resultat.jpg", image_masque_copie)
        time.sleep(5)  # de manière a que l' image soit enregistrer cela peu prendre un petit peu de temps
        # l' implementation de l' interface allonge alors encore un peu le temps de notre programme
        zone_rendu.refresh_image(etape)

        if not Vrai_Faux:
            zone_rendu.algorithme_termine()
            cv2.imshow('Résultat', image_masque_copie)

    # cv2.imwrite(("./resources/resultats/Plage_arbre_noir.jpg"),plage_parasol_noir)
    # permet de sauvegarder l' image dans le dossier résultats

    # Commande type de lancement lorsque l' interface n' est pas liée :
    # py main.py ./resources/images/plage_parasol.jpg ./resources/masques/masque_parasol.jpg
