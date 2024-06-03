#! /usr/bin/env python3
import pyautogui
from time import time, sleep
from random import randint
from sys import argv
from screeninfo import get_monitors

monitors = get_monitors()
min_x = 0
min_Y = 0
for monitor in monitors:
    if monitor.is_primary :
        max_X = monitor.height
        max_Y = monitor.width

goal_x = 1.3 * max_X // 4
goal_y = max_Y // 2

def display_status(nb, minute, tic):
    progress = round((time() - tic) / (minute * 60) * 100, 2)
    print(f"\rLike : {nb} | Progression : {progress} %", end="")

def mouvemnt_alea():
    fichier = open("position_alea.txt", 'r')
    liste_x = []
    liste_y = []
    for lignes in fichier:
        l = lignes.strip()
        l = l.split(" ")
        x = int(l[0])
        y = int(l[1])
        liste_x.append(x)
        liste_y.append(y)
    return liste_x, liste_y


def deplacement_alea(l1, l2):
    i = randint(100, 6400)
    taille = randint(30, 50)
    x_use = l1[i - taille // 2: i + taille//2 + 1]
    y_use = l2[i - taille // 2: i + taille//2 + 1]
    if (len(x_use) == 0):
        return
    pyautogui.moveTo(x_use[0], y_use[0], duration=0.5)
    for j in range(len(x_use)):
        x = x_use[j] // 2
        y = y_use[j]
        pyautogui.moveTo(x, y, duration=0.01)

def mouvement(l1, l2, minute):
    sleep(1)
    pyautogui.moveTo(goal_x, goal_y, duration = 1)
    pyautogui.click()
    global tic, nb
    tic = time()
    nb = 0
    while time() - tic < minute * 60: 
        x = randint(min_x, max_X)
        y = randint(min_Y, max_Y)
        pyautogui.moveTo(x, y, duration=0.5)
        display_status(nb, minute, tic)
        if randint(1, 14) > 2:
            pyautogui.moveTo(goal_x + randint(0, 9), goal_y + randint(0, 5), duration = 0.5)
            pyautogui.press('down')
            display_status(nb, minute, tic)
            if randint(1, 6) > 3:
                nb += 1
                pyautogui.press('L')
                pyautogui.sleep(2)
        else:
            pyautogui.press('up')
            if randint(1, 6) > 2:
                pyautogui.press('L')
            pyautogui.sleep(1)
            pyautogui.press('down')
            display_status(nb, minute, tic)

        if randint(1, 2) == 1:
            deplacement_alea(l1, l2)
        display_status(nb, minute, tic)
        sleep(randint(5, 15)/3)

liste_x, liste_y = mouvemnt_alea()
if (len(argv) > 1):
    minute = float(argv[1])
else:
    minute = 10
mouvement(liste_x, liste_y, minute)