#! /usr/bin/env python3
import pyautogui
import time

# Liste pour stocker les positions de la souris
mouse_movements = []

# Durée pendant laquelle enregistrer les mouvements (en secondes)
duration = 60

# Intervalle de vérification (en secondes)
interval = 0.01

# Temps de fin
end_time = time.time() + duration


# Boucle pour vérifier la position de la souris à intervalles réguliers
while time.time() < end_time:
    # Obtenir la position actuelle de la souris
    x, y = pyautogui.position()
    # Ajouter la position à la liste
    mouse_movements.append((x, y))
    # Attendre un court instant avant de vérifier à nouveau
    time.sleep(interval)
# Afficher les mouvements enregistrés
for movement in mouse_movements:
    print(movement[0], movement[1])
