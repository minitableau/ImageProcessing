from tkinter import *

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

        zone_masque.place(x=525, y=220)

    def dessiner_masque(self):
        print("salut")

        if not self.parent.zone_image.contient_une_image():
            raise Exception("L'image n'a pas encore été chargée !!!!!!!!!")

        PaintMasque(self)
