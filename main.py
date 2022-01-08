import cv2
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
    # Take a screenshot
    image = ImageGrab.grab(bbox=(712,300,1070,350))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Choose look ahead amount at random
    start_ahead = random.randint(792, 832)
    ahead = start_ahead
    
    # Setting zero and white we will flip when game colors invert
    zero = 0
    white = 255
    # Flips white to black and vice versa
    if image[144][376] == zero:
        ahead += 4
        temp = zero
        zero = white
        white = temp

    # Checks for 3 cactus small
    if image[320][ahead] == zero or image[320][ahead-1] == zero or image[320][ahead-2] == zero:
        keyboard.release("down")
        keyboard.press("space")
        time.sleep(0.01)
        keyboard.release("space")
    

    # Get the colour of the pixel a x, y
    color = image.getpixel((x, y))
    mean_color = (color[0] + color[1] + color[2])/3
    print(color)
    print(mean_color)

    # Look ahead code
    look_ahead = random.randint()

    if mean_color < 240:
      keyboard.send('space')
    
