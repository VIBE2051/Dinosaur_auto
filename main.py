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

# Jump loc calibration
print("Calibrating")
while running:
    # If space is pressed
    if (keyboard.is_pressed('space')):
        # Store the location of the cursor
        (x, y) = pyautogui.position()
        break


# Main Loop
while running:
    a,b = 40,29
    box = (x,y,x+a,y+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = np.array(gray.getcolors())
    value = a.sum()
    print(value)
    if value != 1415:
        keyboard.press("space")
        time.sleep(0.0001)
        keyboard.release("space")

