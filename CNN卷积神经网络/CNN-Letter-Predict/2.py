import gzip,os,mnist
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

def mnist_parse_file(fname):
    fopen = gzip.open if os.path.splitext(fname)[1] == '.gz' else open
    with fopen(fname, 'rb') as fd:
        return mnist.parse_idx(fd)

train_images = mnist_parse_file("emnist-letters-train-images-idx3-ubyte.gz")[:1000]
train_labels = mnist_parse_file("emnist-letters-train-labels-idx1-ubyte.gz")[:1000]
test_images = mnist_parse_file("emnist-letters-test-images-idx3-ubyte.gz")[11000:16000]
test_labels = mnist_parse_file("emnist-letters-test-labels-idx1-ubyte.gz")[11000:16000]

conv = Conv3x3(8)                    
pool = MaxPool2()                    
softmax = Softmax(13 * 13 * 8,27)    

def forward(image, label):

    out = conv.forward((image / 255) - 0.5)
    out = pool.forward(out)
    out = softmax.forward(out)

    loss = -np.log(out[label])
    acc = 1 if np.argmax(out) == label else 0

    return out, loss, acc

def train(im, label, lr=.005):

    out, loss, acc = forward(im, label)
    
    gradient = np.zeros(27)
    gradient[label] = -1 / out[label]
    
    gradient = softmax.backprop(gradient, lr)
    gradient = pool.backprop(gradient)
    gradient = conv.backprop(gradient, lr)
    
    return loss, acc
    
print('mnist data loaded')


for epoch in range(3):
    print('--- Epoch %d ---' % (epoch + 1))
    permutation = np.random.permutation(len(train_images))
    train_images = train_images[permutation]
    train_labels = train_labels[permutation]
    
    loss = 0
    num_correct = 0
    # i: index
    # im: image
    # label: label
    for i, (im, label) in enumerate(zip(train_images, train_labels)):
        if i > 0 and i % 100 == 99:
            print(
                '[Step %d] Past 100 steps: Average Loss %.3f | Accuracy: %d%%' %
                (i + 1, loss / 100, num_correct)
            )
            loss = 0
            num_correct = 0

        l, acc = train(im, label)
        loss += 1
        num_correct += acc
        
# Test the CNN
print('\n--- Testing the CNN ---')
loss = 0
num_correct = 0
for im, label in zip(test_images, test_labels):
    _, l, acc = forward(im, label)
    loss += l
    num_correct += acc

num_tests = len(test_images)
print('Test Loss:', loss / num_tests)
print('Test Accuracy:', num_correct / num_tests)


data_1=conv.filters
data_2=softmax.weights
b_1=softmax.biases
np.savetxt("weight1.txt",data_1.reshape(1,72),fmt='%f',delimiter=' ')
np.savetxt("weight2.txt",data_2,fmt='%f',delimiter=' ')
np.savetxt("b1.txt",b_1,fmt='%f',delimiter=' ')

def user(image,lab):
    #print(image)
    out = conv.forward((image / 255) - 0.5)
    out = pool.forward(out)
    out = softmax.forward(out)
    ans= np.argmax(out)
    
    print("Pre: {} , Ans: {}".format(chr(ans+96),chr(lab+96)))

for i in range(50):
    user(test_images[i+1000],test_labels[i+1000])
