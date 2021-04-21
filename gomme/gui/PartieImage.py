from tkinter import *
from tkinter.filedialog import askopenfilename

import PIL.Image
from PIL import ImageTk


class PartieImage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame = Frame(parent, bg="#1E1E1E")

        self.label = Label(self.frame, text="Image", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.button = Button(self.frame, text="Importer", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10, command=self.importer_image)

        self.label.pack()
        self.button.pack(ipadx=50, pady=20)

        self.frame.place(x=100, y=220)

        self.pourcentage_scale = DoubleVar()

    def importer_image(self):
        path = askopenfilename(filetypes=[("jpg files", ".jpg"), ("png files", ".png")])

        self.cache_image = PIL.Image.open(path)

        tk_image = ImageTk.PhotoImage(self.cache_image.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.configure(fg="#00A6A5")

        self.pourcentage_scale.set(100)

        resize_slider = Scale(self.frame, from_=0, to=100, orient=HORIZONTAL, variable=self.pourcentage_scale,
                              length=300, fg="#D9D9D9", bg="#1E1E1E")
        resize_slider.pack()

    def contient_une_image(self):
        try:
            self.cache_image
        except:
            return False

        return True
