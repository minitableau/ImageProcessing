from tkinter import *

import PIL
from PIL import ImageTk

from main import processus, start_time


class PartieRendu(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.disponible = False

        zone_rendu = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_rendu, text="Résultat", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(zone_rendu, text="En attente\n de l'image \net du masque", font=("Calibri", 24, "bold"),
                             fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10, command=self.demarrer_gomme)

        self.label.pack()
        self.button.pack(ipadx=20, pady=20)

        zone_rendu.place(x=900, y=220)

    def image_importee(self):
        self.button["text"] = "En attente du masque"
        self.button.update()

    def masque_pret(self):
        self.disponible = True
        self.button["text"] = "Appuyer pour\ncommencer"
        self.button.update()

    def demarrer_gomme(self):
        if self.disponible:
            processus(self, self.parent.zone_image.cache_image, self.parent.zone_masque.masque)

    def refresh_image(self):
        resultat: PIL.Image = PIL.Image.open("../../resources/resultats/" + str(start_time) + "_resultat.jpg")

        tk_image = ImageTk.PhotoImage(resultat.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.update()
