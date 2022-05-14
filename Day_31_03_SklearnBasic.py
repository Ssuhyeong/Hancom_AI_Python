# Day_31_03_SklearnBasic.py

import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

from sklearn import datasets, svm, neighbors, model_selection

# 머신러닝은 데이터가 부족할 떄 좋은 영향을 미친다. 하지만 지금 시대에서는 데이터가 넘친다.(빅데이터)
# 결국에는 머신러닝을 통해서 동작하는 방식을 배우는 것이 좋다. 딥러닝이 유망하다

def sklearn_1():
    # load(로컬 데이터), make(신규 데이터 생성), fetch(원격 데이)
    iris = datasets.load_iris()
    print(type(iris))       # <class 'sklearn.utils.Bunch'>
    print(iris.keys())      # dict_keys(['data(x 데이터)', 'target(y 데이터)', 'frame(데이터 프레임)'
                            # , 'target_names(클래스의 이름들)', 'DESCR(데이터 셋에 대한 설', 'feature_names(컬럼의 이름)명', 'filename'])

    # print(iris['feature_names'])  # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    # print(iris['target_names'])   # ['setosa' 'versicolor' 'virginica']

    print(iris.data)    # [[5.1 3.5 1.4 0.2] ...[]]
    print(iris.target)  # [0 0 0 0 0 0 ...]  원핫 벡터

def sklearn_2():
    iris = datasets.load_iris()

    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    print(df)

    scatter_matrix(df)
    # scatter_matrix(df, c=iris.target)       # 분류하기가 쉽다.
    scatter_matrix(df, c=iris.target, hist_kwds={'bins':20})
    scatter_matrix(df, c=iris.target, hist_kwds={'bins':20}, cmap='jet')
    plt.show()

def sklearn_3():
    digits = datasets.load_digits()     # mnist 축소
    print(digits.keys())    # ['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR']

    print(digits.images.shape)      # (1797, 8, 8)
    print(digits.data.shape)        # (1797, 64)
    print(digits.target.shape)      # (1797,)

    print(digits.images[0])
    print(digits.data[0])
    print(digits.target[0])     # 0
    print('-' * 30)

    # (1) 머신러닝/전처리 객체 생성 (2) 학습 (3) 예측/변환
    # clf1 = svm.SVC()                             # 1
    # clf1.fit(digits.data, digits.target)         # 2
    #
    # preds = clf1.predict(digits.data)            # 3

    # print(preds)                                 # [0 1 2 ... 8 9 8]
    # print(digits.target)                         # [0 1 2 ... 8 9 8]

    # 문제
    # 예측 결과를 정확도(%)로 표현하세요

    # print(np.sum(preds == digits.target)/len(preds))
    # print(np.mean(preds == digits.target))
    # print(clf1.score(digits.data, digits.target))

    # accuracy = np.round(accuracy_score(digits.target, preds), 4)
    # print("{0}".format(accuracy))

    # 문제
    # 마지막 1개를 제외한 데이터로 학습해서 마지막 1개를 예측하세요
    clf2 = svm.SVC()
    clf2.fit(digits.data[:-1], digits.target[:-1])      # (1796, 64)
    preds = clf2.predict(digits.data[-1:])              # (1, 64)
    # preds = clf2.predict([digits.data[-1]])           # (1, 64)
    print(preds)
    print(digits.target[-1])

# 문제
# digits 데이터셋에 대해 80%로 학습하고 20%에 대해 정확도를 구하세요
def sklearn_4():
    digits = datasets.load_digits()

    x, y = digits.data, digits.target

    train_size = int(len(x) * 0.8)
    x_train, x_test = x[:train_size], x[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    print(x_train.shape, x_test.shape)          # (1437, 64) (360, 64)
    print(y_train.shape, y_test.shape)          # (1437,) (360,)

    clf = svm.SVC()
    clf.fit(x_train, y_train)

    print('acc : ',clf.score(x_test, y_test))

# 문제 iris 데이터셋에 대해 80%로 학습하고 20%에 대해 정확도를 구하세요
# (최소 90% 이상의 정확도를 달성해야한다.
def sklearn_5():
    iris = datasets.load_iris()

    x, y = iris.data, iris.target

    # wrong
    # np.random.shuffle(x)
    # np.random.shuffle(y)

    # 방법 1. right
    # indices = np.arange(len(x))
    # np.random.shuffle(indices)
    # x, y = x[indices], y[indices]
    # print(x)
    #
    #
    # train_size = int(len(x) * 0.8)
    # x_train, x_test = x[:train_size], x[train_size:]    # (120, 4) (30, 4)
    # y_train, y_test = y[:train_size], y[train_size:]    # (120,) (30,)
    #
    # clf = svm.SVC()
    # clf.fit(x_train, y_train)
    #
    # print('acc : ', clf.score(x_test, y_test))

    # 방법 2
    # model_selection.StratifiedShuffleSplit # 완전 정규화해서 스플릿해준다.
    # data = model_selection.train_test_split(x, y)    # 75:25
    data = model_selection.train_test_split(x, y, train_size=0.8)    # 80:20
    # data = model_selection.train_test_split(x, y, train_size=100)    # 100:50
    # data = model_selection.train_test_split(x, y, train_size=100, test_size=30)    # 80:20
    # data = model_selection.train_test_split(x, y, shuffle=False)    # False 데이터 섞지 않는다. -> 시계열(time-series) 데이터는 이걸 사
    x_train, x_test, y_train, y_test = data

    clf = svm.SVC()
    clf.fit(x_train, y_train)

    print(clf.score(x_test, y_test))
    print('-' * 30)

    clf = svm.SVC(C=1.0, gamma=0.1)      # 하이퍼 파라미터 최적화 (grid Search)
    clf.fit(x_train, y_train)

    print('acc : ', clf.score(x_test, y_test))


# 문제
# neighbors 클래스 분류기를 이용해서 digits 데이터에 대해 80%로 학습하고 20%에 대해 정확도를 구하라
# ( 분류기에 들어가는 이웃의 갯수에 대해 어떤 숫자가 가장 좋은지 최적화를 수행하세요 1~10 )
def sklearn_6():
    digits = datasets.load_digits()

    x_train, x_test, y_train, y_test = model_selection.train_test_split(digits.data, digits.target, test_size=0.8)

    y = []
    # 문제
    # 이웃 갯수별 정확도를 막대그래프로 그려주세
    for i in range(1, 11):
        clf = neighbors.KNeighborsClassifier(n_neighbors = i)
        clf.fit(x_train, y_train)

        acc = clf.score(x_test, y_test)
        # print('acc : {:2} : {}'.format(i, acc))
        y.append(acc)

    plt.bar(range(1, 11), y)
    plt.ylim(0.9, 1)
    plt.show()


# sklearn_1()
# sklearn_2()
# sklearn_3()
# sklearn_4()
sklearn_5()
# sklearn_6()