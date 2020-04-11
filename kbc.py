
from tkinter import *
import random
y=[]
kcount=0
count=0
while(kcount!=4):

    root=Tk()
    root.title("KBC")
    
    Q1=["Which Fermion has no anti particle", "Which party did Hitler belong to"," What title was given to Aurangazeb","When was the battle of Plassey fought"]
    op11=["electron","proton","neutrino","pi meson"]
    op12=["Congress","BJP","Shiv sena","Nazi Germany"]
    op13=["alamgir","akbar","alampanah","shehensha"]
    op14=["1793","1765","1757","1803"]

    x=StringVar()

   
    def verify(x,y):
        
        while(True):
            if(x in y):
                x=Q1[random.randrange(4)]
                
                

            elif(x not in y):
                
                return 1
                break
                
    def check(x,Q1):
     
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
          check(x,Q1,)


        

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

    bt1=Button(root,text=op11[0],command=result)
    bt1.pack()
    bt1.place(x=0,y=25)
    bt2=Button(root,text=op11[1],command=result)
    bt2.pack()
    bt2.place(x=0,y=50)
    bt3=Button(root,text=op11[2],command=result)
    bt3.pack()
    bt3.place(x=0,y=75)
    bt4=Button(root,text=op11[3],command=result)
    bt4.pack()
    bt4.place(x=0,y=100)



    while(count!=4):
    

            x=Q1[random.randrange(4)]
            
        
        
            if(verify(x,y)==1):
                label=Label(root,text=x)
                label.place(x=0,y=0)
                y.append(x)
            

        
                

            count=count+1


    

    

        
    
    


    
            butt(x,Q1)
            break
    







    kcount=kcount+1
    root.mainloop()



          



              










              

   



    




                
           
        
        











       

