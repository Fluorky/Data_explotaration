# -*- coding: utf-8 -*-
"""ED_lab_8_regresja_logistyczna.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-NnEXHpCFVRbA9ZHMtFE9tfeDbxrIjO-

Import biblioteki **TensorFlow** ([https://www.tensorflow.org/](https://www.tensorflow.org/)) z której będziemy korzystali w **uczeniu maszynowym**:
"""

import tensorflow as tf
import matplotlib.pyplot as plt 
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense

"""**Dwa gangi**

Zbiór danych:
"""

[0]*10+[1]*10

x_label1 = np.random.normal(3, 1, 1000)
y_label1 = np.random.normal(2, 1, 1000) 
x_label2 = np.random.normal(7, 1, 1000)
y_label2 = np.random.normal(6, 1, 1000)

xs = np.append(x_label1, x_label2)
ys = np.append(y_label1, y_label2) 
labels = np.asarray([0.]*len(x_label1)+[1.]*len(x_label2))
labels

plt.scatter(x_label1, y_label1, c='r', marker='x', s=20)
plt.scatter(x_label2, y_label2, c='g', marker='1', s=20)
plt.show()

x_label1

"""Definiujemy model:"""

model = Sequential()

"""Dodajemy **jedną warstwę** (Dense) z **jednym neuronem** (units=1) z **biasem** (use_bias=True) i **liniową funkcją aktywacji** (activation="linear"):"""

model.add(Dense(units = 1, use_bias=True, input_dim=2, activation = "sigmoid"))

"""Definiujemy **optymalizator** i **błąd** (entropia krzyżowa). **Współczynnik uczenia = 0.1**"""

#opt = tf.keras.optimizers.Adam(learning_rate=0.1)
opt = tf.keras.optimizers.SGD(learning_rate=0.1)

model.compile(loss='binary_crossentropy',optimizer=opt)

"""Informacja o modelu:"""

model.summary()

"""Przygotowanie danych:"""

xs=xs.reshape(-1,1)
ys=ys.reshape(-1,1)
data_points=np.concatenate([xs,ys],axis=1)
data_points

"""Proces **uczenia**:"""

epochs = 100
h = model.fit(data_points,labels, verbose=1, epochs=epochs,validation_split=0.2)

Loss = h.history['loss']
Loss

"""Sprawdźmy jakie są **wartości wag**:"""

weights = model.get_weights()

print(weights[0])
print(weights[1])    #bias

plt.scatter(np.arange(epochs),h.history['loss'])
plt.scatter(np.arange(epochs),h.history['val_loss'],c='r')
plt.show()

"""Sprawdzamy działanie modelu dla punktu o współrzędnych **x** i **y**:"""

x=7.0
y=5.0 
plt.scatter(x_label1, y_label1, c='r', marker='x', s=20)
plt.scatter(x_label2, y_label2, c='g', marker='1', s=20)
plt.scatter(x,y,c='b', marker='s')
plt.show()

model.predict([[x,y]])






