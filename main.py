import cv2
import time
import keyboard
from PIL import ImageGrab
import numpy as np

running = True
x = 712
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
    # Take a screenshot
    image = ImageGrab.grab(bbox=(712,300,1070,350))

    

    # Get the colour of the pixel a x, y
    color = image.getpixel((x, y))
    mean_color = (color[0] + color[1] + color[2])/3
    print(color)
    print(mean_color)

    # Look ahead 


    if mean_color < 240:
      keyboard.send('space')
    
