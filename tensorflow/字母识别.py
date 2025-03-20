import tensorflow as tf
import mnist,os,gzip



def mnist_parse_file(fname):
    fopen = gzip.open if os.path.splitext(fname)[1] == '.gz' else open
    with fopen(fname, 'rb') as fd:
        return mnist.parse_idx(fd)

x_train = mnist_parse_file("emnist-letters-train-images-idx3-ubyte.gz")[:50000]
y_train = mnist_parse_file("emnist-letters-train-labels-idx1-ubyte.gz")[:50000]
x_test = mnist_parse_file("emnist-letters-test-images-idx3-ubyte.gz")[1000:6000]
y_test = mnist_parse_file("emnist-letters-test-labels-idx1-ubyte.gz")[1000:6000]
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
              
model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

