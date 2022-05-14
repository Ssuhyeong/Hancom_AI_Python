# Day_30_01_SklearnPreprocessing.py

from sklearn import preprocessing, impute
import numpy as np

# 머신러닝은 우리가 가는 것은 힘들다. 딥러닝을 해야한다. 시각, 언어 중에서 강의를 듣는 것이 좋다.

def add_dummy_feature() :
    # y = a(기울기)x + b(편향:bias)
    x = [[0, 1],
               [2, 3]]
    # print(preprocessing.add_dummy_feature(x))      # (feature : columns, (변수), dummy : 가짜)
    # [[1. 0. 1.]
    #  [1. 2. 3.]]  왼쪽에 1들이 bias dummy_feature로 만들어진 수

    print(preprocessing.add_dummy_feature(x, value=7).T)


    # 문제
    # 열이 아니라 첫 번째 행에 bias를 추가하세요
    # print(preprocessing.add_dummy_feature(x).T)
    # print(preprocessing.add_dummy_feature(np.transpose(x)).T)


def Binarizer():
    x = [[1., -1., 2.],
         [2., 0., 0.],
         [0., 1., -1.]]

    bin1 = preprocessing.Binarizer()    # 객체 생성
    print(bin1.fit(x))             # fit (학습)
    print(bin1)

    bin2 = preprocessing.Binarizer().fit(x)         # bin1, bin2 중 선택
    print(bin2)

    print(bin1.transform(x))        # 변환한다.
    print(bin2.transform(x))

    print(preprocessing.Binarizer().fit_transform(x), end='\n')         # 0 이하는 0이된다. 0초과는 1로 표현

    print(preprocessing.Binarizer(threshold=-1).fit_transform(x))       # -1 이하는 0이된다.

# 결측치(데이터에 값이 없는 것) 처리
def SimpleImputer():
    # 4 = (1 + 7).mean() / 소수점은 버
    x = [[1, 2],
         [np.nan, 4],
         [7, 9]]
    #                        평균      중간값         최빈값          없는 것처럼무시핻
    # allowed_strategies = ["mean", "median", "most_frequent", "constant"]
    imp = impute.SimpleImputer()
    # imp = impute.SimpleImputer(strategy='mean')
    imp.fit(x)

    print(imp.transform(x), end='\n\n')

    # 문제
    # 아래 코드에서 발생하는 에러를 수정하세
    y = [np.nan, np.nan]

    print(imp.transform(np.reshape(y, (1, -1))))

    print(imp.statistics_)      # [4. 5.]
    print(imp.strategy)         # mean

# 클래스: 중복되지 않은 레이블
def LabelBinarizer():
    x = [1, 2, 6, 2, 4]

    # 0과 1로만 구성된 패턴(숫자)
    # 1. 2진수
    #    000 001 010 011 100 101 110 111
    # 2. 원핫 벡터

    lb1 = preprocessing.LabelBinarizer()
    lb1.fit(x)

    print(lb1.transform(x))
    print('-' * 30)

    x2 = ['yes', 'no', 'yes']

    lb2 = preprocessing.LabelBinarizer()
    lb2.fit(x2)

    print(lb2.transform(x2))        # 원핫 벡터 형식으로 치
    print(lb2.classes_)
    print('-' * 30)

    x3 = ['yes', 'no', 'yes', 'cancel']

    lb3 = preprocessing.LabelBinarizer()
    lb3.fit(x3)

    t = lb3.transform(x3)
    print(t)
    print('-'*30)
    # print(lb3.classes_, end='\n\n')
    #
    # print(lb3.inverse_transform(t))         # 원래 상태로 되돌려준다.

    # 문제
    # transform 결과물인 t를 사용해서 원래 데이터로 복원하세요
    # (invese_transform 호출과 동일한 결과를 만드세요)

    # str = []
    # for i in t :
    #     if i[2] == 1 :
    #         str.append('yes')
    #     elif i[1] == 1 :
    #         str.append('no')
    #     else :
    #         str.append('cancel')
    # print(str)

    # k = [2, 1, 2, 0]
    k = np.argmax(t, axis=1)        # 가장 큰 값에 위치를 알려준다.
    print(lb3.classes_[k])

    # dense, sparse(희소)
    lb4 = preprocessing.LabelBinarizer(sparse_output=True)
    lb4.fit(x3)

    print(lb4.transform(x3))

# LabelEncoder = LabelBinarizer + argmax
def LabelEncoder():
    x = [1, 2, 6, 2, 4]

    lb1 = preprocessing.LabelEncoder()
    lb1.fit(x)

    print(lb1.transform(x))     # [0 1 3 1 2]
    print(lb1.classes_)         # [1 2 4 6]
    print('-' * 30)

    x2 = ['yes', 'no', 'yes']

    lb2 = preprocessing.LabelEncoder()
    lb2.fit(x2)

    print(lb2.transform(x2))  # 원핫 벡터 형식으로 치환
    print(lb2.classes_)
    print('-' * 30)


    x3 = ['yes', 'no', 'yes', 'cancel']

    lb3 = preprocessing.LabelEncoder()
    lb3.fit(x3)

    t = lb3.transform(x3)
    print(t)
    print(lb3.classes_, end='\n\n')

    print(lb3.inverse_transform(t))         # 원래 상태로 되돌려준다.

    # 문제
    # transform 결과물인 t를 사용해서 원핫 벡터를 만드세요
    # (LabelBinarizer 클래스의 transform 호출 결과와 같아야 합니다.)

    encoding = np.eye(len(lb3.classes_), dtype=np.int32)[t]
    print(encoding)

    # [2 1 2 0]

def SrandardScaler():
    x = [[1, -1, -3],
         [2,  0,  1],
         [0,  1,  7]]

    scaler = preprocessing.StandardScaler()
    scaler.fit(x)

    print(scaler.transform(x), end='\n\n')

    print(preprocessing.StandardScaler().fit_transform(x), end='\n\n')

    print(preprocessing.scale(x))

def MinMaxScaler():
    x = [[1, -1, -3],
         [2,  0,  1],
         [0,  1,  7]]

    # columns 기준으로 가장 작은 값 0, 가장 큰 값은 1 작은 값과 큰값의 비율에 따라 중간값은 다르다.

    scaler = preprocessing.MinMaxScaler()
    scaler.fit(x)

    print(scaler.transform(x), end='\n\n')

    print(preprocessing.MinMaxScaler().fit_transform(x), end='\n\n')

    print(preprocessing.minmax_scale(x))
    print('-' * 30)

    # 문제
    # minmax_scale 함수를 직접 구현하세요

    mx = np.max(x, axis=0)
    mn = np.min(x, axis=0)

    # (3, 3) - (3,)
    print((x - mn) / (mx-mn))



# [[0 0 1]
#  [0 1 0]
#  [0 0 1]
#  [1 0 0]]

# add_dummy_feature()
# Binarizer()
# SimpleImputer()

# LabelBinarizer()
# LabelEncoder()

# StandardScaler()
MinMaxScaler()