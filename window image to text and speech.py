import tkinter as tk
window = tk.Tk()
window.title("window")
window.geometry("500x500")
window.configure(background="Red")
lbl=tk.Label(window,text="Image to text",width=20,height=3,bg="Purple",fg="White",font=("times",15,"bold"))
lbl.place(x=50,y=50)
def new():
    #!/usr/bin/env python
    import numpy as np
    import sys
    import cv2
    import os
    from gtts import gTTS
    import pytesseract
    from PIL import Image
    import time
    from playsound import playsound
    
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    cap = cv2.VideoCapture(0)
    sample=0;
    error=0
    print('Opening CAM')
    time.sleep(2)
    while(cap.isOpened()):
        #while(True):
        ret, img = cap.read()
        #print(ret)
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
    ##                cv2.destroyAllWindows()
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
button=tk.Button(window,text="ENTER",command=new,width=7,height=2,bg="Green",fg="Black",activebackground="Pink",font=("times",15,"bold"))
button.place(x=50,y=250)
window.mainloop()
#cv2.destroyAllWindows()


