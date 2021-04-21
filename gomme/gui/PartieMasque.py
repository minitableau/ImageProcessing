from tkinter import *


class PartieMasque(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        zone_masque = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_masque, text="Masque", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(zone_masque, text="Définir", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10)

        self.label.pack()
        self.button.pack(ipadx=50, pady=20)

        zone_masque.place(x=525, y=220)
