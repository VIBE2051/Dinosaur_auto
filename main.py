import pyautogui
import random
import time
import keyboard
from PIL import ImageGrab
import numpy as np


running = True
x = 792
y = 330

# Define hotkey to quit program [esc]
def quit():
    global running
    running = False
    print("Program Ended")
keyboard.add_hotkey('esc',quit)

time.sleep(5)
# Main Loop
while running:
    im = pyautogui.screenshot()
    screen = im.getpixel((722,250))

    x1 = im.getpixel((760,327))
    x2 = im.getpixel((780,327))
    x3 = im.getpixel((800,327))
    x4 = im.getpixel((820,327))
    
    y1 = im.getpixel((760,301))
    y2 = im.getpixel((770,300))
    y3 = im.getpixel((780,308))
    y4 = im.getpixel((790,300))


    # Checks if it is day or night time
    
    if screen[0] == 247:
        if x1 != 247 or x2 != 247 or x3 != 247 or x4 != 247 or y1 != 247 or y2 != 247 or y3 != 247 or y4 != 247:
            keyboard.send('space')
            time.sleep(0.0001)

        else:
            if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
                keyboard.send('space')
                time.sleep(0.0001)
