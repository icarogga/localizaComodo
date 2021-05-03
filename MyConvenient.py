import sklearn
import pandas as pd
import numpy as np
import os

os.chdir('/content/drive/MyDrive/datasets')

df = pd.read_csv('my_wifi.csv')

X = df.drop('Class', axis=1)

y = df.copy().pop('Class')

from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.16, random_state=1, stratify=y)

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.19, random_state=1, stratify=y_train)

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=3, weights = 'distance', p = 1)

neigh.fit(X_train, y_train)

predicted_values = neigh.predict(X_val)

from sklearn.metrics import f1_score

print(f1_score(y_val, predicted_values, average='macro'))
print(f1_score(y_val, predicted_values, average='micro'))
print(f1_score(y_val, predicted_values, average='weighted'))

X_train_val = pd.concat([X_train, X_val])
y_train_val = pd.concat([y_train, y_val])

neigh.fit(X_train_val, y_train_val)

predicted_values_test = neigh.predict(X_test)

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

accuracy_score(y_test, predicted_values_test)

print(precision_score(y_test, predicted_values_test, average='macro'))
print(precision_score(y_test, predicted_values_test, average='micro'))
print(precision_score(y_test, predicted_values_test, average='weighted'))

print(recall_score(y_test, predicted_values_test, average='macro'))
print(recall_score(y_test, predicted_values_test, average='micro'))
print(recall_score(y_test, predicted_values_test, average='weighted'))

print(f1_score(y_test, predicted_values_test, average='macro'))
print(f1_score(y_test, predicted_values_test, average='micro'))
print(f1_score(y_test, predicted_values_test, average='weighted'))

confusion_matrix(y_test, predicted_values_test)