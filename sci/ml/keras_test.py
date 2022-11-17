import os
os.system('nvidia-smi')
import tensorflow as tf
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist

if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
   print("Please install GPU version of TF")

some_variable = 5

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1, batch_size=10)
model.evaluate(x_test, y_test)

print(tf.__version__)

print("I owe you nothing!")

fig = plt.figure()

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y)
plt.savefig("test.png")



def background(f,x):
    '''
    Takes a function f and extend using analytic continuation (either by least square fitting
    or by some other polynomial and extends into the x range.
    :param f:
    :return: y
    '''