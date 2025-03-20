import tkinter as tk
import random
import numpy as np
win=tk.Tk()
ca=tk.Canvas(win,width=280,height=280,bg="#000000")
cal=tk.Canvas(win,width=280,height=60)
#X=tk.IntVar(value=0)
#Y=tk.IntVar(value=0)
data=[]
for i in range(28):
    data.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def onLeftButtonMove(event):
    if 0<=event.x<=280 and 0<=event.y<=280:
        X=event.x//10
        Y=event.y//10
        ca.create_rectangle(X*10+1,Y*10+1,X*10+9,Y*10+9,fill="#FFFFFF",outline="#FFFFFF")
        data[X][Y]=random.randint(200,255)
        if X!=0:
            if data[X-1][Y]==0:
                ca.create_rectangle(X*10-9,Y*10+1,X*10-1,Y*10+9,fill="#888888",outline="#888888")
                data[X-1][Y]==random.randint(0,20)
        if X!=27:
            if data[X+1][Y]==0:
                ca.create_rectangle(X*10+11,Y*10+1,X*10+19,Y*10+9,fill="#888888",outline="#888888")
                data[X+1][Y]=random.randint(0,20)
        if Y!=0:
            if data[X][Y-1]==0:
                ca.create_rectangle(X*10+1,Y*10-9,X*10+9,Y*10-1,fill="#888888",outline="#888888")
                data[X][Y-1]=random.randint(0,20)
        if Y!=27:
            if data[X][Y+1]==0:
                ca.create_rectangle(X*10+1,Y*10+11,X*10+9,Y*10+19,fill="#888888",outline="#888888")
                data[X][Y+1]=random.randint(0,20)
def on_key_down(event):
    global data,color,colorbox
    if event.keysym=="N":
        data=[]
        for i in range(28):
            data.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ca.delete("all")
    elif event.keysym=="P":
        l=[]
        for i in data:
           l+=i
        print(l)

def bt_clear():
    global da,data,result
    da=[]
    for i in range(28):
        da.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    ca.delete("all")

i=0
def bt_run():
    
    global da,data,result,i
    #print(data)
    with open("data.txt",'ab') as f:
        np.savetxt(f,data,fmt='%f',delimiter=' ')
    ab=[str(i)+" "]
    with open("label.txt",'ab') as g:
        np.savetxt(g,ab,fmt='%s',delimiter=' ')
    i+=1
    if(i>25):
        i=0
    
    
b_clear=tk.Button(cal,text="Clear",command=bt_clear)
b_run=tk.Button(cal,text="Run",command=bt_run)

ca.pack()
cal.pack()
ca.bind('<B1-Motion>',onLeftButtonMove)
win.bind("<Key>",on_key_down)

b_clear.place(x=75,y=20)
b_run.place(x=155,y=20)
win.mainloop()
