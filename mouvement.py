#! /usr/bin/env python3
from pyautogui import press, moveTo, click, sleep
from time import time, sleep
from random import randint, random
from sys import argv
from screeninfo import get_monitors
from trouve_sub import mouse_position, sub, realistic_move
import bezier

monitors = get_monitors()
min_x = 0
min_Y = 0
for monitor in monitors:
    if monitor.is_primary :
        max_X = monitor.height
        max_Y = monitor.width

goal_x = 1.3 * max_X // 4
goal_y = max_Y // 2

def display_status(nb, minute, tic, abo):
    progress = round((time() - tic) / (minute * 60) * 100, 2)
    print(f"\rLike : {nb} | Progression : {progress} % | abo : {abo}", end="")

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
    moveTo(x_use[0], y_use[0], duration=random())
    for j in range(len(x_use)):
        x = x_use[j] // 2
        y = y_use[j]
        moveTo(x, y, duration=random()/10)

def follow():
    val = mouse_position()
    sleep(0.2)
    click()
    sleep(random() + 1)
    return val

def mouvement(l1, l2, minute):
    sleep(1)
    moveTo(goal_x, goal_y, duration = 1)
    click()
    tic = time()
    nb = 0
    abo = 0
    while time() - tic < minute * 60: 
        x = randint(min_x, max_X)
        y = randint(min_Y, max_Y)
        realistic_move(x, y, duration=0.5)
        display_status(nb, minute, tic, abo)
        if randint(1, 14) > 2:
            press('down')
            if randint(1, 6) > 3:
                nb += 1
                press('L')
                sleep(random() + 1)
        else:
            press('up')
            if randint(1, 6) > 2:
                sleep(random() + 0.2)
                press('L')
            sleep(random() + 0.2)
            press('down')

        display_status(nb, minute, tic, abo)

        if randint(1, 12) == 1:
            realistic_move(max_X // 2, max_Y // 2, duration = random() / 2)
            abo += sub()

        if randint(1, 2) == 1:
            deplacement_alea(l1, l2)

        display_status(nb, minute, tic, abo)

        sleep(randint(5, 15) / 3)

def main():
    liste_x, liste_y = mouvemnt_alea()
    if (len(argv) > 1):
        minute = float(argv[1])
    else:
        minute = 10
    mouvement(liste_x, liste_y, minute)
    print()

if __name__ == "__main__":
    main()