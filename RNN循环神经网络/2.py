import numpy as np

class SoftMax():

    # 函数原型：e^x/sum(e^x)
    def forward(self, input):
        '''
        正向计算求值
        :param input:
        :return:
        '''
        result = np.exp(input)
        return result / (np.sum(result) + 0.001)
        pass

    def backward(self, output):
        '''
        反向计算求梯度
        :param output: 是正向计算的结果，forward的计算结果
        :return:
        '''
        return output * (1 - output)
        pass
    pass

class Tanh():

    # 函数原型：e^x/sum(e^x)
    def forward(self, input):
        '''
        正向计算求值
        :param input:
        :return:
        '''
        result = np.exp(input)
        result2 = np.exp(-input)
        return (result - result2) / (result + result2)
        pass

    def backward(self, output):
        '''
        反向计算求梯度
        :param output: 是正向计算的结果，forward的计算结果
        :return:
        '''
        return 1 - output ** 2
        pass
    pass

# 手写循环神经网络
# 全连接层只用三层input-hidden-output

class RNN():

    def __init__(self, inputSize, stateSize, outputSize, times=1, maxLen=32,
                 activator=SoftMax, learningRate=0.01):
        '''
        定义网络结构
        :param inputSize: 输入x向量的长度
        :param stateSize: 其实就是s的大小，s其实就是之前dense的hidden层神经元个数
        :param times: 记录时间状态，记录多长时间的状态
        :param maxLen: 最大记忆长度 解决记忆的太长导致梯度消失
        '''
        self.inputSize = inputSize
        self.stateSize = stateSize
        self.outputSize = outputSize
        self.activator = activator

        self.Ux = np.random.uniform(-0.5, 0.5, (stateSize, inputSize))
        self.Ws = np.random.uniform(-0.5, 0.5, (stateSize, stateSize))
        self.Vy = np.random.uniform(-0.5, 0.5, (outputSize, stateSize))

        self.Wb = np.zeros(stateSize)
        self.Vb = np.zeros(outputSize)
        # 记录状态信息
        self.stateList = []      # 有少条样本就有产生多少条状态
        self.times = times       # times是记录的计算次数，一个轮次内，最大是系列总长度
        self.maxLen = maxLen     # 暂时不用吧
        self.outputList = []
        pass

    # 正向计算求结果值
    '''
        :param inputX: 输入的系列，是向量
        :param times:  是时间，初始值为1，说明是第一个样本的计算
        :return:
    '''
    def forward(self, inputX, times, maxLen):
        if times - 1 == 0: # t0时刻对stateList，outputList重置，说明一轮训练结束
            self.stateList = []
            self.outputList = []
            self.stateList.append(np.zeros(self.stateSize))
            self.outputList.append(np.zeros(self.outputSize))
            pass

        # 此处要用tanh激活
        state = np.dot(self.Ux, inputX) + np.dot(self.Ws, self.stateList[times-1]) + self.Wb
        tanh = Tanh()
        state = tanh.forward(state)
        self.stateList.append(state) # 记录当前时刻的状态
        # 此处要用softmax激活
        output = np.dot(self.Vy, state) + self.Vb # 记录t时刻的输出
        softmax = SoftMax()
        output = softmax.forward(output)
        self.outputList.append(output) # 记录t时刻的输出
        self.times = times # 下一个时刻
        return output
        pass

    # 反向传播求梯度
    # 分别求Vy，Ws、Ux以及Wb和Vb的梯度
    # 其中Vy，Ux和Vb的梯度可以直接算出来，唯一就是Ws计算比较复杂
    # loss函数使用 E(y) = -np.sum(y * log(y) + (1 - y)*log)
    # 计算各个时刻的delta，最后T时刻的delta = V(Y(T) - y(T))
    def backward(self, X, inputY, T):
        deltaT = self.Vy.dot(self.outputList[T] - inputY[T-1])
        deltaList = [0 for i in range(0, T+1)]
        deltaList[T] = deltaT
        # 计算1到T-1时刻的delta：
        for t in range(T - 1, 0, -1):
            deltat = self.Vy.dot(self.outputList[t] - inputY[t - 1]) \
                     + (self.Ws.dot(np.diag(1 - self.stateList[t+1] **2))).dot(deltaList[t+1])
            deltaList[t] = deltat
            pass

        # 计算loss/Vb loss/Yy的梯度
        self.vbGrad = np.zeros(shape=self.Vb.shape)
        self.vyGrad = np.zeros(shape=self.Vy.shape)

        # 计算loss/Ws loss/Wb loss/Ux
        self.wsGrad = np.zeros(shape=self.Ws.shape)
        self.wbGrad = np.zeros(shape=self.Wb.shape)
        self.uxGrad = np.zeros(shape=self.Ux.shape)
        for t in range(1, T+1):
            self.vbGrad += self.outputList[t] - inputY[t-1]
            self.vyGrad += np.dot((self.outputList[t] - inputY[t-1])[:, np.newaxis], self.stateList[t][np.newaxis, :])

            self.wsGrad += np.dot(np.dot(np.diag(1 - self.stateList[t]**2), deltaList[t])[:,np.newaxis],
                                  self.stateList[t - 1][np.newaxis,:])
            self.wbGrad += np.dot(np.diag(1 - self.stateList[t] ** 2), deltaList[t])
            self.uxGrad += np.dot(np.dot(np.diag(1 - self.stateList[t] ** 2), deltaList[t])[:, np.newaxis],
                                  X[t-1][np.newaxis, :])
            pass
        pass

    def update(self, learningRate):
        '''
        根据学习速率和已经获得的梯度，更新权重系数和截距项的梯度
        :param learningRate:
        :return:
        '''
        print(self.Ws)
        self.Ux -= self.uxGrad*learningRate
        self.Ws -= self.wsGrad*learningRate
        self.Vy -= self.vyGrad*learningRate

        self.Wb -= self.wbGrad*learningRate
        self.Vb -= self.vbGrad*learningRate

        pass

    def predict(self, input):
        '''
        正向计算，预测结果
        :param input: 是一个向量
        :return:
        '''
        output = self.forward(input, 1, 12)

        return output
        pass

    def fit(self, X, Y, loss=None, epochs=1000, learningRate=0.1):
        '''
        训练模型
        :param X:
        :param y:
        :param loss: 成本函数
        :return:
        '''
        T = len(X)
        for i in range(epochs):
            # epochs
            print("epochs:", i)
            times = 1
            # 正向计算所有的state和output
            for x, y in zip(X, Y):
                self.forward(x, times, T)  # T是系列的总长度，暂时不考虑截取
                times += 1
                pass
            # 反向传播求梯度
            self.backward(X, Y, T)
            # 跟新梯度
            self.update(learningRate)
            pass
        pass

    pass

rnn = RNN(4, 4 , 4)

# 构造训练样本
#  我 是 中国 人
# 我->   [1,0,0,0]
# 是->   [0,1,0,0]
# 中国-> [0,0,1,0]
# 人->   [0,0,0,1]
X = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
y =  np.array([
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,0,0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
])
rnn.fit(X, y)
print(rnn.predict([0,1,0,0]), 1, 12)
