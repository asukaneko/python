import torch
from torch.autograd import Variable
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms as tfs
from torchvision.datasets import MNIST
from datetime import datetime
import numpy
# 定义数据
data_tf = tfs.Compose([tfs.ToTensor(), tfs.Normalize([0.5], [0.5])])

train_set = MNIST('./data', train=True, transform=data_tf)
test_set = MNIST('./data', train=False, transform=data_tf)

train_data = DataLoader(train_set, batch_size=64, shuffle=True)
test_data = DataLoader(test_set, batch_size=64, shuffle=False)

# 定义模型
class rnn_classify(nn.Module):
    def __init__(self, in_feature=28, hidden_feature=100, num_class=10, num_layers=2):
        super(rnn_classify, self).__init__()
        self.rnn = nn.LSTM(input_size=in_feature, hidden_size=hidden_feature, num_layers=num_layers)   # 使用两层LSTM
        self.classifier = nn.Linear(hidden_feature, num_class)      # 将最后一个rnn的输出使用全连接得到最后的分类结果
    def forward(self, x):
        # 先要将 维度为 (batch, 1, 28, 28)的x转换为 (28, batch, 28)
        x = x.squeeze()        # (batch, 1, 28, 28)——(batch, 28, 28)
        x = x.permute(2, 0, 1)     # 将最后一维放到第一维，变成(28, batch, 28)
        out, _ = self.rnn(x)     # 使用默认的隐藏状态，即全0，得到的out是 (28, batch, hidden_feature)
        out = out[-1, :, :]
        out = self.classifier(out)
        return out

net = rnn_classify()
criterion = nn.CrossEntropyLoss()
optimzier = torch.optim.Adadelta(net.parameters(), 1e-1)

def get_acc(output, label):
    total = output.shape[0]
    _, pred_label = output.max(1)
    num_correct = (pred_label == label).sum().data
    # print(num_correct, total)
    return num_correct

def train(net, train_data, valid_data, num_epochs, optimizer, criterion):
    if torch.cuda.is_available():
        net = net.cuda()
    for i in range(num_epochs):
        train_loss = 0
        train_acc = 0
        net = net.train()
        for im, label in train_data:
            if torch.cuda.is_available():
                im = Variable(im.cuda())
                label = Variable(label.cuda())
            else:
                im = Variable(im)
                label = Variable(label)
            # forward
            output = net(im)
            total = output.shape[0]
            loss = criterion(output, label)
            # backward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.data.cpu().numpy()/float(total)
            train_acc += get_acc(output, label).cpu().numpy()/float(total)
        if valid_data is not None:
            valid_loss = 0
            valid_acc = 0
            net = net.eval()
            for im, label in valid_data:
                if torch.cuda.is_available():
                    im = Variable(im.cuda(), volatile=True)
                    label = Variable(label.cuda(), volatile=True)
                else:
                    im = Variable(im, volatile=True)
                    label = Variable(label, volatile=True)
                output = net(im)
                total = output.shape[0]
                loss = criterion(output, label)
                valid_loss += loss.data.cpu().numpy()/float(total)
                valid_acc += get_acc(output, label).cpu().numpy()/float(total)
            print("epoch: %d, train_loss: %f, train_acc: %f, valid_loss: %f, valid_acc:%f"
                  % (i, train_loss/len(train_data),  train_acc/len(train_data),
                  valid_loss/len(valid_data),  valid_acc/len(valid_data)))

        else:
            print("epoch= ", i, "train_loss= ", train_loss/len(train_data), "train_acc= ", train_acc/len(train_data))
# 开始训练
train(net, train_data, test_data, 10, optimzier, criterion)
