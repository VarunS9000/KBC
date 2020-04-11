
mport matplotlib.pyplot as plt
from tkinter import *

root=Tk()
root.title("KBC")
label=Label(root,text="Lifelines").place(x=0,y=0)

def poll():

    ops=['A','B','C','D']
    perc=[35,25,25,15]
    plt.bar(ops,perc,color='g')
    plt.legend()
    plt.xlabel("Options")
    plt.ylabel("Percentage")
    plt.title("Audience Poll")
    plt.show()

bt1=Button(root,text="Audience poll",command=poll)
bt1.pack()
bt1.place(x=0,y=25)
           
