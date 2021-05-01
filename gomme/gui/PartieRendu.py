from tkinter import *


class PartieRendu(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        zone_masque = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_masque, text="Résultat", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(zone_masque, text="En attente\n de masque", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10)

        self.label.pack()
        self.button.pack(ipadx=20, pady=40)

        zone_masque.place(x=900, y=220)
