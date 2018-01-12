import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.cross_validation import train_test_split

dataset = pd.read_csv(
    '/Users/howechen/Downloads/Machine Learning A-Z/Part 1 - Data Preprocessing/Data.csv')
print(dataset)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(x)
print(y)

# take care of the missing data
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
print(x)

# for the categorical data we use the labelencoder from sklearn
# 给每个column下的不同元素进行编号, 适用于元素之间有内在关系的，比方说大小，这样子的话大小可以通过编号
# 表现出来，如果没有内在关系，比方说 国家名称，给予编号则会多加了一个内在的比较关系
# LabelEncoder 不关心元素的排列顺序，转而用 OneHotEncoder 做一个dummy encoding table
# 生成一个元素个数的图
# but OneHotEncoder would be based on the labelEncoder
label_encoder_x = LabelEncoder()
x[:, 0] = label_encoder_x.fit_transform(x[:, 0])
print(x)
# [[0 44.0 72000.0]
#  [2 27.0 48000.0]
#  [1 30.0 54000.0]
#  [2 38.0 61000.0]
#  [1 40.0 63777.77777777778]
#  [0 35.0 58000.0]
#  [2 38.77777777777778 52000.0]
#  [0 48.0 79000.0]
#  [1 50.0 83000.0]
#  [0 37.0 67000.0]]

one_hot_encoder = OneHotEncoder(categorical_features=[0])
x = one_hot_encoder.fit_transform(x).toarray()
print(x)

label_encoder_y = LabelEncoder()
y = label_encoder_x.fit_transform(y)
print(y)

# splitting the dataset into training set and test set
# x_train -> y_train, x_test -> y_test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=27)
print(x_train)
print(x_test)
print(y_train)
print(y_test)


# Feature Scaling
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)
sc_y = StandardScaler
print(x_train)
print(x_test)
