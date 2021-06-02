from tkinter import *

from gomme.gui.PartieImage import PartieImage
from gomme.gui.PartieMasque import PartieMasque
from gomme.gui.PartieRendu import PartieRendu


class Interface(Tk):
    def __init__(self, parent):
        """Le constructeur permet de crée le bouton fermé en haut à droite de l' interface, de placé l' interface au
        centre de notre écran, de placé le titre en haut au milieu """
        Tk.__init__(self, parent)

        self.parent = parent

        w, h = 1280, 720

        # Récupération des dimensions de l' écran
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        # Calcul des coordonnées x & y pour placer la fenêtre au centre
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)

        self.geometry(f'{w}x{h}+{x}+{y}')

        self.overrideredirect(1)
        self.resizable(FALSE, FALSE)

        self.config(bg="#1E1E1E")

        closeButton = Button(self, text="x", font=("Calibri", 22, "bold"), fg="#FF2010", bg="#1E1E1E", bd=0,
                             command=self.destroy)

        closeButton.pack(ipadx=10, ipady=5, anchor="ne")

        titre = Label(self, text="Bienvenue sur notre TIPE !", font=("Calibri", 42, "bold"),
                      fg="#D9D9D9",
                      bg="#1E1E1E")

        titre.pack()

        self.zone_image = PartieImage(self)
        self.zone_masque = PartieMasque(self)
        self.zone_rendu = PartieRendu(self)

        self.mainloop()


if __name__ == '__main__':
    start = Interface(None)
