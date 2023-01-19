import time
import keyboard as kb
import cv2
import pyautogui as pag
import pytesseract as pt
from PIL import Image, ImageEnhance
import numpy as np

color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}

img = cv2.imread('textwithyellow.png')

grayscaleImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r'monkeytype\test.png', np.asarray(img))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lower = np.array([226, 183, 20])  #-- Lower range --
upper = np.array([226, 183, 20])  #-- Upper range --
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(hsv, hsv, mask=mask)
res = Image.fromarray(res)
res.save('edited.png')

