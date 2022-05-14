# Day_20_02_MatplotlibBasic.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc         # 한글 폰트
from matplotlib import colors               # 색
import csv
import re

# 복습 문제
# 로그 그래프 4개를 플롯 1개에 그려주세
def f_1():
    x = np.arange(0.01, 2.00, 0.01)

    # 문제
    # 피겨를 2개 만들고, 각각의 피겨에 그래프를 2개씩 출력하세요
    plt.figure()
    plt.grid(True)

    plt.subplot(2, 2, 1)        # 행, 열, 인덱스(1~)
    plt.plot(x, np.log(x))

    plt.subplot(2, 2, 2)
    plt.plot(x, -np.log(x))

    plt.figure()

    plt.subplot(223)           # 동일하다.
    plt.plot(-x, np.log(x))

    plt.subplot(336)
    plt.plot(-x, -np.log(x))

    plt.show()

def f_2():
    men = [15, 30, 40, 25, 35]
    women = [40, 45, 25, 30, 35]

    indices = np.arange(len(men))

    plt.bar(indices, men, width = 0.40, color='b', alpha=0.6)
    plt.bar(indices+0.40, women, width = 0.40, color='r', alpha=0.6)

    plt.xticks(indices + 0.20, ['A', 'B', 'C', 'D', 'E'])

    plt.show()

# 문제
# 1016 파일을 읽어서 2차원 리스트 형식으로 반환하는 함수를 만드세요
def read_gdp_2016():
    f = open('data/2016_GDP.txt', 'r', encoding='utf-8')
    rows = []
    # 1번
    # for line in f :
    #     row = line.strip().split(':')
    #     rows.append(row)
    # rows.pop(0)

    # 2번
    # for i, line in enumerate(f) :
    #     if i > 0 :
    #         rows.append(line.strip().split(':'))

    # 3번
    f.readline()        # 한 줄 읽는 함수 (skip header)
    for line in f :
        rank, name, dollar = line.strip().split(':')

        items = dollar.split(',')
        if len(items) > 1:
            dollar = items[0] + items[1]

        rows.append([name, int(dollar)])

    # for i in rows :
        # i[2] = re.sub(",","",i[2])

    f.close()
    return rows

# 문제
# gdp 파일을 csv 모듈을 사용해서 읽고 결과를 반환하세
def read_gdp_2016_by_csv():
    f = open('data/2016_GDP.txt', 'r', encoding='utf-8')
    rows = []
    f.readline()

    for _, name, dollar in csv.reader(f, delimiter=':', quoting=csv.QUOTE_ALL):
        dollar = dollar.replace(',', '')
        rows.append([name, int(dollar)])

    f.close()

    return rows

# 문제
# 읽어온 내용 중에서 top 10을 뽑아서 막대 그래프로 그려주세
def f_3():
    # gdp = read_gdp_2016()
    gdp = read_gdp_2016_by_csv()
    top_10 = gdp[:10]

    names = [n for n, _ in top_10]
    dollars = [d for _, d in top_10]

    # print(names)
    # print(dollars)

    indices = np.arange(len(names))

    font_name = font_manager.FontProperties(fname='/System/Library/Fonts/Supplemental/AppleGothic.ttf').get_name()

    rc('font', family=font_name)
    plt.bar(indices, dollars)
    # plt.barh(indices, dollars)      # 수평 막대그래프

    plt.xticks(indices, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    # plt.xticks(indices, names, rotation='vertical')     # 수평, 수직
    plt.xticks(indices, names, rotation=45)     # 각도 가능
    # plt.bar(indices, dollars, color='r', alpha=0.7)
    # plt.bar(indices, dollars, color='rgb', alpha=0.7)   # 에러
    # plt.bar(indices, dollars, color=['r', 'g', 'b'], alpha=0.7)     # 번갈아 가면서 색상적용
    # plt.bar(indices, dollars, color=['red', 'green', 'blue'], alpha=0.7)
    # plt.bar(indices, dollars, color=['gold', 'skyblue', 'aqua'])      # 구글에 색상 이름 검색해서 사
    plt.bar(indices, dollars, color=colors.TABLEAU_COLORS)     # TABLEAU, CSS4, BASE 여러 구성이 있다.

    # plt.subplots_adjust(bottom=0.2)         # 그래프가 어느 비율에 있게 하겠다.

    plt.title('2016 GDP')                   # 제목 생성

    plt.subplots_adjust(bottom=0.3, top=0.8)           # top은 반대이다. 20% 위치
    plt.show()


# f_1()
# f_2()
f_3()

