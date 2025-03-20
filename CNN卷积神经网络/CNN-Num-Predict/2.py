import mnist,random
import numpy as np

class Conv3x3:
    
    def __init__(self, num_filters):
        self.num_filters = num_filters
        self.filters = np.loadtxt("weight1.txt").reshape(num_filters, 3, 3)
        
    def iterate_regions(self, image):

        h, w = image.shape
        
        
        for i in range(h - 2):
            for j in range(w - 2):
                im_region = image[i:(i + 3), j:(j + 3)]
                yield im_region, i, j
                
    def forward(self, input):
 
        self.last_input = input
        #print(type(input))
        h, w = input.shape
        output = np.zeros((h - 2, w - 2, self.num_filters))
        
        for im_region, i, j in self.iterate_regions(input):
            output[i, j] = np.sum(im_region * self.filters, axis=(1, 2))
            
        return output
    
    def backprop(self, d_L_d_out, learn_rate):

        d_L_d_filters = np.zeros(self.filters.shape)
        
        for im_region, i, j in self.iterate_regions(self.last_input):
            for f in range(self.num_filters):

                d_L_d_filters[f] += d_L_d_out[i, j, f] * im_region
                

        self.filters -= learn_rate * d_L_d_filters
        
        return None
        
class MaxPool2:

    def iterate_regions(self, image):

        
        h, w, _ = image.shape
        new_h = h // 2
        new_w = w // 2

        for i in range(new_h):
            for j in range(new_w):
                im_region = image[(i * 2):(i * 2 + 2), (j * 2):(j * 2 + 2)]
                yield im_region, i, j

    def forward(self, input):


        self.last_input = input
        

        h, w, num_filters = input.shape
        output = np.zeros((h // 2, w // 2, num_filters))

        for im_region, i, j in self.iterate_regions(input):
            output[i, j] = np.amax(im_region, axis=(0, 1))
        
        return output
        
    def backprop(self, d_L_d_out):

        d_L_d_input = np.zeros(self.last_input.shape)
        
        for im_region, i, j in self.iterate_regions(self.last_input):
            h, w, f = im_region.shape
            amax = np.amax(im_region, axis=(0, 1))
            
            for i2 in range(h):
                for j2 in range(w):
                    for f2 in range(f):
                        if im_region[i2, j2, f2] == amax[f2]:
                            d_L_d_input[i + i2, j + j2, f2] = d_L_d_out[i, j, f2]
                            
        return d_L_d_input
        
class Softmax:

    def __init__(self, input_len, nodes):

        self.weights = np.loadtxt("weight2.txt").reshape(input_len, nodes)
        self.biases = np.loadtxt("b1.txt")

    def forward(self, input):
 
        self.last_input_shape = input.shape
        
        input = input.flatten()
        
        self.last_input = input

        input_len, nodes = self.weights.shape

        totals = np.dot(input, self.weights) + self.biases
        
        self.last_totals = totals
        
        exp = np.exp(totals)
        return exp / np.sum(exp, axis=0)
    
    def backprop(self, d_L_d_out, learn_rate):
        for i, gradient in enumerate(d_L_d_out):
            if gradient == 0:
                continue

            t_exp = np.exp(self.last_totals)
        
            S = np.sum(t_exp)
            
            d_out_d_t = -t_exp[i] * t_exp / (S ** 2)

            d_out_d_t[i] = t_exp[i] * (S - t_exp[i]) / (S ** 2)

            d_t_d_w = self.last_input  
            d_t_d_b = 1
            d_t_d_inputs = self.weights

            d_L_d_t = gradient * d_out_d_t
        
            d_L_d_w = d_t_d_w[np.newaxis].T @ d_L_d_t[np.newaxis]
            d_L_d_b = d_L_d_t * d_t_d_b
            d_L_d_inputs = d_t_d_inputs @ d_L_d_t
        
            self.weights -= learn_rate * d_L_d_w
            self.biases -= learn_rate * d_L_d_b
    
            return d_L_d_inputs.reshape(self.last_input_shape)

           
#test_images = mnist.test_images()[:1000]
#test_labels = mnist.test_labels()[:1000]
train_images = mnist.train_images()[:10000]
train_labels = mnist.train_labels()[:10000]
test_images = mnist.test_images()[:1000]
test_labels = mnist.test_labels()[:1000]

conv = Conv3x3(8)                    
pool = MaxPool2()                    
softmax = Softmax(13 * 13 * 8, 10)    


cor=0
tes=300
def test(image,lab):
    global cor
    #print(image)
    #out = conv.forward((image / 255) - 0.5)
    out = conv.forward(image)
    out = pool.forward(out)
    out = softmax.forward(out)
    ans= np.argmax(out)
    if(ans==lab):
        cor+=1
    print("predict: {} ,ans: {} ".format(ans,lab))

def user(image):
    global cor
    #print(image)
    #out = conv.forward((image / 255) - 0.5)
    out = conv.forward(image)
    out = pool.forward(out)
    out = softmax.forward(out)
    ans= np.argmax(out)
    print("predict:{}".format(ans))

for i in range(tes):
    test(test_images[i],test_labels[i])
print(cor/tes)


import tkinter as tk
win=tk.Tk()
ca=tk.Canvas(win,width=280,height=280,bg="#000000")
ca1=tk.Canvas(win,width=280,height=60)
da=np.zeros((28,28))
def onLeftButtonMove(event):
    if 0<=event.x<=280 and 0<=event.y<=280:
        X=event.x//10
        Y=event.y//10
        ca.create_rectangle(X*10+1,Y*10+1,X*10+9,Y*10+9,fill="#FFFFFF",outline="#FFFFFF")
        da[X][Y]=random.randint(200,255)
        if X!=0:
            if da[X-1][Y]==0:
                ca.create_rectangle(X*10-9,Y*10+1,X*10-1,Y*10+9,fill="#888888",outline="#888888")
                da[X-1][Y]==random.randint(100,200)
        if X!=27:
            if da[X+1][Y]==0:
                ca.create_rectangle(X*10+11,Y*10+1,X*10+19,Y*10+9,fill="#888888",outline="#888888")
                da[X+1][Y]=random.randint(100,200)
        if Y!=0:
            if da[X][Y-1]==0:
                ca.create_rectangle(X*10+1,Y*10-9,X*10+9,Y*10-1,fill="#888888",outline="#888888")
                da[X][Y-1]=random.randint(100,200)
        if Y!=27:
            if da[X][Y+1]==0:
                ca.create_rectangle(X*10+1,Y*10+11,X*10+9,Y*10+19,fill="#888888",outline="#888888")
                da[X][Y+1]=random.randint(100,200)
        
def on_key_down(event):
    global da,data,result
    if event.keysym=="M":
        da=[]
        for i in range(28):
            np.append(da,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],axis=0)
        ca.delete("all")
    elif event.keysym=="R":
        re=run(da)
        if re.max()>=0.5:
            print(np.argmax(re),re.max())
        else:
            print("I don't know")
    elif event.keysym=="P":
        print(da)
    elif event.keysym=="N":
        tr_ans=int(input("true answer:"))
        tr_arr=[0,0,0,0,0,0,0,0,0,0]
        tr_arr[tr_ans]+=1
        
        result=np.append(result,tr_arr)
        #print(result)
        re_long=int(len(result)/10)
        result=result.reshape(re_long,10)
        np.savetxt("result.txt",result,fmt='%f',delimiter=' ')
        
        data=np.append(data,da)
        da_long=int(len(data)/784)
        data=data.reshape(da_long,784)
        #print(data.shape)
        np.savetxt("data.txt",data,fmt='%f',delimiter=' ')
    elif event.keysym=="Y":
        tr_ans=np.argmax(run(da))
        tr_arr=[0,0,0,0,0,0,0,0,0,0]
        tr_arr[tr_ans]=1
        #print("signed",tr_arr[tr_ans])
        result=np.append(result,tr_arr)
        re_long=int(len(result)/10)
        result=result.reshape(re_long,10)
        #print(result)
        np.savetxt("result.txt",result,fmt='%f',delimiter=' ')
        
        data=np.append(data,da)
        da_long=int(len(data)/784)
        data=data.reshape(da_long,784)
        np.savetxt("data.txt",data,fmt='%f',delimiter=' ')
        print("ok")
    elif event.keysym=="l":
        print(result)
    
def bt_clear():
    global da,data,result
    da=np.zeros((28,28))
    ca.delete("all")

def bt_run():
    global da,data,result
    user(da)
    
b_clear=tk.Button(ca1,text="Clear",command=bt_clear)
b_run=tk.Button(ca1,text="Run",command=bt_run)

ca.pack()
ca1.pack()
ca.bind('<B1-Motion>',onLeftButtonMove)
win.bind("<Key>",on_key_down)
b_clear.place(x=25,y=20)
b_run.place(x=75,y=20)
win.mainloop()
