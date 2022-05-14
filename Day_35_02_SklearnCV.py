# Day_35_02_SklearnCV.py
from sklearn.datasets import make_blobs, load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, KFold
import matplotlib.pyplot as plt
import numpy as np
import itertools

# 파이썬 64bit, 3.5 ~ 3.8

def show_blobs():
    x, y = make_blobs(random_state=1, centers=7)
    print(x.shape, y.shape)     # (100, 2) (100,)
    print(x[:5])
    print(y[:10])               # [0 6 5 5 5 6 2 3 6 3]

    # 문제
    # x, y를 scatter 플롯에 출력하세요
    plt.scatter(x[:,0], x[:,1], c=y)
    plt.show()

# 문제
# iris 데이터셋을 80% 학습하고 20%에 대해 정확도를 구하요
def cv_1():
    iris = load_iris()
    x, y = iris.data, iris.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)


    clf = LogisticRegression(solver='liblinear')
    clf.fit(x_train, y_train)

    print('acc : ', clf.score(x_test, y_test))

# 문제
# 아래에서 설명한 교차 검증 알고리즘을 구현하세
def cv_2():
    def extract(data, idx):
        return data[idx * 50:idx * 50 + 50]     # idx(1) : [1*50:1*50+50] => [50:100]

    iris = load_iris()
    clf = LogisticRegression(solver='liblinear')

    # cv 3회 적용 (2:1 분할)
    # 분할 3개: 0번(0~49), 1번(50~99), 2번(100~149)
    # 반복 1회: 학습(0번, 1번), 검사(2번)
    # 반복 2회: 학습(1번, 2번), 검사(0번)
    # 반복 3회: 학습(2번, 0번), 검사(1번)

    # itertools.combinations()        # 조합
    # itertools.permutations()        # 순열

    indices = np.arange(len(iris.data))
    np.random.shuffle(indices)

    x, y = iris.data[indices], iris.target[indices]

    # for i1, i2, i3 in [(0, 50, 100), (50, 100, 0), (100, 0, 50)]:
    for i1, i2, i3 in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        x_train = np.vstack([extract(x, i1), extract(x, i2)])
        y_train = np.concatenate([extract(y, i1), extract(y, i2)])
        x_test = extract(x, i3)
        y_test = extract(y, i3)

        # print(x_train.shape, y_train.shape)             # (100, 4) (100,)
        # print(x_test.shape, y_test.shape)               # (50, 4) (50,)

        clf.fit(x_train, y_train)
        print('acc :', clf.score(x_test, y_test))

def cv_3():
    iris = load_iris()
    clf = LogisticRegression(solver='liblinear')

    scores = cross_val_score(clf, iris.data, iris.target)
    print(scores)
    #  [1.         0.96666667 0.93333333 0.9        1.        ]

    scores = cross_val_score(clf, iris.data, iris.target, cv=3)
    print(scores)
    # [0.96 0.96 0.94]

    scores

    scores = cross_val_score(clf, iris.data, iris.target, cv=KFold(n_splits=7))
    print(scores)
    # [1.  1.  0.81818182 0.57142857 1.   0.80952381 0.76190476]

# show_blobs()

# cv_1()
# cv_2()
cv_3()