import matplotlib.pyplot as plt
from tkinter import *
import tkinter
import random
import cv2
import PIL.Image, PIL.ImageTk
kcount=0
count=0
amount=5000
Q1=["Which Fermion has no anti particle", "Which party did Hitler belong to"," What title was given to Aurangazeb","When was the battle of Plassey fought"]
op11=["electron","proton","neutrino","pi meson"]
op12=["Congress","BJP","Shiv sena","Nazi Germany"]
op13=["alamgir","akbar","alampanah","shehensha"]
op14=["1793","1765","1757","1803"]
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
    
    

    x=StringVar()

    def destroy(Q1,x):
        w=Q1.index(x)
        Q1[w]=0
        
        

    def wow():
        top=Toplevel()
        top.title("KBC")
        t=Text(top,height=20,width=30,bg='midnight blue',fg='snow',font=('Airal',12))
        t.pack()
        t.insert(END,"LOCK KIYA JAE?")
        tot=tkinter.Button(top,text="HAAN JI",width=27,command=result,activeforeground='black',bg='light cyan',font=('Airal',12))
        tot.place(x=8,y=30)
        
    def audiencepollsneak(x,Q1,plt):
        perc=[]
        if(x==Q1[0]):
            perc=[25,15,35,25]

        elif(x==Q1[1]):
            perc=[15,25,25,35]

        elif(x==Q1[2]):
            perc=[35,25,15,25]

        elif(x==Q1[3]):
            perc=[25,25,35,15]

        ops=['A','B','C','D']
        plt.bar(ops,perc,color='g')
        plt.legend()
        plt.xlabel("Options")
        plt.ylabel("Percentage")
        plt.title("Audience Poll")
        plt.show()

            

    def audiencepoll():
        audiencepollsneak(x,Q1,plt)

    def fiftysneak(x,Q1):
        if(x==Q1[0]):
            bt1.destroy()
            bt4.destroy()

        elif(x==Q1[1]):
            bt2.destroy()
            bt3.destroy()

        elif(x==Q1[2]):
            bt3.destroy()
            bt4.destroy()

        elif(x==Q1[3]):
            bt1.destroy()
            bt2.destroy()

        

    def fifty():
         fiftysneak(x,Q1)
    
    


   
    
                
    def check(x,Q1):
     top.destroy()

     
     
     if(x==Q1[0]):
    
    
         
         bt3["bg"]="green"
         

     elif(x==Q1[1]):
        
        bt4["bg"]="green"
        
     elif(x==Q1[2]):
         
         bt1["bg"]="green"

     

     elif(x==Q1[3]):
              
              bt3["bg"]="green"

    

    def result():
          
         
          check(x,Q1)


        

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
    ap=Button(root,text="Audience poll",command=audiencepoll,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
    ap.pack()
    ap.place(x=1100,y=40)

    ff=Button(root,text="50 50",command=fifty,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
    ff.pack()
    ff.place(x=1000,y=40)




    while(count!=4):
    

            x=Q1[random.randrange(4)]

            
            while(True):
                if(x==0):
                    x=Q1[random.randrange(4)]

                else:
                    break

            
        
        
            
            #label=Label(root,text=x,bg='black',fg='white',font=('Airal',30),width=width)
            #label.place(x=470,y=505)
            #verify(x,y)
            messageVar=tkinter.Message(root,text= x)
            messageVar.config(bg='black',fg='white',font=('Airal',30),width=width)
            messageVar.place(x=400,y=505)

            messageVar1=tkinter.Message(root,text= amount)
            messageVar1.config(bg='black',fg='white',font=('Airal',15),width=width)
            messageVar1.place(x=650,y=30)
            
            
            

        
                

            count=count+1


    

    

        
    
    


    
            butt(x,Q1)
            break
    






    
    kcount=kcount+1
    amount=2*amount
    
    root.mainloop()
    destroy(Q1,x)
    


          



              










              

   



    




                
           
        
        











       

