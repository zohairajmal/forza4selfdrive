import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    last_time = time.time()
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640))) #Remove title navbar, 800 x 640 resolution of screen 
        print('loop took {} seconds'.format(time.time()-last_time)) #Checking the time to see if the method is efficient enough or not 
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))# converting to rgb because for some reason it was in bluie greedn red, weird.
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()