from tkinter import *
import random


def f1():
    fenetre = Tk()
    fenetre.title('pfc')
    cadre = Frame(fenetre, width=300, height=10, borderwidth=1)
    cadre2 = Frame(fenetre, width=300, height=10, borderwidth=1)

    q = StringVar()
    rage = Button(fenetre, text="Rage quite", command=fenetre.quit)
    exp_label = Label(fenetre, text="Fait ton chois")
    pierre = Button(fenetre, text="pierre", command=pierref)
    ciseaux = Button(fenetre, text="ciseaux", command=ciseauxf)
    feuille = Button(fenetre, text="feuille", command=feuillef)
    


    cadre.pack(fill=BOTH)
    exp_label.pack()
    pierre.pack()
    feuille.pack()
    ciseaux.pack()
    rage.pack()
    cadre2.pack(fill=BOTH)
	
    fenetre.mainloop()

def f2():
    fenetre2 = Tk()
    fenetre2.title('de base ct censer juste etre un teste')
    exp_label = Label(fenetre2, text="c un jeux simple de pierre feuille ciseaux")
    button = Button(fenetre2, text="jouer", command=f1)
    exp_label.pack()
    button.pack()
    fenetre2.mainloop()


def pierref():
    pfc = quoi("coucou")
    fenetrep = Tk()
    fenetrep.title('Chois pierre')
    cadre = Frame(fenetrep, width=300, height=10, borderwidth=1)
    cadre2 = Frame(fenetrep, width=300, height=10, borderwidth=1)
    ega_label = Label(fenetrep, text="égalité")
    loos_label = Label(fenetrep, text="Tu a perdu(e), looser!!!!")
    win_label = Label(fenetrep, text="Tu a gagner, GG")
    choisEnemi_label = Label(fenetrep, text=("Ton énemi a choisi ", pfc))
    
    
    cadre.pack(fill=BOTH)
    choisEnemi_label.pack()
    if pfc == "pierre":
        ega_label.pack()
        
    elif pfc == "feuille":
        loos_label.pack()
    else:
        win_label.pack()
    cadre2.pack(fill=BOTH)
    fenetrep.mainloop()
    
def ciseauxf():
    pfc = quoi("coucou")
    fenetref = Tk()
    fenetref.title('Chois ciseaux')
    cadre = Frame(fenetref, width=300, height=10, borderwidth=1)
    cadre2 = Frame(fenetref, width=300, height=10, borderwidth=1)
    ega_label = Label(fenetref, text="égalité")
    loos_label = Label(fenetref, text="Tu a perdu(e), looser!!!!")
    win_label = Label(fenetref, text="Tu a gagner, GG")
    choisEnemi_label = Label(fenetref, text=("Ton énemi a choisi ", pfc))
    
    
    cadre.pack(fill=BOTH)
    choisEnemi_label.pack()
    if pfc == "pierre":
        loos_label.pack()  
    elif pfc == "feuille":
        win_label.pack()
    else:
        ega_label.pack()
    cadre2.pack(fill=BOTH)
    fenetref.mainloop()

def feuillef():
    pfc = quoi("coucou")
    fenetrec = Tk()
    fenetrec.title('Chois feuille')
    cadre = Frame(fenetrec, width=300, height=10, borderwidth=1)
    cadre2 = Frame(fenetrec, width=300, height=10, borderwidth=1)
    ega_label = Label(fenetrec, text="égalité")
    loos_label = Label(fenetrec, text="Tu a perdu(e), looser!!!!")
    win_label = Label(fenetrec, text="Tu a gagner, GG")
    choisEnemi_label = Label(fenetrec, text=("Ton énemi a choisi ", pfc))
    
    
    cadre.pack(fill=BOTH)
    choisEnemi_label.pack()
    if pfc == "pierre":
        win_label.pack()  
    elif pfc == "feuille":
        ega_label.pack()
    else:
        loos_label.pack()
    cadre2.pack(fill=BOTH)
    fenetrec.mainloop()

def quoi(q):
    
    q=random.choice(['pierre', 'feuille', 'ciseau'])
    return q
    


f1()
