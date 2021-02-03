from PIL import Image

from src.filtres.noir_et_blanc import noir_et_blanc

img = Image.open("../Image/5Ballons.jpg")
A=noir_et_blanc(img)
A.show()
