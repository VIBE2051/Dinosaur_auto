import pyautogui
import random
import time
import keyboard
from PIL import ImageGrab, ImageOps
import numpy as np


running = True


# Define hotkey to quit program [esc]
def quit():
    global running
    running = False
    print("Program Ended")
keyboard.add_hotkey('esc',quit)

time.sleep(5)
# Main Loop
while running:
    x1,y1,a,b = 288,316,40,29
    box = (x1,y1,x1+a,y1+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = np.array(gray.getcolors())
    value = a.sum()
    print(value)
    if value != 1407:
        pyautogui.press("space")


    
