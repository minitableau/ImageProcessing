from tkinter import *

import PIL
from PIL import ImageTk

from gomme.gui.PaintMasque import PaintMasque


class PartieMasque(Frame):
    def __init__(self, parent):
        """Le constructeur permet de crée tout ce qui est en lien avec la partie masque """

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
        """Je crée une fonction qui  vérifie que l' image a été chargé si ce n' est pas le cas elle nous affiche un
        message d' erreur dans la console """

        if not self.parent.zone_image.contient_une_image():
            raise Exception("L'image n'a pas encore été chargée !")

        PaintMasque(self)
        self.parent.zone_image.resize_slider.pack_forget()

    def afficher_masque(self):
        """Je crée une fonction qui nous donne un apercu du masque sur l' interface"""

        self.masque: PIL.Image = PIL.Image.open("masque.jpg").convert('L')

        tk_image = ImageTk.PhotoImage(self.masque.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.update()

        self.parent.zone_rendu.masque_pret()

    def reinitialiser_masque(self):
        """Je crée une fonction qui permet de réinitialiser_masque """

        self.label.destroy()
        self.button.destroy()
        self.parent.zone_masque = PartieMasque(self.parent)
