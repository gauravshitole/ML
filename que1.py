"""
1. Write a python program to Prepare Scatter Plot (Use Forge Dataset / Iris
Dataset).
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./Iris.csv')
print(df)

print(df.head())
print(df.tail())

X=df['SepalLengthCm']
X.head()

Y=df['PetalLengthCm']
Y.head()

plt.scatter(X,Y,c='blue')
plt.xlabel("SepalLengthCm")
plt.ylabel("PetalLengthCm")
plt.show()

