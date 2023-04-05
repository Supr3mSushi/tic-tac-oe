## Projet 3 Morpion (Player 1 vs Player 2)

from tkinter import * 
from tkinter import messagebox
import tkinter.font as font

window=Tk()
window.configure(bg="black")
window.resizable(height = False, width = False)

window.title("Morpion")
labelf=Label(window, text="Morpion by Ekip", bg="black",fg="orange",)
labels=font.Font(size=19)
labelf['font'] = labels
f=font.Font(size=110)
labelf.grid(row=0, column=2, pady=1, padx=1)
clicked=True
count=0 

## Désactiver tout les bouttons  

def disbld_buttons() : 
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

def gagne() :
    global winner
    winner = False
    check(b1,b2,b3)
    check(b4,b5,b6)
    check(b7,b8,b9)
    check(b1,b4,b7)
    check(b2,b5,b8)
    check(b3,b6,b9)
    check(b1,b5,b9)
    check(b3,b5,b7)

def check(A,B,C) :
    global joueur, winner
    if clicked == False:
        joueur = "O"
    else :
        joueur = "X"
    if A["text"] + B["text"] + C["text"] == "XXX" or A["text"] + B["text"] + C["text"] == "OOO" :
        A.config(bg="green")
        B.config(bg="green")
        C.config(bg="green")
        winner = True   
        messagebox.showinfo(title=None, message="Fin du jeu ! Bravo, tu as gagné la partie !")
        disbld_buttons()

## Clicks 

def click(b) : 
    global clicked, count
    if b["text"] == " " and clicked == True : 
        b["text"] = "X"
        clicked=False
        count+=1 
        gagne()
    elif b["text"] == " " and clicked == False : 
        b["text"] = "O" 
        clicked = True 
        count+=1 
        gagne()
    else : 
        messagebox.showerror("Morpion", "Cette case est déjà utilisée \nChoisis en une autre ...")

## Création des boutons 

b1=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b1))
b2=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b2))
b3=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b3))

b4=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b4))
b5=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b5))
b6=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b6))

b7=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b7))
b8=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b8))
b9=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b9))


##Création de la grille 

b1.grid(row=1, column=1, pady=0.2, padx=0.2)
b2.grid(row=1, column=2, pady=0.2, padx=0.2)
b3.grid(row=1, column=3, pady=0.2, padx=0.2)

b4.grid(row=2, column=1, pady=0.2, padx=0.2)
b5.grid(row=2, column=2, pady=0.2, padx=0.2)
b6.grid(row=2, column=3, pady=0.2, padx=0.2)

b7.grid(row=3, column=1, pady=0.2, padx=0.2)
b8.grid(row=3, column=2, pady=0.2, padx=0.2)
b9.grid(row=3, column=3, pady=0.2, padx=0.2)



b1['font'] = f
b2['font'] = f
b3['font'] = f
b4['font'] = f
b5['font'] = f
b6['font'] = f
b7['font'] = f
b8['font'] = f
b9['font'] = f

## Affichage du jeu 

window.mainloop()
