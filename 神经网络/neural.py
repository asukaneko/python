import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))
    
class Neuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias
        
    def feedforward(self,inputs):
        total = np.dot(self.weights,inputs) + self.bias
        return sigmoid(total)
#神经网络
class NeuralNetwork:
  def __init__(self,weights,bias):
    #weights = np.array([0, 1])
    #bias = 0
    self.weights = weights
    self.bias = bias
    #实例化三个神经元
    self.h1 = Neuron(self.weights, self.bias)
    self.h2 = Neuron(self.weights, self.bias)
    self.o1 = Neuron(self.weights, self.bias)

  def feedforward(self, x):
    out_h1 = self.h1.feedforward(x)
    out_h2 = self.h2.feedforward(x)
    #把前面两个神经元的输出当作这个神经元的输入
    out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
    return out_o1


