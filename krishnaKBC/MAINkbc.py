# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:41:21 2020

@author: vetur
"""
import matplotlib.pyplot as plt
from random import randint
from tkinter import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk

#creating the window
root = Tk()
root.title("KBC")
myStr = StringVar()
#setting the background image
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

#deifining the questions

Questions = {1:{"what is the indian currency?":[3,["dollars","yen","euro","rupee"]],
                "who is the host of KBC":[2,["SRK","salman","amitabh","amir"]]},
             2:{"where does sri live?":[0,["nerul","mulund","thane","airoli"]],
                "where does sanju live?":[1,["nerul","mulund","thane","airoli"]]}}

def option1():
    check(0)
    return

def option2():
    check(1)
    return
    
def option3():
    check(2)
    return

def option4():
    check(3)
    return

def check(option):
    global currentLevel #neeche wala hi explanantion
    global currentQuestion #this is saying that currentQuestion karke local variable nahi hai function ka, wo global wala use karna hai
    print("here")
    print("option",option)
    print("level",currentLevel)
    print(currentQuestion)
    print("Q mein",Questions[currentLevel][currentQuestion][0])
    if option == Questions[currentLevel][currentQuestion][0] and currentLevel <= 2:
        currentLevel+=1
        myStr.set("thass right bitchussss")
        if currentLevel > 2:
            myStr.set("you win")
            print("you win")   
            exit(0)
        questionsInLevel = Questions[currentLevel].keys()
        questionsInLevel = list(questionsInLevel)
        currentQuestionIndex = randint(0,len(questionsInLevel)-1)
        currentQuestion = questionsInLevel[currentQuestionIndex]
        print(currentQuestion)
        print(Questions[currentLevel][currentQuestion][1])
        print(Questions[currentLevel][currentQuestion][0])  
        myStr.set(currentQuestion)
        butt1["text"] = Questions[currentLevel][currentQuestion][1][0]
        butt1.place(x=500,y=300)
        butt2["text"] = Questions[currentLevel][currentQuestion][1][1]
        butt2.place(x= 500,y = 320)
        butt3["text"] = Questions[currentLevel][currentQuestion][1][2]
        butt3.place(x=500,y=340)
        butt4["text"] = Questions[currentLevel][currentQuestion][1][3]
        butt4.place(x=500,y=360)

    else:
        myStr.set("game over")
        print("wrong answer")
        currentLevel = 100
    return
#_________________
myLabel = Label(root, textvariable=myStr)
myLabel.place(x=500,y=260)

butt1 = Button(root, command=option1)
butt1.place(x=500,y=300)

butt2 = Button(root, command=option2)
butt2.place(x= 500,y = 320)

butt3 = Button(root, command=option3)
butt3.place(x=500,y=340)

butt4 = Button(root, command=option4)
butt4.place(x=500,y=360)

currentLevel = 1
questionsInLevel = Questions[currentLevel].keys()
questionsInLevel = list(questionsInLevel)
currentQuestionIndex = randint(0,len(questionsInLevel)-1)
currentQuestion = questionsInLevel[currentQuestionIndex]
print(currentQuestion)
print(Questions[currentLevel][currentQuestion][1])
print(Questions[currentLevel][currentQuestion][0])  
x = Questions[currentLevel][currentQuestion][0]
myStr.set(currentQuestion)
butt1["text"] = Questions[currentLevel][currentQuestion][1][0]
butt1.place(x=500,y=300)
butt2["text"] = Questions[currentLevel][currentQuestion][1][1]
butt2.place(x= 500,y = 320)
butt3["text"] = Questions[currentLevel][currentQuestion][1][2]
butt3.place(x=500,y=340)
butt4["text"] = Questions[currentLevel][currentQuestion][1][3]
butt4.place(x=500,y=360)
root.mainloop()


#jabhi bhi button dabate hai tabhi option wala functions apne aap call hota hai bina kisi loop ke, to jab bhi button click hoga,tabh edit kar diya screen to sort hp jaayega, wo hi kiya hai