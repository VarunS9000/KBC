#button
import tkinter as tk
m=tk.Tk()
m.title("Manju is going to die a ")
w=tk.Button(m,text="VIRGIN",width=69,command=m.destroy,activeforeground='red')
w.pack()
m.mainloop()

#pop-up
from tkinter import *
master= Tk()
w = Canvas(master,width=500,height=600,bg='dark blue')
w.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
a=int(input("Enter a number"))
if(a==5):
    top=Toplevel()
    top.title("KBC")
    t=Text(top,height=25,width=30,bg='light grey')
    t.pack()
    t.insert(END,"LOCK KIYA JAE?")
    t=tkinter.Button(top,text="HAAN JI",width=69,command=top.destroy,activeforeground='red')
mainloop()

#image
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
window = tkinter.Tk()
window.title("OpenCV and Tkinter")
cv_img = cv2.cvtColor(cv2.imread("unnamed.jpg"), cv2.COLOR_BGR2RGB)
height, width, no_channels = cv_img.shape
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
window.mainloop()


#image + background
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
def wow():
    top=Toplevel()
    top.title("KBC")
    t=Text(top,height=25,width=30,bg='light grey')
    t.pack()
    t.insert(END,"LOCK KIYA JAE?")
    
window = tkinter.Tk()
window.title("OpenCV and Tkinter")
cv_img = cv2.cvtColor(cv2.imread("xoxo.jpg"), cv2.COLOR_BGR2RGB)
height, width, no_channels = cv_img.shape
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
ourMessage = "IS DADDY THE BEST"
messageVar=tkinter.Message(window,text= ourMessage)
messageVar.config(bg='black',fg='white',font=('Airal',30),width=width)
messageVar.place(x=470,y=505)
w=tkinter.Button(window,text="YES",command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
w.place(x=370,y=600)
w=tkinter.Button(window,text="OFCOURSE",command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
w.place(x=760,y=600)
w=tkinter.Button(window,text="NO DOUBT BRO",command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
w.place(x=370,y=660)
w=tkinter.Button(window,text="ILL BE A FOOL TO SAY NO",command=wow,activeforeground='white',activebackground='goldenrod1',bg='black',fg='white',font=('Airal',12))
w.place(x=760,y=660)
messageVar=tkinter.Message(window,text="₹5000")
messageVar.config(bg='black',fg='white',font=('Airal',18),width=width)
messageVar.place(x=640,y=30)
mainloop()


