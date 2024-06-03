#! /usr/bin/env python3
import pyautogui
from screeninfo import get_monitors
import numpy as np
from PIL import Image
import pytesseract

def get_screen_position(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def give_info():
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.is_primary:
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

def find_word(image):
  text = pytesseract.image_to_string(image, config='--psm 6') 
  text = text.lower()
  if "follow" in text:
    boxes = pytesseract.bounding_boxes(image, raw=True)
    for box in boxes:
      x, y, w, h = box
      if "follow" in text[box[0]:box[1]]:
        return x, y, x+w, y+h  
  return None

def mouse_position():
  min_X, max_X, min_Y, max_Y = give_info()
  image = get_screen_position((min_X ,min_Y, max_X - min_X, max_Y - min_Y))
  bw_image = image.convert('L')
  image_np = np.array(bw_image)
  image = image_np.astype(np.uint8)
  
  follow_position = find_word(image)
  
  if follow_position:
    x, y, end_x, end_y = follow_position
    print(f"The word 'Follow' is found at position: ({x}, {y}) to ({end_x}, {end_y})")
  else:
    print("The word 'Follow' is not found in the screenshot.")

pytesseract.pytesseract.tesseract_cmd = r'path/to/tesseract.exe'  # Replace with your Tesseract path

mouse_position()