from tkinter import *
from tkinter.filedialog import askopenfilename

import PIL.Image
from PIL import ImageTk

from gomme.utils.zoom_ratio import recuperer_resolution_ecran, coef_zoom


class PartieImage(Frame):
    def __init__(self, parent):
        """Le constructeur permet de crée tout ce qui est en lien avec la partie image """

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
        """Je crée une fonction qui permet d' importer des images au format .jpg et .png, elle permet aussi de
        redimensionner automatiquement l' image si celle-ci est trop grande pour notre écran. Elle permet aussi de
        nous donner un apercu de notre image ou encore du redimensionnement  à l' aide du slider """

        path = askopenfilename(filetypes=[("jpg files", ".jpg"), ("png files", ".png")])

        self.cache_image: PIL.Image = PIL.Image.open(path)

        dimensions_ecran = recuperer_resolution_ecran()
        zoom = coef_zoom()
        coeff = 1
        resize = False

        if self.cache_image.width * zoom > dimensions_ecran[0] * 0.9:
            coeff = (dimensions_ecran[0] * 0.9) / self.cache_image.width
            resize = True
        elif self.cache_image.height * zoom > dimensions_ecran[1] * 0.9:
            coeff = (dimensions_ecran[1] * 0.9) / self.cache_image.height
            resize = True

        if resize == True:
            self.cache_image = self.cache_image.resize(
                (int(self.cache_image.width * coeff), int(self.cache_image.height * coeff)))

        tk_image = ImageTk.PhotoImage(self.cache_image.resize((300, 200)))

        self.button.image = tk_image
        self.button.configure(image=tk_image, height=200, width=200)

        self.label["fg"] = "#00A6A5"
        self.label.update()
        self.pourcentage_scale.set(100)  # de base 100% on peut alors réduire

        self.size_description["text"] = f"{self.cache_image.width} x {self.cache_image.height}"
        self.resize_slider.pack()
        self.size_description.pack()

        self.parent.zone_masque.reinitialiser_masque()
        self.parent.zone_rendu.image_importee()

    def contient_une_image(self) -> bool:
        """Je crée une fonction qui test si une image a été importé si c'est le cas elle nous renvoie True
        dans le cas inverse elle nous renvoie False"""

        try:
            self.cache_image
        except:
            return False

        return True

    def maj_dimensions_image(self, event=None):
        """Je crée une fonction qui affiche les dimensions du slider"""

        (width, height) = self.recuperer_dimensions()

        self.size_description["text"] = f"{width} x {height}"

    def recuperer_dimensions(self) -> tuple:
        """Je crée une fonction qui récupère les dimensions définies par l' utilisateur à l' aide du slider  """

        slider_val = self.resize_slider.get()

        new_width = int(self.cache_image.width * (slider_val / 100))
        new_heigth = int(self.cache_image.height * (slider_val / 100))

        return new_width, new_heigth
