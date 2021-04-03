from tkinter import *
from gomme.gui.create_mask import Paint

class fenetres():
    def __init__(self):
        self.f = Tk()
        x,y=1800,900
        self.f.geometry("{}x{}".format(x,y))
        self.f.minsize(1080, 720)
        Frame1 = Frame(self.f,bg='#41B6A0')
        champ_label = Label(self.f, text="Bienvenue sur notre TIPE !",font=("Calibri Light",75),bg='#41B6A0',fg='#FF8333')
        champ_label.pack(anchor='n')
        self.f.config(bg='#41B6A0')
        mask_button = Button(Frame1, text="Création du masque", command=self.test,bg='#33C1FF',font=("Calibri Light",25),relief='ridge',highlightbackground='red')
        mask_button.grid(row=0,column=0,padx=100)
        bouton2 = Button(Frame1, text="En cours de development", command=self.test, bg='#33C1FF', font=("Calibri Light", 25),relief='ridge')
        bouton2.grid(row=0,column=1)
        bouton3 = Button(Frame1, text="+Tard", command=self.test, bg='#33C1FF', font=("Calibri Light", 25),relief='ridge')
        bouton3.grid(row=0,column=2,padx=100)
        quit_button = Button(Frame1, text="Quitter", command=self.f.destroy, bg='#FF0000', font=("Calibri Light", 25),relief='ridge')
        xtemp, ytemp = x - 200, y - 75
        quit_button.grid(row=0,column=3)
        Frame1.pack(expand='YES')
        self.f.mainloop()

    def PagePrincipale(self):
        Paint()

    def test(self):
        self.f.withdraw()
        self.PagePrincipale()

if __name__ == '__main__':
    start = fenetres()


