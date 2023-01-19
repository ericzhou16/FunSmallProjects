import time
import keyboard as kb
import cv2
import pyautogui as pag
import pytesseract as pt
from PIL import ImageEnhance
import numpy as np

pag.FAILSAFE = True
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('monkeytype\monkeytypeLogo.png')
test = pag.locateOnScreen('monkeytype\monkeytypeLogo.png')

while test == None:
    time.sleep(0.18)
    print('waiting')
    test = pag.locateOnScreen(img, grayscale=False)

print('done waiting')
textPic = pag.screenshot(region = (257, 434, 1404, 300))
enhancer = ImageEnhance.Brightness(textPic)
im_output = enhancer.enhance(1.5)

im_output.save(r'monkeytype\texttest.png')


toType = pt.image_to_string(im_output).replace('\n', ' ')

print("Going to type: " + toType)
# kb.write(toType)
