from tkinter import *

import cv2
from PIL import ImageTk, ImageGrab

from gomme.utils.zoom_ratio import coef_zoom


# Problème il faut faire attention que l' image soit plus petite que la resolution de notre écran (resize avec le
# slider si ce n' est pas le cas) désormais fait automatiquement


class PaintMasque:

    def __init__(self, zone_masque):
        """Le constructeur permet de crée tout ce qui est en lien avec la création du masque """

        # TopLevel = Sous fenêtre ayant comme parent la fenêtre principale créée par Tk()
        self.fenetre = Toplevel(zone_masque.parent)

        self.fenetre.resizable(FALSE, FALSE)

        self.fenetre.protocol("WM_DELETE_WINDOW", self.close_paint)

        self.zone_parent = zone_masque
        zone_image = self.zone_parent.parent.zone_image

        self.w, self.h = zone_image.recuperer_dimensions()
        self.image = ImageTk.PhotoImage(zone_image.cache_image.resize((self.w, self.h)))

        # Récupération des dimensions de l'écran
        ws = self.fenetre.winfo_screenwidth()
        hs = self.fenetre.winfo_screenheight()

        # Calcul des coordonnées x & y pour placer la fenêtre au centre
        x = int(ws / 2 - self.w / 2)
        y = int(hs / 2 - self.h / 2) - 30

        self.fenetre.geometry(f'{self.w}x{self.h}+{x}+{y}')

        self.canvas = Canvas(self.fenetre, width=self.w, height=self.h)
        self.image_fond = self.canvas.create_image(0, 0, anchor="nw", image=self.image)
        self.setup()

        self.canvas.pack()

        self.fenetre.mainloop()

    def setup(self):
        """Je crée une fonction qui permet de paramétrer les deux cliques"""

        self.old_x = None
        self.old_y = None
        self.line_width = min(self.w, self.h) / 30
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<Button-3>', self.erase)

    def paint(self, event):
        """Je crée une fonction qui permet de dessiner sur le canvas"""

        if self.old_x and self.old_y:  # Commence au deuxième tick (maintient clic gauche)
            if abs(self.old_x - event.x) > (self.w / 100) or (abs(self.old_y - event.y) > (self.h / 100)):
                # calcul la distance entre le premier clic et le deuxième et regarde quelle soit très petite
                self.old_x = event.x
                self.old_y = event.y

            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.line_width, fill="red",
                                    capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def erase(self, event):
        """Je crée une fonction qui permet d' effacer notre dessin"""

        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)

    def close_paint(self):
        """Je crée une fonction qui permet la récupération du masque"""

        self.canvas.delete(self.image_fond)
        self.canvas.update()
        self.canvas.update()
        self.canvas.update()
        self.canvas.update()
        # Faire plusieurs update car sinon le screenshot est parfois pris trop rapidement et le canvas n' est pas
        # supprimer

        bbox = self.recuperer_canvas_entourage()
        grabcanvas = ImageGrab.grab(bbox=bbox)

        grabcanvas.save("masque.jpg")

        self.zone_parent.masque = cv2.imread("masque.jpg")
        self.zone_parent.afficher_masque()
        self.fenetre.destroy()

    def recuperer_canvas_entourage(self):
        """Je crée une fonction qui permet de retrouver où est placé la fenêtre"""

        ratio = coef_zoom()
        x = self.canvas.winfo_rootx() * ratio + self.canvas.winfo_x() * ratio
        y = self.canvas.winfo_rooty() * ratio + self.canvas.winfo_y() * ratio
        x1 = x + self.canvas.winfo_width() * ratio
        y1 = y + self.canvas.winfo_height() * ratio
        box = (x, y, x1, y1)
        print('box = ', box)
        return box
