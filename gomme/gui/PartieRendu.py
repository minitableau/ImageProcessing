from tkinter import *


class PartieRendu(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        disponible = False

        zone_rendu = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_rendu, text="Résultat", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(zone_rendu, text="En attente\n de l'image \net du masque", font=("Calibri", 24, "bold"),
                             fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10)#, command=self.demarrer_gomme)

        self.label.pack()
        self.button.pack(ipadx=20, pady=20)

        zone_rendu.place(x=900, y=220)

    def image_importee(self):
        self.button["text"] = "En attente du masque"
        self.button.update()

    def masque_pret(self):
        disponible = True
        self.button["text"] = "Appuyer pour\ncommencer"
        self.button.update()

    # def demarrer_gomme(self):
