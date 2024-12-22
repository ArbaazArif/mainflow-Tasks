import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)

data = pd.read_csv('C:\\Users\\rd\\Desktop\\01.Data Cleaning and Preprocessing.csv')
type(data)
pd.core.frame.DataFrame
print(data.info)
data.describe()
data = data.drop_duplicates()
print("\n", data)

print("\n", data.isnull())

print("\n", data.isnull().sum())
data.notnull()

print("\n\n", data.isnull().sum().sum())

data2 = data.fillna(value=0)
print(data2)

data2.isnull().sum().sum()
data

data3 = data.fillna(method = 'pad')
print("\n", data3)

data4 = data.fillna(method = 'bfill')
print("\n", data4)

print("\n", data2.columns)
data2.drop(['Observation'], axis = 1, inplace = True)
print("\n", data2.columns)

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3 - Q1
print("\n", IQR)

data2 = data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis = 1)]
print("\n", data2)

print("\n", data2.describe())
