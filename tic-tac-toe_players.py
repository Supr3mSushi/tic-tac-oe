import random
import time
import os
from tkinter import W

###Lire les lignes -> compter le nombre de 0 ou X
###Relire les lignes -> insérer le 0 ou X. 

def init():
    tab = [' '] * 9
    liste = [0,1,2,3,4,5,6,7,8]
    coins = [0,2,6,8]
    print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
    return tab,liste,coins

def player1(tab,liste,coins):
    a = (int(input("Choisissez la case entre 1 et 9\n")))
    if tab[a-1] == ' ':
        tab[a-1] = '0'
        liste.remove(a-1)
        if (a-1) == 0 or (a-1) == 2 or (a-1) == 6 or (a-1) == 8:
            coins.remove(a-1)
    else:
        print('Cette case est déjà utilisée, veuillez recommencer')
        return player1(tab,liste,coins)

    print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
    return tab,liste,coins


def player2(tab,liste,coins):
    b = (int(input("Choisissez la case entre 1 et 9\n")))
    if tab[b-1] == ' ':
        tab[b-1] = '0'
        liste.remove(b-1)
        if (b-1) == 0 or (b-1) == 2 or (b-1) == 6 or (b-1) == 8:
            coins.remove(b-1)
    else:
        print('Cette case est déjà utilisée, veuillez recommencer')
        return player2(tab,liste,coins)

    print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
    return tab,liste,coins


def botquicommencepas(tab,coups,liste,coins):
    print("\nAu tour de l'ordinateur \n")

    if coups == 1:
        if tab[4] == ' ': 
            tab[4] = 'X'
            liste.remove(4)
        else:
            ici = random.choice(liste)
            tab[ici] = 'X'
            liste.remove(ici)
            if (ici) == 0 or (ici) == 2 or (ici) == 6 or (ici) == 8:
                coins.remove(ici)

    
    if coups > 2:
        ici = random.choice(liste)
        tab[ici] = 'X'
        liste.remove(ici)
        if (ici) == 0 or (ici) == 2 or (ici) == 6 or (ici) == 8:
            coins.remove(ici)

    print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
    return tab,liste,coins



def botquicommence(tab,coups,liste,coins):
    print("\nAu tour de l'ordinateur \n")
    cpt0 = 0
    cptX = 0
    if coups == 0:
        ici = random.choice(coins)
        tab[ici] = '0'
        liste.remove(ici)
        coins.remove(ici)

    if coups == 2:
        ici = random.choice(coins)
        tab[ici] = '0'
        liste.remove(ici)
        coins.remove(ici)

    if coups > 2:
            for i in range(3):
                if tab[i] == '0':
                    cpt0 = cpt0 + 1
                if tab[i] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for j in range(3):
                    if tab[j] == ' ':
                        tab[j] = '0'
                        liste.remove(j)
                        if (j) == 0 or (j) == 2 or (j) == 6 or (j) == 8:
                            coins.remove(j)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins

            cpt0 = 0
            cptX = 0
            for i in range(3,6):
                if tab[i] == '0':
                    cpt0 = cpt0 + 1
                if tab[i] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for x in range(3,6):
                    if tab[x] == ' ':
                        tab[x] = '0'
                        liste.remove(x)
                        if (x) == 0 or (x) == 2 or (x) == 6 or (x) == 8:
                            coins.remove(x)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins

            cpt0 = 0
            cptX = 0
            for i in range(6,9):
                if tab[i] == '0':
                    cpt0 = cpt0 + 1
                if tab[i] == 'X':
                    cptX = cptX + 1

            if cpt0 > 1 or cptX > 1:
                for k in range(6,9):
                    if tab[k] == ' ':
                        tab[k] = '0'
                        liste.remove(k)
                        if (k) == 0 or (k) == 2 or (k) == 6 or (k) == 8:
                            coins.remove(k)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins
                        
            cpt0 = 0
            cptX = 0 
            for n in range(0,7,3):
                if tab[n] == '0':
                    cpt0 = cpt0 + 1
                if tab[n] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for m in range(0,7,3):
                    if tab[m] == ' ':
                        tab[m] = '0'
                        liste.remove(m)
                        if (m) == 0 or (m) == 2 or (m) == 6 or (m) == 8:
                            coins.remove(m)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins
            
            cpt0 = 0
            cptX = 0 
            for p in range(1,8,3):
                if tab[p] == '0':
                    cpt0 = cpt0 + 1
                if tab[p] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for q in range(1,8,3):
                    if tab[q] == ' ':
                        tab[q] = '0'
                        liste.remove(q)
                        if (q) == 0 or (q) == 2 or (q) == 6 or (q) == 8:
                            coins.remove(q)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins
            
            cpt0 = 0
            cptX = 0
            for c in range(2,9,3):
                if tab[c] == '0':
                    cpt0 = cpt0 + 1
                if tab[c] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for d in range(2,9,3):
                    if tab[d] == ' ':
                        tab[d] = '0'
                        liste.remove(d)
                        if (d) == 0 or (d) == 2 or (d) == 6 or (d) == 8:
                            coins.remove(d)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins

            cpt0 = 0
            cptX = 0
            for f in range(0,9,4):
                if tab[f] == '0':
                    cpt0 = cpt0 + 1
                if tab[f] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for g in range(2,9,3):
                    if tab[g] == ' ':
                        tab[g] = '0'
                        liste.remove(g)
                        if (g) == 0 or (g) == 2 or (g) == 6 or (g) == 8:
                            coins.remove(g)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins
            
            cpt0 = 0
            cptX = 0
            for v in range(6,1,-2):
                if tab[v] == '0':
                    cpt0 = cpt0 + 1
                if tab[v] == 'X':
                    cptX = cptX + 1
            if cpt0 > 1 or cptX > 1:
                for w in range(2,9,3):
                    if tab[w] == ' ':
                        tab[w] = '0'
                        liste.remove(w)
                        if (w) == 0 or (w) == 2 or (w) == 6 or (w) == 8:
                            coins.remove(w)
                        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
                        return tab,liste,coins
            

            else:
                ici = random.choice(liste)
                tab[ici] = '0'
                liste.remove(ici)
                if (ici) == 0 or (ici) == 2 or (ici) == 6 or (ici) == 8:
                    coins.remove(ici)
    
    print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
    return tab,liste,coins


def morpion():
    os.system('cls')
    print("\nNouvelle partie !\n")
    tab,liste,coins = init()
    coups = 0
    win1 = False
    win2 = False
    while win1 == False and win2 == False and coups < 9:
        #player1(tab,liste,coins)
        time.sleep(1)
        botquicommence(tab,coups,liste,coins)
        os.system('cls')
        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
        coups = coups + 1
        win1 = gagnant1(tab)
        if win1 == True:
            print('\nLe joueur 1 a gagné !\n')
            break
        if coups == 9:
            print('\nEgalité')
            break

        #player2(tab,liste,coins)
        time.sleep(1)
        botquicommencepas(tab,coups,liste,coins)
        os.system('cls')
        print('[',tab[0],'|',tab[1],'|',tab[2],']\n[',tab[3],'|',tab[4],'|',tab[5],']\n[',tab[6],'|',tab[7],'|',tab[8],']\n')
        coups = coups + 1
        win2 = gagnant2(tab)
        if win2 == True:
            print('\nLe joueur 2 a gagné !\n')
            break
            
    replay = int(input('Voulez-vous rejouer ? \n1:Oui \n2:Non\n\n'))
    if replay == 1:
        morpion()
    else:
        return

def gagnant1(tab):
    win = False
    if (tab[0] == tab[1] == tab[2] == '0') or (tab[3] == tab[4] == tab[5] == '0') or (tab[6] == tab[7] == tab[8] == '0') or (tab[0] == tab[3] == tab[6] == '0') or (tab[1] == tab[4] == tab[7] == '0') or (tab[2] == tab[5] == tab[8] == '0') or (tab[0] == tab[4] == tab[8] == '0') or (tab[2] == tab[4] == tab[6] == '0'):
        win = True
    return win

def gagnant2(tab):
    win = False
    if (tab[0] == tab[1] == tab[2] == 'X') or (tab[3] == tab[4] == tab[5] == 'X') or (tab[6] == tab[7] == tab[8] == 'X') or (tab[0] == tab[3] == tab[6] == 'X') or (tab[1] == tab[4] == tab[7] == 'X') or (tab[2] == tab[5] == tab[8] == 'X') or (tab[0] == tab[4] == tab[8] == 'X') or (tab[2] == tab[4] == tab[6] == 'X'):
        win = True
    return win


morpion()