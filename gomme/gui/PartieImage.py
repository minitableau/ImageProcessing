from tkinter import *
from tkinter.filedialog import askopenfilename

import PIL.Image
from PIL import ImageTk


class PartieImage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        zone_image = Frame(parent, bg="#1E1E1E")

        self.label = Label(zone_image, text="Image", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(zone_image, text="Importer", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10, command=self.importer_image)

        self.label.pack()
        self.button.pack(ipadx=50, pady=40)

        zone_image.place(x=100, y=220)

    def importer_image(self):
        path = askopenfilename(filetypes=[("jpg files", ".jpg"), ("png files", ".png")])

        self.buffer_cache_image = PIL.Image.open(path)

        tk_image = ImageTk.PhotoImage(self.buffer_cache_image.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.configure(fg="#00A6A5")

