# -*- coding: utf-8 -*-
"""ED_9_regresja_softmax_TODO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y_11lEkAKgQ-6FcWDt5zAH11iG-Ezsw6
"""

import tensorflow as tf
import matplotlib.pyplot as plt 
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense

"""# Regresja **softmax**"""

s = [0.2, 0.1, 0.6, 0.1]
exps = [np.exp(i) for i in s]
sum_of_exps = sum(exps)
softmax = [j/sum_of_exps for j in exps]

"""##3 gangi

Zbiór danych:
"""

x_label0 = np.random.normal(1, 1.5, (1000, 1)) 
y_label0 = np.random.normal(1, 1.5, (1000, 1)) 
x_label1 = np.random.normal(5, 1.5, (1000, 1)) 
y_label1 = np.random.normal(4, 1.5, (1000, 1)) 
x_label2 = np.random.normal(8, 1.5, (1000, 1)) 
y_label2 = np.random.normal(0, 1.5, (1000, 1))

data_label0 = np.concatenate([x_label0, y_label0],axis=1) 
data_label1 = np.concatenate([x_label1, y_label1],axis=1)  
data_label2 = np.concatenate([x_label2, y_label2],axis=1)   
points = np.concatenate([data_label0, data_label1, data_label2],axis=0)

"""Kodowanie one-hot"""

labels = np.array([[1., 0., 0.]] * len(data_label0) + [[0., 1., 0.]] * len(data_label1) + [[0.,0., 1.]] * len(data_label2))

points.shape,labels.shape

plt.scatter(x_label0, y_label0, c='r', marker='x', s=20)
plt.scatter(x_label1, y_label1, c='b', marker='x', s=20)
plt.scatter(x_label2, y_label2, c='g', marker='x', s=20)
plt.show()

model = Sequential()

model.add(Dense(units = 3, use_bias=True, input_dim=2, activation = "softmax"))

#opt = tf.keras.optimizers.Adam(learning_rate=0.1)
opt = tf.keras.optimizers.Adam()
#opt = tf.keras.optimizers.SGD(learning_rate=0.1)

model.compile(loss='binary_crossentropy',optimizer=opt)

model.summary()

epochs = 1000
#h = model.fit(data_points,labels, verbose=1, epochs=epochs,validation_split=0.2)
h = model.fit(points,labels, verbose=1, epochs=epochs, batch_size= 70, validation_split=0.2)

Loss = h.history['loss']
Loss

weights = model.get_weights()

print(weights[0])
print(weights[1])    #bias

plt.scatter(np.arange(epochs),h.history['loss'])
plt.scatter(np.arange(epochs),h.history['val_loss'],c='r')
plt.show()

model.predict([[4,6]])