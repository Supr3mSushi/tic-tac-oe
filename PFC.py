import random
j= str(input("Pierre, feuille ou ciseau ? : "))

choix=["pierre", "feuille","ciseau"]
bot=random.choice(choix)
print("choix du bot : ",bot)

if j=="pierre" and bot == "pierre":
    print("égalité")
if j=="pierre" and bot == "feuille":
    print("L'IA 2 à gagné")
if j=="pierre" and bot == "ciseau":
    print("Joeur à gagné")
if j=="feuille" and bot == "pierre":
    print("Joueur à gagné")
if j=="feuille" and bot == "feuille":
    print("égalité")
if j=="feuille" and bot == "ciseau":
    print("L'IA à gagné")
if j=="ciseau" and bot == "pierre":
    print("L'IA à gagné")
if j=="ciseau" and bot == "feuille":
    print("Joueur à gagné")
if j=="ciseau" and bot == "ciseau":
    print("égalité")
