## Morpion EKIP

from tkinter import *
from tkinter import messagebox
import tkinter.font as font
window=Tk()
window.configure(bg="black")
window.resizable(height=False,width=False)


window.title("Morpion")
labelf=Label(window,text="Morpion by Ekip",bg="black",fg="orange")
labels=font.Font(size=19)
labelf['font']=labels
f=font.Font(size=110)
labelf.grid(row=0,column=2,pady=1,padx=1)

stop=False
clicked=True
pierre=True
stylo=True
souris=True
bureau=True
papier=True
ciseaux=True
compteur=0
points1=0
points2=0


## Désactiver tout les bouttons

def disbld_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

## Vérification si un joueur a gagné

def gagne(): # modifier
    check_O(b1,b2,b3)
    check_O(b4,b5,b6)
    check_O(b7,b8,b9)
    check_O(b1,b4,b7)
    check_O(b2,b5,b8)
    check_O(b3,b6,b9)
    check_O(b1,b5,b9)
    check_O(b3,b5,b7)

    check_X(b1,b2,b3)
    check_X(b4,b5,b6)
    check_X(b7,b8,b9)
    check_X(b1,b4,b7)
    check_X(b2,b5,b8)
    check_X(b3,b6,b9)
    check_X(b1,b5,b9)
    check_X(b3,b5,b7)


def check_X(A,B,C):
   global points1, compteur, stop
   labelf=Label(window,text="Joueur : "+str(points1),bg="black",fg="white")
   labels=font.Font(size=15)
   labelf['font']=labels
   f=font.Font(size=110)
   labelf.grid(row=0,column=1,pady=1,padx=1)
   if A["text"]+B["text"]+C["text"]=="XXX":
    A.config(bg="green")
    B.config(bg="green")
    C.config(bg="green")
    stop=True
    points1+=1
    messagebox.showinfo(title=None,message="Fin du jeu ! Bravo, tu as gagné la partie !")
    disbld_buttons()
    compteur=0
   else:
    compteur+=1
    if compteur==160:
        egalité()
        rejouer()


def check_O(A,B,C) :
    global points2, compteur
    labelf=Label(window,text="Bot : "+str(points2),bg="black",fg="white")
    labels=font.Font(size=15)
    labelf['font']=labels
    f=font.Font(size=110)
    labelf.grid(row=0,column=3,pady=1,padx=1)
    if A["text"]+B["text"]+C["text"]=="OOO":
        A.config(bg="green")
        B.config(bg="green")
        C.config(bg="green")
        points2+=1
        messagebox.showinfo(title=None,message="Fin du jeu ! Tu as perdu ;)")
        disbld_buttons()
        compteur=0
    else:
        compteur+=1
        if compteur==160:
            egalité()
            rejouer()


## Création du bot

def auto1():
    bot(b2,b5,b8)
def auto2():
    bot(b1,b2,b3)
def auto3():
    bot(b4,b5,b6)
def auto4():
    bot(b7,b8,b9)
def auto5():
    bot(b1,b4,b7)
def auto6():
    bot(b2,b5,b8)
def auto7():
    bot(b3,b6,b9)
def auto8():
    bot(b1,b5,b9)
def auto9():
    bot(b3,b5,b7)

def bot(A,B,C):
    global pierre, stylo, souris, bureau, papier

    if B["text"]==" " and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        B["text"]="O"
        bureau=False
        pierre=False
    elif A["text"]==" " and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        A["text"]="O"
        stylo=False
    elif C["text"]==" " and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        C["text"]="O"
        souris=False

def autocontre():
    botcontre(b1,b2,b3)
    botcontre(b4,b5,b6)
    botcontre(b7,b8,b9)
    botcontre(b1,b4,b7)
    botcontre(b2,b5,b8)
    botcontre(b3,b6,b9)
    botcontre(b1,b5,b9)
    botcontre(b3,b5,b7)

def botcontre(A,B,C):
   global ciseaux
   if A["text"]+B["text"]+C["text"]=="XX " and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        C["text"]="O"
        ciseaux=False
   if A["text"]+B["text"]+C["text"]==" XX" and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        A["text"]="O"
        ciseaux=False
   if A["text"]+B["text"]+C["text"]=="X X" and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        B["text"]="O"
        ciseaux=False

def autowin():
    botwin(b1,b2,b3)
    botwin(b4,b5,b6)
    botwin(b7,b8,b9)
    botwin(b1,b4,b7)
    botwin(b2,b5,b8)
    botwin(b3,b6,b9)
    botwin(b1,b5,b9)
    botwin(b3,b5,b7)

def botwin(A,B,C):
    global papier,ciseaux
    if A["text"]+B["text"]+C["text"]=="OO " and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        C["text"]="O"
        papier=False
    if A["text"]+B["text"]+C["text"]==" OO" and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        A["text"] = "O"
        papier=False
    if A["text"]+B["text"]+C["text"]=="O O" and not clicked and pierre and stylo and souris and bureau and papier and ciseaux:
        B["text"]="O"
        papier=False

def clique(b):
    global clicked, pierre, stylo, souris, bureau, papier, ciseaux, compteur, stop
    if b["text"]==" " and clicked: ##b["text"] = récupèrer le texte du boutton et checker si == " "
        b["text"]="X"  ##nouveau text = "X"
        clicked=False
        gagne()
    if clicked==False and stop==False:
        autowin()
        autocontre()
        auto1()
        auto2()
        auto3()
        auto4()
        auto5()
        auto6()
        auto7()
        auto8()
        auto9()
        gagne()
        clicked=True
        pierre=True
        stylo=True
        souris=True
        bureau=True
        papier=True
        ciseaux=True
    elif clicked==False and stop==True:
        clicked=True
        stop=False
    else:
        messagebox.showerror("Morpion", "Cette case est déjà utilisée \nChoisis en une autre ...")


def egalité():
    global compteur
    compteur=0
    messagebox.showerror("egalité", "Tu ne gagneras jamais :)")
    disbld_buttons()
    rejouer()



def rejouer():

    global b1,b2,b3,b4,b5,b6,b7,b8,b9,compteur
    compteur=0
    b1=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b1))
    b2=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b2))
    b3=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b3))

    b4=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b4))
    b5=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b5))
    b6=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b6))

    b7=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b7))
    b8=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b8))
    b9=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b9))


    b1.grid(row=1,column=1,pady=0.2,padx=0.2)
    b2.grid(row=1,column=2,pady=0.2,padx=0.2)
    b3.grid(row=1,column=3,pady=0.2,padx=0.2)

    b4.grid(row=2,column=1,pady=0.2,padx=0.2)
    b5.grid(row=2,column=2,pady=0.2,padx=0.2)
    b6.grid(row=2,column=3,pady=0.2,padx=0.2)

    b7.grid(row=3,column=1,pady=0.2,padx=0.2)
    b8.grid(row=3,column=2,pady=0.2,padx=0.2)
    b9.grid(row=3,column=3,pady=0.2,padx=0.2)


    b1['font']=f
    b2['font']=f
    b3['font']=f
    b4['font']=f
    b5['font']=f
    b6['font']=f
    b7['font']=f
    b8['font']=f
    b9['font']=f


## Création des boutons pour rejouer et quitter


rejouer()
## Création des boutons

b1=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b1))   #clique(b1) pour envoyer les info du boutton b1 à la fonction clics()
b2=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b2))
b3=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b3))

b4=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b4))
b5=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b5))
b6=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b6))

b7=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b7))
b8=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b8))
b9=Button(window,text=" ",height=1,width=2,bg="slate gray",command=lambda : clique(b9))


## Création de la grille

b1.grid(row=1,column=1,pady=0.2,padx=0.2)
b2.grid(row=1,column=2,pady=0.2,padx=0.2)
b3.grid(row=1,column=3,pady=0.2,padx=0.2)

b4.grid(row=2,column=1,pady=0.2,padx=0.2)
b5.grid(row=2,column=2,pady=0.2,padx=0.2)
b6.grid(row=2,column=3,pady=0.2,padx=0.2)

b7.grid(row=3,column=1,pady=0.2,padx=0.2)
b8.grid(row=3,column=2,pady=0.2,padx=0.2)
b9.grid(row=3,column=3,pady=0.2,padx=0.2)


b1['font']=f
b2['font']=f
b3['font']=f
b4['font']=f
b5['font']=f
b6['font']=f
b7['font']=f
b8['font']=f
b9['font']=f


def exit():
    window.destroy()

quitter=Button(window,text="Quitter",height=2,width=6,bg="slate gray",command=exit)
replay=Button(window,text="Rejouer",height=2,width=6,bg="slate gray",command=rejouer)
replay.grid(pady=10,padx=5,column=1,row=5)
quitter.grid(pady=10,padx=5,column=3,row=5)
## Affichage du jeu

window.mainloop()





