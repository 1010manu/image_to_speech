import numpy as np
import sys
import cv2
import os
import pytesseract
from gtts import gTTS
from PIL import Image
import time
from playsound import playsound
from PIL import Image
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
cap = cv2.VideoCapture(0)
sample=0
error=0
print('Opening CAM')
time.sleep(2)
while(cap.isOpened()):
    ret, img = cap.read()
    if ret:
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',img)
        cv2.imwrite('frame.png',img)
        cv2.waitKey(1)
        sample=sample+1
        if (sample == 50):
            sample =0
            error=1
            print('Camera break')  
            cap.release()
    if error ==0:
        print('Camera is interrupted\nPlease execute the script again')
    if error ==1:
        print('image is caputured')
        im = Image.open("frame.png")
        text = pytesseract.image_to_string(im,lang = 'eng')
        lag = 'en'
        myobj = gTTS(text=text,lang=lag, slow =False)
        myobj.save("voice.mp3")
        playsound("voice.mp3")
        print(text)                  
cap.release()
cv2.destroyAllWindows()
