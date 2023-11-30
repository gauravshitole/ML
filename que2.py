"""2. Write a python program to find all null values from a given data set and
remove them. (Student.csv)
"""
import pandas as pd
df1=pd.read_csv('./student.csv')
print(df1)

df1.isnull()

newdf=df1.dropna()
print()
print()
print()
print()
print()
print(newdf)

