# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:42:44 2020

@author: vetur
"""

from tkinter import *
root = Tk()

myStr = StringVar()
myStr.set("welcome")

def left():
    myStr.set("left")
    
def right():
    myStr.set("right")

myLabel = Label(root, textvariable=myStr)
myLabel.pack()

lbutt = Button(root, text="left", command=left)
lbutt.pack()

rbutt = Button(root, text="right", command=right)
rbutt.pack()

root.mainloop()