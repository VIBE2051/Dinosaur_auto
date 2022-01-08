import cv2
import time
import keyboard
from PIL import ImageGrab
import numpy as np

running = True

def quit():
    global running
    running = False
    print("Program Ended")
keyboard.add_hotkey('esc',quit)

def screenGrab(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    img = np.array(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    return img

while running:
    img = screenGrab(bbox=(360,85,575,210))
    
    
    cv2.imshow("Screen",img)
    cv2.waitKey(1)
    













