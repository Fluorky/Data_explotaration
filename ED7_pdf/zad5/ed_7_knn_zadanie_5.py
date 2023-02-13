# -*- coding: utf-8 -*-
"""ED_7_kNN_zadanie_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ArtwdIz-hg09bo4TSV2gEeDadjf1xMkj
"""

import pandas as pd
import numpy as np
import random
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

from sklearn.neighbors import KNeighborsClassifier

dataFile = pd.read_csv('Titanic_train.csv')

dataFile.head()

dataFile = dataFile[["Survived","Pclass","Age", "Sex","SibSp","Parch","Fare","Embarked"]]

dataFile=dataFile.dropna()

dataFile.info()

pclass  =  list(dataFile["Pclass"])
sex  =  list(dataFile["Sex"])
age =  list(dataFile["Age"])
sibSp =   list(dataFile["SibSp"])
parch =  list(dataFile["Parch"])
fare = list(dataFile["Fare"])
#cabin =   list(dataFile["Cabin"])
embarked =   list(dataFile["Embarked"])

survived=list(dataFile["Survived"])

pclass_encoded=le.fit_transform(pclass)
sex_encoded=le.fit_transform(sex)
age_encoded=le.fit_transform(age)
sibSp_encoded=le.fit_transform(sibSp)
parch_encoded=le.fit_transform(parch)
fare_encoded=le.fit_transform(fare)
#cabin_encoded=le.fit_transform(cabin)
embarked_encoded=le.fit_transform(embarked)
survived_encoded=le.fit_transform(survived)

data=list(zip(pclass_encoded,sex_encoded,age_encoded,sibSp_encoded,parch_encoded,embarked_encoded,fare_encoded))#,cabin_encoded))
print(data)

label=le.fit_transform(survived_encoded)
print(label)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=570)

for i in range (3,38):
  neigh = KNeighborsClassifier(n_neighbors=i)
  neigh.fit(x_train,y_train)
  neigh.score(x_test,y_test)
  print(i, " " ,neigh.score(x_test,y_test))

