# -*- coding: utf-8 -*-
"""Zad5_PCA_HR_comma_sep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sYuzgfw_vAGqhWMwzBCweO8x9VytGg3z

# **ANALIZA SKŁADOWYCH GŁÓWNYCH**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from sklearn.decomposition import PCA

"""Załadowanie zbioru danych:"""

data=pd.read_csv('HR_comma_sep.csv')
data

corr=data.corr()

sb.heatmap(corr,xticklabels=corr.columns,yticklabels=corr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

CorrMatrix = np.array(data.corr())
CorrMatrix

plt.scatter(data.iloc[:,1], data.iloc[:,2])
plt.axis('equal');
plt.show()

plt.scatter(data.iloc[:,1], data.iloc[:,3])
plt.axis('equal');
plt.show()

plt.scatter(data.iloc[:,2], data.iloc[:,3])
plt.axis('equal');
plt.show()

w, v = np.linalg.eig(CorrMatrix)
print(w)
print(v)

v[:,0]

v[:,1]

v[:,2]

v[:,3]

v[:,4]

v[:,5]

v[:,6]

v[:,7]

data2=data.drop("sales", axis='columns')

data2=data2.drop("salary", axis='columns')

"""## Dwie składowe główne

Wyliczamy dwie składowe główne (**n_components=2**) czyli wektory bazowe nowego układu współrzędnych:
"""

pca = PCA()
pca.fit(data2)
cumsum = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax(cumsum >= 0.95) + 1

d

pca = PCA(n_components=2)
pca.fit(data2)

"""Wektory bazowe nowego układu wpółrzędnych: """

print(pca.components_)

"""Wariancje dla nowych współrzędnych:"""

print(pca.explained_variance_)

"""Dodajemy do wykresu wektory wyznaczające nowy układ współrzędnych. Ich długość określona jest przez wariancje: """

def draw_vector(v0, v1, ax=None):
  ax = ax or plt.gca()
  arrowprops=dict(arrowstyle='->',
  linewidth=2,
  shrinkA=0, shrinkB=0, color='black')
  ax.annotate('', v1, v0, arrowprops=arrowprops)

pca.explained_variance_

#plt.scatter(data2.iloc[:, 0], data2.iloc[:, 4], alpha=0.2)
#for length, vector in zip(pca.explained_variance_, pca.components_):
 # v = vector * 3 * np.sqrt(length)
 # draw_vector(pca.mean_, pca.mean_ + v)
#plt.axis('equal');

"""Współrzędne punktów w **nowym układzie współrzędnych**:"""

data_pca = pca.transform(data2)
data_pca

plt.scatter(data_pca[:,0], data_pca[:,1])
plt.axis('equal');

"""## Jedna składowa główna

Wyliczamy jedną składową główną (**n_components=1**) - chcemy wyeliminować jeden wymiar danych.
"""

pca = PCA(n_components=1)
pca.fit(data2)

"""Współrzędne punktów w **nowym układzie współrzędnych**:"""

data_pca = pca.transform(data2)

"""Porówanie kształtów danych początkowych i po redukcji jednego wymiaru:"""

print("Początkowy shape: ", data2.shape)
print("Po transformacji shape:", data_pca.shape)

"""Dane początkowe i po redukcji wymiaru:"""

data_new = pca.inverse_transform(data_pca)
plt.scatter(data2.iloc[:, 1], data2.iloc[:, 2]),
plt.scatter(data_new[:, 0], data_new[:, 1]),
plt.axis('equal');
