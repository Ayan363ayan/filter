import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk, Image

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2,columnspan=4)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 



#Slider window (slider controls stage position)
# sliderFrame = tk.Frame(window, width=600, height=100)
# sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

#Making the buttons
gb = tk.Button(window,width=10,height=2,text="Gushian Blur",command=lambda:gub()).grid(row=602,column=0)
canny = tk.Button(window,width=10,height=2,text="Canny",command=lambda:canny()).grid(row=602,column=1)
gray = tk.Button(window,width=10,height=2,text="Gray",command=lambda:gray()).grid(row=602,column=2)
blur = tk.Button(window,width=10,height=2,text="Blur",command=lambda:blur()).grid(row=602,column=3)

def gray():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, gray)
def gub():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image= cv2.GaussianBlur(frame,(7,7),cv2.BORDER_DEFAULT)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, gub)
def canny():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.Canny(frame,100,300)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, canny)
def blur():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.medianBlur(frame,15)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, blur)


# show_frame()  #Display 2
window.mainloop()  #Starts GUI
