#! /usr/bin/env python3
import pyautogui
from screeninfo import get_monitors
import numpy as np
from PIL import Image

def get_screen_position(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def give_info():
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.is_primary :
            max_X = monitor.height
            max_Y = monitor.width
    min_X = 3 * max_X //4
    min_Y = max_Y // 2
    return min_X, max_X, min_Y,  max_Y

def transfo_nb(image):
    nb_l, nb_c = image.size
    for i in range(nb_l):
        for j in range(nb_c):
            if image.getpixel((i, j)) < 128:
                image[i, j] = 0
            else:
                image[i, j] = 255
    return image

def mouse_position():
    min_X, max_X, min_Y, max_Y = give_info()
    image = get_screen_position((min_X ,min_Y, max_X - min_X, max_Y - min_Y))
    bw_image = image.convert('L')
    image_np = np.array(bw_image)
    image = image_np.astype(np.uint8)
    pil_image = Image.fromarray(image)
    pil_image.show()
mouse_position()