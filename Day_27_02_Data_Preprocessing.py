# Day_27_02_Data_Preprocessing.py

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

### LabelEncode API ##


items = ['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
# print('Label Encoding result: ', labels)
# Label Encoding result:  [0 1 4 5 3 3 2 2]
# print('Encoding classes: ', encoder.classes_)
# Encoding classes:  ['TV' '냉장고' '믹서' '선풍기' '전자레인지' '컴퓨터']
# print('Decoding values: ', encoder.inverse_transform([4, 5, 2, 0, 1, 3]))
# Decoding values:  ['전자레인지' '컴퓨터' '믹서' 'TV' '냉장고' '선풍기']

### one-Hot Encoding API ### -> 해당 item은 1 나머지는 0으로 처리

labels = labels.reshape(-1, 1)

one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit(labels)

one_hot_labels = one_hot_encoder.transform(labels)
print(one_hot_labels.toarray())

# [[1. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 1.]
#  [0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]]

### StandardScaler API ### -> 데이터 값의 범위를 일정한 수준으로 변환하는 전처리 기법

# 표준화 : 평군이 0, 분산이 1인 Gaussian Normal Distribution 으로 변환
# 정규화 : 서로 다른 스케일의 데이터의 크기를 통일

iris = load_iris()
iris_data = iris.data
df_iris = pd.DataFrame(data=iris_data, columns=iris.feature_names)
# print('Average')
# print(df_iris.mean())   # 평균
# print('\nVariance')
# print(df_iris.var())    # 분산

scaler = StandardScaler()
scaler.fit(df_iris)
scaled_iris = scaler.transform(df_iris)
df_scaled_iris = pd.DataFrame(data=scaled_iris,
                              columns=iris.feature_names)
#
# print('Average')
# print(df_scaled_iris.mean())
# print('\nVariance')
# print(df_scaled_iris.var())

# 평균이 0 분산이 1로 유사하게 변환

### MinMaxScaler API ###

# 데이터 값의 범위를 0 ~ 1 사이로 변환, 음수 존재 시 -1 ~ 1 사이로 변환

scaler = MinMaxScaler
scaler.fit(df_iris)
scaled_iris = scaler.transform(df_iris)
df_scaled_iris = pd.DataFrame(data=scaled_iris,
                              columns=iris.feautre_names)
print('Min Value')
print(df_scaled_iris.min())
print('\n Max Value')
print(df_scaled_iris.max())

# 머신러닝 프로젝트 사이트
# Kaggle