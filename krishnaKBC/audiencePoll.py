# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:19:08 2020

@author: vetur

from random import randint
"""

import matplotlib.pyplot as plt
from tkinter import *
from random import randint

root=Tk()
root.title("KBC")
label=Label(root,text="Lifelines").place(x=0,y=0)

def poll():

    ops=['A','B','C','D']
    perc=[20,0,0,0]
    for i in range(80):
        perc[randint(0,3)] += 1
    plt.bar(ops,perc,color='g')
    plt.legend()
    plt.xlabel("Options")
    plt.ylabel("Percentage")
    plt.title("Audience Poll")
    plt.show()

bt1=Button(root,text="Audience poll",command=poll)
bt1.pack()
bt1.place(x=0,y=25)

root.mainloop()