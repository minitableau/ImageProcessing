from PIL import Image
from networkx.drawing.tests.test_pylab import plt

from src.filtres.Appliquer_masque import appliquer_masque

# img = Image.open("../Images/5Ballons.jpg")
# A = noir_et_blanc(img)
# A.show()

image = Image.open("../Images/Plage_avec_parasol.jpg")
masque = Image.open("../Masque/masque_parasol.jpg")
plage_parasol_noir = appliquer_masque(image, masque)

plt.imshow(plage_parasol_noir)
plt.show()
# plage_parasol_noir.save("../Résultats/Plage_parasol_noir.jpg")
# permet de sauvegarder l'image dans le dossier Résultats


image2 = Image.open("../Images/Plage_avec_arbre.jpg")
masque2 = Image.open("../Masque/masque_arbre.jpg")
plage_arbre_noir = appliquer_masque(image2, masque2)

plt.imshow(plage_arbre_noir)
plt.show()
# plage_arbre_noir.save("../Résultats/Plage_arbre_noir.jpg")
# permet de sauvegarder l'image dans le dossier Résultats


# Idée si l'image est en noir et blanc passer d'abord tout les pixel noir d'un couleur puis appliquer le filtre puis
# remettre la couleur noir
