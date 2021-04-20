from tkinter import *


class PartieImage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        zone_image = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_image, text="Image", font=("Calibri", 40, "bold"), fg="#01A2A1", bg="#1E1E1E")
        self.button = Button(zone_image, text="Importer", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10)

        self.label.pack()
        self.button.pack(ipadx=50, pady=40)

        zone_image.place(x=100, y=220)
