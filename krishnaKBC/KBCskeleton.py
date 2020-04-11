# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:03:59 2020

@author: vetur
"""
from tkinter import *
root = Tk()

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
myLabel.pack()

butt1 = Button(root, text="qt", command=option1)
butt1.pack()

butt2 = Button(root, text="fatso", command=option2)
butt2.pack()

butt3 = Button(root, text="bitch", command=option3)
butt3.pack()

butt4 = Button(root, text="dumbudi", command=option4)
butt4.pack()

root.mainloop()