# Day_37_01_SklearnLeaf.py

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm, neighbors
import pandas as pd

# 문제
# leaf.csv 파일을 읽어서 80% 학습하고 20%에 대해 정확도를 구하세요
# 최소 90% 이상의 정확도가 나와야 합니다.

# leaves = pd.read_csv('data/leaf.csv', index_col=0)
#
# target = leaves['species'].values
# data = leaves.iloc[:, 2:].values
#
# x_train, x_test, y_train, y_test = train_test_split(data, target, train_size=0.8)
#
# clf = LogisticRegression(solver='liblinear')
# clf.fit(x_train, y_train)
#
# print('acc : ', clf.score(x_test, y_test))

leaves = pd.read_csv('data/leaf.csv', index_col=0)

x = leaves.values[:, 1:]
y = leaves.values[:, 0]

# print(y[:5])

# ['Acer_Opalus' 'Pterocarya_Stenoptera' 'Quercus_Hartwissiana' 'Tilia_Tomentosa' 'Quercus_Variabilis']
# preprocessing.LabelBinarizer, preprocessing.LavelEncoder 가 자동으로 적용 (머신러닝)
# 딥러닝에서는 숫자로 바꿔야한다.

x = preprocessing.scale(x)
# x = preprocessing.minmax_scale(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
# print(x_train.shape, y_train.shape) # (792, 192) (792,)
# print(x_test.shape, y_test.shape)   # (198, 192) (198,)

# clf = LogisticRegression()
# clf.fit(x_train, y_train)

# clf = svm.SVC()
# clf.fit(x_train, y_train)

clf = neighbors.KNeighborsClassifier(n_neighbors=7)
clf.fit(x_train, y_train)

print('acc : ', clf.score(x_test, y_test))

# linear
# acc : 0.12626262626262627     non-preprocessing
# acc : 0.9696969696969697      scale

# svm
# acc : 0.8585858585858586      non-scale
# acc : 0.9848484848484849      scale

# neighbors
# acc : 0.7878787878787878          non-preprocessing
# acc :  0.9444444444444444         scale