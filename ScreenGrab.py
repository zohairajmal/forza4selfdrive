import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img


last_time = time.time()
while True:
    PressKey(W)
    # Remove title navbar, 800 x 640 resolution of screen
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    # print('Frame took {} seconds'.format(time.time()-last_time)) #Checking the time to see if the method is efficient enough or not
    last_time = time.time()
    new_screen = process_img(screen)
    cv2.imshow('window', new_screen)
    # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)) # converting to rgb because for some reason it was in bluie greedn red, weird.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
