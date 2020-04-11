from tkinter import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk

root = Tk()

cv_img = cv2.cvtColor(cv2.imread("KBC2.png"), cv2.COLOR_BGR2RGB)

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(root, width = width, height = height)
canvas.pack()

# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW) 

myStr = StringVar()
myStr.set("sri is a?")

def option1():
    check(0)

def option2():
    check(1)
    butt2["text"] = "wrong"

def option3():
    check(2)
    butt3["text"] = "wrong"

def option4():
    check(3)
    butt4["text"] = "wrong"

def check(option):
    if option == 0:
        myStr.set("thass right bitchussss")
    else:
        myStr.set("nope,wrong")        

myLabel = Label(root, textvariable=myStr)
myLabel.place(x=500,y=260)

butt1 = Button(root, text="qt", command=option1)
butt1.place(x=500,y=300)

butt2 = Button(root, text="fatso", command=option2)
butt2.place(x= 500,y = 320)

butt3 = Button(root, text="bitch", command=option3)
butt3.place(x=500,y=340)

butt4 = Button(root, text="dumbudi", command=option4)
butt4.place(x=500,y=360)

root.mainloop()