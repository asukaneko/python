import numpy as np
import tkinter as tk
import mnist
data = mnist.train_images()[:1000]
result = mnist.train_labels()[:1000]
print(result)
win=tk.Tk()
ca=tk.Canvas(win,width=280,height=280,bg="#000000")
ca1=tk.Canvas(win,width=280,height=60)
n=tk.IntVar()
n.set(0)
dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
def f(x):
    a=x//16
    b=x%16
    if a>9:
        a=dic[a]
    else:
        a=str(a)
    if b>9:
        b=dic[b]
    else:
        b=str(b)
    return(a+b)
def g(x,y,z):
    return("#"+f(x)+f(y)+f(z))

def draw(li):
    ca.delete("all")
    for i in range(28):
        for o in range(28):
            ca.create_rectangle(i*10+1,o*10+1,i*10+9,o*10+9,fill=g(li[o][i],li[o][i],li[o][i]),outline=g(li[o][i],li[o][i],li[o][i]))
def bt_n():
    if n==len(data)-1:
        print("当前是最后一个")
    else:
        n.set(n.get()+1)
        draw(data[n.get()].reshape(28,28))
        print(result[n.get()])
def bt_p():
    if n==0:
        print("当前是第一个")
    else:
        n.set(n.get()-1)
        draw(data[n.get()].reshape(28,28))
        print(result[n.get()])

b_n=tk.Button(ca1,text=">>",command=bt_n)
b_p=tk.Button(ca1,text="<<",command=bt_p)


ca.pack()
ca1.pack()

b_p.place(x=25,y=20)
b_n.place(x=75,y=20)

win.mainloop()
