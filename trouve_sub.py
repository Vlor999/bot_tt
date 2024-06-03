#!/usr/bin/env python3
import pyautogui
from screeninfo import get_monitors
import numpy as np
from PIL import Image
import cv2
from random import random, uniform
import time

def get_screen_position(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def give_info():
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.is_primary:
            max_X = monitor.height
            max_Y = monitor.width
    min_X = 3 * max_X // 4
    min_Y = max_Y // 4
    return min_X, max_X, 3 * min_Y // 2, 11 * max_Y // 20

def find_image(template_path, screenshot):
    template = cv2.imread(template_path, 0)
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0 and len(loc[1]) > 0:
        pt = (loc[1][0], loc[0][0])
        w, h = template.shape[::-1]
        return pt[0], pt[1], pt[0] + w, pt[1] + h
    else:
        return None

def mouse_position():
    template_path = 'im.png'
    min_X, max_X, min_Y, max_Y = give_info()
    image = get_screen_position((min_X, min_Y, max_X - min_X, max_Y - min_Y))
    
    match_position = find_image(template_path, image)
    
    if match_position:
        x, y, end_x, end_y = match_position
        pyautogui.moveTo(x + min_X, y + min_Y, duration=random() + 0.5)
        return 1
    else:
        return 0

def bezier_curve(t, p0, p1, p2, p3):

    return ( 
        (1-t)**3 * p0[0] + 3 * (1-t)**2 * t * p1[0] + 3 * (1-t) * t**2 * p2[0] + t**3 * p3[0],
        (1-t)**3 * p0[1] + 3 * (1-t)**2 * t * p1[1] + 3 * (1-t) * t**2 * p2[1] + t**3 * p3[1]
    )

def realistic_move(x, y, duration=1.0):
    start_x, start_y = pyautogui.position()
    control_x1 = start_x + (x - start_x) * uniform(0.25, 0.75)
    control_y1 = start_y + (y - start_y) * uniform(0.25, 0.75)
    control_x2 = start_x + (x - start_x) * uniform(0.25, 0.75)
    control_y2 = start_y + (y - start_y) * uniform(0.25, 0.75)
    
    steps = duration * 50  # More steps for smoother movement
    if steps == 0:
        steps = 50
    i = 0
    while i < steps + 1:
        t = i / steps
        new_x, new_y = bezier_curve(t, (start_x, start_y), (control_x1, control_y1), (control_x2, control_y2), (x, y))
        pyautogui.moveTo(new_x, new_y, duration=0.001)
        time.sleep(0.001)
        i += 1

def sub():
    destination_x = 1250 + uniform(-5, 5)
    destination_y = 175 + uniform(-5, 5)
    realistic_move(destination_x, destination_y, duration=1)
    return 1
