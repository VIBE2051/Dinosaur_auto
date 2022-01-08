import cv2
import time
import keyboard
from PIL import ImageGrab
import numpy as np

running = True
x = 100
y = 100

# Define hotkey to quit program [esc]
def quit():
    global running
    running = False
    print("Program Ended")
keyboard.add_hotkey('esc',quit)

# Main Loop
while running:
    # Take a screenshot
    image = ImageGrab.grab()

    # Get the colour of the pixel a x, y
    color = image.getpixel((x, y))
    













