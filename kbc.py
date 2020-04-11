
from tkinter import *
import tkinter
import random
import cv2
import PIL.Image, PIL.ImageTk
y=[]
kcount=0
count=0
while(kcount!=4):

    root=Tk()
    root.title("KBC")
    cv_img = cv2.cvtColor(cv2.imread("xoxo.jpg"), cv2.COLOR_BGR2RGB)
    height, width, no_channels = cv_img.shape
    canvas = Canvas(root, width = width, height = height)
    canvas.pack()
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    top=Toplevel()
    
    Q1=["Which Fermion has no anti particle", "Which party did Hitler belong to"," What title was given to Aurangazeb","When was the battle of Plassey fought"]
    op11=["electron","proton","neutrino","pi meson"]
    op12=["Congress","BJP","Shiv sena","Nazi Germany"]
    op13=["alamgir","akbar","alampanah","shehensha"]
    op14=["1793","1765","1757","1803"]

    x=StringVar()

    def wow():
        top=Toplevel()
        top.title("KBC")
        t=Text(top,height=20,width=30,bg='midnight blue',fg='snow',font=('Airal',12))
        t.pack()
        t.insert(END,"LOCK KIYA JAE?")
        tot=tkinter.Button(top,text="HAAN JI",width=27,command=result,activeforeground='black',bg='light cyan',font=('Airal',12))
        tot.place(x=8,y=30)


   
    def verify(x,y):
        
        while(True):
            if(x in y):
                x=Q1[random.randrange(4)]
                
                

            elif(x not in y):
                
                
                break
                
    def check(x,Q1,top):
     top.destroy()
     
     if(x==Q1[0]):
    
    
         bt1["text"]="wrong"
         bt2["text"]="wrong"
         bt3["text"]="correct"
         bt4["text"]="wrong"

     elif(x==Q1[1]):
        bt1["text"]="wrong"
        bt2["text"]="wrong"
        bt3["text"]="wrong"
        bt4["text"]="correct"

     elif(x==Q1[2]):
         bt1["text"]="correct"
         bt2["text"]="wrong"
         bt3["text"]="wrong"
         bt4["text"]="wrong"

     elif(x==Q1[3]):
              bt1["text"]="wrong"
              bt2["text"]="wrong"
              bt3["text"]="correct"
              bt4["text"]="wrong"

    def result():
         
          check(x,Q1,top)


        

    def butt(x,Q1):
          if(x==Q1[0]):
              bt1["text"]=op11[0]
              bt2["text"]=op11[1]
              bt3["text"]=op11[2]
              bt4["text"]=op11[3]
              

          elif(x==Q1[1]):
               bt1["text"]=op12[0]
               bt2["text"]=op12[1]
               bt3["text"]=op12[2]
               bt4["text"]=op12[3]
              
          elif(x==Q1[2]):
               bt1["text"]=op13[0]
               bt2["text"]=op13[1]
               bt3["text"]=op13[2]
               bt4["text"]=op13[3]
              
          elif(x==Q1[3]):
               bt1["text"]=op14[0]
               bt2["text"]=op14[1]
               bt3["text"]=op14[2]
               bt4["text"]=op14[3]

    bt1=Button(root,text=op11[0],command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
    bt1.pack()
    bt1.place(x=370,y=600)
    bt2=Button(root,text=op11[1],command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
    bt2.pack()
    bt2.place(x=760,y=600)
    bt3=Button(root,text=op11[2],command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
    bt3.pack()
    bt3.place(x=370,y=660)
    bt4=Button(root,text=op11[3],command=wow,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
    bt4.pack()
    bt4.place(x=760,y=660)



    while(count!=4):
    

            x=Q1[random.randrange(4)]
            
        
        
            
            #label=Label(root,text=x,bg='black',fg='white',font=('Airal',30),width=width)
            #label.place(x=470,y=505)
            verify(x,y)
            messageVar=tkinter.Message(root,text= x)
            messageVar.config(bg='black',fg='white',font=('Airal',30),width=width)
            messageVar.place(x=400,y=505)
            y.append(x)

            
            

        
                

            count=count+1


    

    

        
    
    


    
            butt(x,Q1)
            break
    







    kcount=kcount+1
    root.mainloop()



          



              










              

   



    




                
           
        
        











       

