from tkinter import *

from PIL import ImageTk


class PaintMasque:

    def __init__(self, zone_masque):
        self.fenetre = Toplevel(zone_masque.parent)
        # self.fenetre.config(bg='#CD5C5C')

        self.zone_parent = zone_masque
        zone_image = self.zone_parent.parent.zone_image

        self.w, self.h = zone_image.recuperer_dimensions()
        self.image = ImageTk.PhotoImage(zone_image.cache_image.resize((self.w, self.h)))

        # Récupération des dimensions de l'écran
        ws = self.fenetre.winfo_screenwidth()
        hs = self.fenetre.winfo_screenheight()

        # Calcul des coordonnées x & y pour placer la fenêtre au centre
        x = int(ws / 2 - self.w / 2)
        y = int(hs / 2 - self.h / 2)

        self.fenetre.geometry(f'{self.w}x{self.h}+{x}+{y}')
        #
        # background = Label(self.fenetre, image=image)
        # background.image = image
        # background.configure(image=image, height=h, width=w)
        # background.pack()

        self.canvas = Canvas(self.fenetre, width=self.w, height=self.h)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)
        self.setup()

        self.canvas.pack()

        self.fenetre.mainloop()

    def setup(self):
        print("turbo")
        self.old_x = None
        self.old_y = None
        self.line_width = min(self.w, self.h) / 30
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<Button-3>', self.erase)

    # def use_eraser(self):
    #    self.activate_button(self.eraser_button, eraser_mode=True)

    def paint(self, event):

        if self.old_x and self.old_y:
            if abs(self.old_x - event.x) > (self.w / 100) or (abs(self.old_y - event.y) > (self.h / 100)):
                self.old_x = event.x
                self.old_y = event.y

            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.line_width, fill="red",
                                    capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def erase(self, event):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)
