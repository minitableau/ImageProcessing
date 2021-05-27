from tkinter import *

import PIL
from PIL import ImageTk

from gomme.gui.PaintMasque import PaintMasque


class PartieMasque(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        zone_masque = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_masque, text="Masque", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(zone_masque, text="Définir", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10, command=self.dessiner_masque)

        self.label.pack()
        self.button.pack(ipadx=50, pady=20)

        self.masque = None
        zone_masque.place(x=500, y=220)

    def dessiner_masque(self):
        if not self.parent.zone_image.contient_une_image():
            raise Exception("L'image n'a pas encore été chargée !")

        PaintMasque(self)
        self.parent.zone_image.resize_slider.pack_forget()

    def afficher_masque(self):
        self.masque: PIL.Image = PIL.Image.open("masque.jpg")

        tk_image = ImageTk.PhotoImage(self.masque.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.update()

        self.parent.zone_rendu.masque_pret()

    def reinitialiser_masque(self):
        self.label.destroy()
        self.button.destroy()
        self.parent.zone_masque = PartieMasque(self.parent)
