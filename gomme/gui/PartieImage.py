from tkinter import *
from tkinter.filedialog import askopenfilename

import PIL.Image
from PIL import ImageTk


class PartieImage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.frame = Frame(parent, bg="#1E1E1E")

        self.label = Label(self.frame, text="Image", font=("Calibri", 40, "bold"), fg="#FF5F62", bg="#1E1E1E")
        self.label.pack()

        self.button = Button(self.frame, text="Importer", font=("Calibri", 24, "bold"), fg="#D9D9D9",
                             bg="#1E1E1E", borderwidth=10, command=self.importer_image)
        self.button.pack(ipadx=50, pady=20)

        self.pourcentage_scale = DoubleVar()

        self.resize_slider = Scale(self.frame, from_=10, to=100, orient=HORIZONTAL, variable=self.pourcentage_scale,
                                   length=300, fg="#D9D9D9", bg="#1E1E1E")
        self.resize_slider.pack_forget()

        self.size_description = Label(self.frame, text="width - height", bg="#1E1E1E", fg="#D9D9D9",
                                      font=("Calibri", 16))
        self.size_description.pack_forget()

        self.resize_slider.bind("<ButtonRelease-1>", self.maj_dimensions_image)

        self.frame.place(x=100, y=220)

    def importer_image(self):
        path = askopenfilename(filetypes=[("jpg files", ".jpg"), ("png files", ".png")])

        self.cache_image: PIL.Image = PIL.Image.open(path)

        tk_image = ImageTk.PhotoImage(self.cache_image.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.configure(fg="#00A6A5")
        self.pourcentage_scale.set(100)

        self.size_description["text"] = f"{self.cache_image.width} x {self.cache_image.height}"
        self.resize_slider.pack()
        self.size_description.pack()

    def contient_une_image(self):
        try:
            self.cache_image
        except:
            return False

        return True

    def maj_dimensions_image(self, event=None):

        slider_val = self.resize_slider.get()

        (width, height) = self.recuperer_dimensions()

        self.size_description["text"] = f"{width} x {height}"

    def recuperer_dimensions(self):

        slider_val = self.resize_slider.get()

        new_width = int(self.cache_image.width * (slider_val / 100))
        new_heigth = int(self.cache_image.height * (slider_val / 100))

        return new_width, new_heigth
