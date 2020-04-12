# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:54:09 2020

@author: vetur
"""
import matplotlib.pyplot as plt
from random import randint
from tkinter import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk

def wow():
    print("in option")
    top=Toplevel()
    top.title("KBC")
    t=Text(top,height=20,width=30,bg='midnight blue',fg='snow',font=('Airal',12))
    t.pack()
    t.insert(END,"LOCK KIYA JAE?")
    tot=Button(top,text="HAAN JI",width=27,command=check,activeforeground='black',bg='light cyan',font=('Airal',12))
    tot.place(x=8,y=30)

def check():
    print("in check")
    global option
    global currentLevel #neeche wala hi explanantion
    global currentQuestion #this is saying that currentQuestion karke local variable nahi hai function ka, wo global wala use karna hai
    print("here")
    print("option",option)
    print("level",currentLevel)
    print(currentQuestion)
    print("Q mein",Questions[currentLevel][currentQuestion][0])
    if option == Questions[currentLevel][currentQuestion][0] and currentLevel <= 2:
        currentLevel+=1
        messageVar1["text"]="thass right bitchussss"
        if currentLevel > 2:
            messageVar1["text"]="you win"
            print("you win")   
            exit(0)
        questionsInLevel = Questions[currentLevel].keys()
        questionsInLevel = list(questionsInLevel)
        currentQuestionIndex = randint(0,len(questionsInLevel)-1)
        currentQuestion = questionsInLevel[currentQuestionIndex]
        print(currentQuestion)
        print(Questions[currentLevel][currentQuestion][1])
        print(Questions[currentLevel][currentQuestion][0])  
        messageVar1["text"]=currentQuestion
        butt1["text"] = Questions[currentLevel][currentQuestion][1][0]
        butt1.place(x=370,y=600)
        butt2["text"] = Questions[currentLevel][currentQuestion][1][1]
        butt2.place(x=760,y=600)
        butt3["text"] = Questions[currentLevel][currentQuestion][1][2]
        butt3.place(x=370,y=660)
        butt4["text"] = Questions[currentLevel][currentQuestion][1][3]
        butt4.place(x=760,y=660)

    else:
        messageVar1["text"]="game over"
        print("wrong answer")
        currentLevel = 100
    return


window = Tk()
window.title("OpenCV and Tkinter")
cv_img = cv2.cvtColor(cv2.imread("xoxo.jpg"), cv2.COLOR_BGR2RGB)
height, width, no_channels = cv_img.shape
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

Questions = {1:{"what is the indian currency?":[3,["dollars","yen","euro","rupee"]],
                "who is the host of KBC":[2,["SRK","salman","amitabh","amir"]]},
             2:{"where does sri live?":[0,["nerul","mulund","thane","airoli"]],
                "where does sanju live?":[1,["nerul","mulund","thane","airoli"]]}}
def option1():
    global option
    option = 0
    wow()
    return

def option2():
    global option
    option = 1
    wow()
    return
    
def option3():
    global option
    option = 2
    wow()
    return

def option4():
    global option
    option = 3
    wow()
    return

currentLevel = 1
questionsInLevel = Questions[currentLevel].keys()
questionsInLevel = list(questionsInLevel)
currentQuestionIndex = randint(0,len(questionsInLevel)-1)
currentQuestion = questionsInLevel[currentQuestionIndex]
print(currentQuestion)
print(Questions[currentLevel][currentQuestion][1])
print(Questions[currentLevel][currentQuestion][0])  
x = Questions[currentLevel][currentQuestion][0]
#_____________________

messageVar1=Message(window)
messageVar1["text"]=currentQuestion
messageVar1.config(bg='black',fg='white',font=('Airal',30),width=width)
messageVar1.place(x=470,y=505)

butt1=Button(window,command=option1,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
butt1["text"] = Questions[currentLevel][currentQuestion][1][0]
butt1.place(x=370,y=600)
butt2=Button(window,command=option2,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
butt2["text"] = Questions[currentLevel][currentQuestion][1][1]
butt2.place(x=760,y=600)
butt3=Button(window,command=option3,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
butt3["text"] = Questions[currentLevel][currentQuestion][1][2]
butt3.place(x=370,y=660)
butt4=Button(window,command=option4,activeforeground='white',activebackground='goldenrod1',bg='black',fg='white',font=('Airal',12))
butt4["text"] = Questions[currentLevel][currentQuestion][1][3]
butt4.place(x=760,y=660)
messageVar2=Message(window,text="₹5000")
messageVar2.config(bg='black',fg='white',font=('Airal',18),width=width)
messageVar2.place(x=640,y=30)
mainloop()

#jabhi bhi button dabate hai tabhi option wala functions apne aap call hota hai bina kisi loop ke, to jab bhi button click hoga,tabh edit kar diya screen to sort hp jaayega, wo hi kiya hai