from tkinter import *
from tkinter.colorchooser import askcolor


class PaintMasque:
    DEFAULT_PEN_SIZE = 20.0
    DEFAULT_COLOR = 'black'

    def __init__(self, zone_masque):
        self.fenetre = Tk()
        self.fenetre.config(bg='#CD5C5C')

        background = Label(self.fenetre, image=zone_masque.parent.zone)

        self.c = Canvas(self.fenetre, bg='white', width=1700, height=800)
        self.c.grid(row=1, columnspan=5)

        self.pen_button = Button(self.fenetre, text='stylo', command=self.use_pen, bg='#FA8072')
        self.pen_button.grid(row=0, column=0)

        self.save_button = Button(self.fenetre, text='sauvegarder', command=self.use_save, bg='#FA8072')
        self.save_button.grid(row=0, column=1)

        self.color_button = Button(self.fenetre, text='couleur', command=self.choose_color, bg='#FA8072')
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.fenetre, text='gomme', command=self.use_eraser, bg='#FA8072')
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.fenetre, from_=1, to=30, orient=HORIZONTAL, bg='#FA8072')
        self.choose_size_button.grid(row=0, column=4)

        self.setup()
        self.fenetre.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_save(self):
        self.activate_button(self.save_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()

# L'option sauvegarder est encore a faire elle permet d'écrire pour le moment
