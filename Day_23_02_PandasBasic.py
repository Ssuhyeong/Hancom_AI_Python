# Day_23_02_PandasBasic.py
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def dataframe_plot() :
    df = pd.DataFrame({
        'city': ['jeju', 'jeju', 'jeju', 'gunsan', 'gunsan', 'gunsan'],
        'year' : [2018, 2019, 2020, 2018, 2019, 2020],
        'population' : [300, 400, 350, 400, 450, 500]
    })

    # 제주는 왼쪽 플롯에, 군산은 오른쪽 플롯에 막대 그래프로 그려주세요
    # 막대 색상은 다르게, 플롯 위쪽에 도시 이름을 출력하세요

    plt.figure()
    plt.subplot(1, 2 ,1)
    plt.bar(df.head(3)['year'].values, df.head(3)['population'].values)
    plt.bar(df.head(3)['year'].values, df.head(3)['population'].values, color=colors.TABLEAU_COLORS)
    plt.title('Jeju')
    plt.ylim(0, 600)

    plt.subplot(1, 2, 2)
    plt.bar(df.tail(3)['year'].values, df.tail(3)['population'].values)
    plt.bar(df.tail(3)['year'].values, df.tail(3)['population'].values, color=colors.BASE_COLORS)
    plt.title('Gunsan')
    plt.ylim(0, 600)            # 단위 설정

    plt.show()

def dataframe_basic() :
    df = pd.read_csv('data/scores.csv')
    print(df)
    print()

    # print(df.loc[3])
    # print(df.iloc[3])
    # print()

    # print(df.name)
    # print(df['name'])
    print()

    # 모든 학생의 점수 합계를 구하세요

    # print(sum(df.kor) + sum(df.eng) + sum(df.mat) + sum(df.boi))
    # print(np.sum(df.kor.values + df.eng.values + df.mat.values + df.bio.values))
    # print(df.kor.values.sum() + df.eng.values.sum() + df.mat.values.sum() + df.bio.values.sum())
    # print(df.kor.sum() + df.eng.sum() + df.mat.sum() + df.bio.sum())

    # print(sum(df.kor + df.eng + df.mat + df.bio))
    # print((df.kor + df.eng + df.mat + df.bio).sum())

    # print(df.values[:, 2:].sum())

    # print(df.columns)           # Index(['class', 'name', 'kor', 'eng', 'mat', 'bio'], dtype='object')
    # print(df.columns.values)    # ['class' 'name' 'kor' 'eng' 'mat' 'bio']

    subjects = ['kor', 'eng', 'mat', 'bio']
    print(df[subjects])           # 인덱스 배열
    print(df[subjects].sum())
    print(df[subjects].sum().sum())
    print()

    print(df[subjects].sum(axis=0))     # 수직
    print(df[subjects].sum(axis=1))     # 수평
    print('-' * 30)

    # print(df.sum())       # 모든 컬럼에 대해 합계를 계산한다.

    # 문제
    # 과목별 평균과 학생 별제 평

    # print(df[subjects].sum(axis=0) / 12)
    # print(df[subjects].sum(axis=1) / 4)

    # print(df[subjects].mean(axis=0))        # 과목별 평균
    # print(df[subjects].mean(axis=1))        # 학생별 평균
    # print('-' * 50)

    df['avg'] = (df[subjects].mean(axis=1))
    # print(df)
    # print('-' * 30)

    print(df.sort_values('avg'))            # 'avg' 기준으로 정렬
    # print(df.sort_values('avg', ascending=False))   # 내림차순
    print('-' * 30)

    # 문제
    # 넘파이의 argsort 함수를 사용해서 앞의 결과와 똑같이 정렬된 형태로 출력
    # print(df.avg.sort_values().index.values)
    # orders = np.argsort(df.avg.values)
    # orders = np.argsort(df.values[:, -1])
    # print(orders)
    # print(df.loc[orders])   # 오름차순
    # print(df.loc[orders[::-1]])
    print('-' * 30)

    df.index = df.name
    del df['name']
    print(df)
    print('-' * 30)

    # df.avg.plot()
    # df.avg.plot(kind='line')
    # df.avg.plot(kind='bar')
    # df.avg.plot(kind='bar', figsize=[8, 4])     # figsize 픽셀의 크기 숫자 * 100
    #
    # plt.show()

    # 문제
    # matplotlib만 사용해서 avg.plot 함수와 똑같이 그려주세요
    # plt.figure(figsize=(8, 4))
    # plt.bar(df.index, df['avg'].values)
    # plt.show()

    # 문제
    # 1반과 2반 중에서 어느 반의 평균이 높을까요?
    # clas_1 = df.head(6).values[:, -1].mean()
    # clas_2 = df.tail(6).values[:, -1].mean()
    # if clas_1 > clas_2 :
    #     print('1반')
    # else :
    #     print('2반')

    # print(df['class'] == 1)     # broadcast

    # c1 = df[df['class'] == 1]     # 1반만 데리고온다.
    # c2 = df[df['class'] == 2]
    # # print(c1)
    # # print(c2)
    #
    # print('1반 : ', c1.avg.mean())
    # print('2반 : ', c2.avg.mean())

    # 문제
    # 과목별 막대 그래프를 그려보세요
    print(df[subjects])
    # df[subjects].plot(kind='bar')

    # df[subjects].boxplot()

    # 문제
    # 1반과 2반 학생의 데이터를 각각의 박스플롯으로 그려보세요
    c1 = df[df['class'] == 1]
    c2 = df[df['class'] == 2]
    c1[subjects].boxplot()
    plt.figure()
    c2[subjects].boxplot()

    plt.show()

# dataframe_plot()
dataframe_basic()