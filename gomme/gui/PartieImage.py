from tkinter import *


class PartieImage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="red")

        zone_image = Frame(parent, bg="#1E1E1E")

        label = Label(zone_image, text="Image", font=("Calibri", 40, "bold"), fg="#01A2A1", bg="#1E1E1E")
        button = Button(zone_image, text="Importer", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                        bg="#1E1E1E", borderwidth=10)

        label.pack()
        button.pack(ipadx=50, pady=40)

        zone_image.pack(padx=120, pady=70, anchor="w")
