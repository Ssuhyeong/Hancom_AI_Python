# Day_28_01_MatplotlibMiddle.py
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import colors


def plot_1():
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)

    plt.plot(t, s, lw=3)    # lw: line width

    plt.annotate('local max',
                 xy=[2, 1],
                 xytext=[3, 1.5],
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.ylim(-2, 2)         # y 축의 범위를 지
    plt.show()

# 문제(주식 시뮬레이션)          # random walker
# 0에서 시작해서 100개의 난수(-1, 0, 1)를 발생시켜 위아래로 움직이는 꺾은 선 그래프를 그려주세요
def plot_2() :
    # np.random.seed(1)
    # t = np.random.randint(-1, 2).cumsum()
    # s = np.arange(0, 100)
    # plt.plot(s, t)
    #
    # plt.ylim(-10, 10)
    # plt.show()

    pos = 0
    y = [pos]
    for i in range(100) :
        n = random.randrange(-1, 2)
        pos += n
        y.append(pos)
        # plt.plot(i, pos, 'rx')

    plt.plot(range(len(y)), y)
    plt.show()

# 문제
# 앞에서 만든 random walker 그래프를 컴프리헨션 버젼으로 수정하세요
def plot_3() :
    # y = np.cumsum([i for i in np.random.randint(-1, 2, 100)])     # cumsum() 누적 합계

    # randoms = np.random.randint(-1, 2, 101)
    randoms = np.random.choice([-1, 0, 1], 100+1)
    randoms[0] = 0
    #
    # y1 = [sum(randoms[:i+1]) for i in range(len(randoms))]
    # y2 = np.cumsum(randoms)
    # print(randoms)
    # print(y1)
    # print(y2)

    # 문제
    # cumsum 함수와 같은 알고리즘으로 누적 합계를 갖는 리스트를 만드세요

    #
    # y = np.zeros(100, dtype=np.int32)
    # for i in range(100) :
    #     n = random.randrange(-1, 2)
    #     y[i] = y[i-1] + n
    # print(y)

    # 3번
    pos = randoms[0]
    # # print('', pos, end=', ')
    # y3 = [pos]
    # for i in randoms[1:] :
    #     pos += i
    #     y3.append(pos)
    #     # print(pos, end=', ')
    # print()
    #
    # print(y3)

    # 4번
    y4 = [randoms[0]]
    for i in randoms[1:]:
        y4.append(y4[-1] + i)
    print(y4)

    # plt.plot(range(len(y)), y)

    # plt.subplot(1, 2, 1)
    # plt.plot(range(len(y1)), y1, 'r')
    # plt.plot(range(len(y2)), y2, 'b')

    # plt.subplot(1, 2, 2)
    # plt.plot(range(len(randoms)), randoms, 'ro')
    # plt.show()

def plot_4() :
    # print(plt.style.available)
    # ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic'
    # , 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
    # 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
    # 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep',
    # 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
    # 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
    # 'seaborn-whitegrid', 'tableau-colorblind10']

    # print(len(plt.style.available))     # 26

    x = np.linspace(1, 10)

    with plt.style.context('fast'):
        plt.plot(x, np.log(x), 'rx')
        plt.plot(x, np.sin(x))


    plt.show()

# 문제
# matplotlib에서 제공하는 스타일을 적용한 그래프를 한 줄에 5개씩, 모든 그래프를 한 개의 플롯에 그려주세요
def plot_5() :
    # x = np.linspace(1, 10)
    x = np.arange(10)

    plt.figure(figsize=[12, 8])
    plt.figure(figsize=[30, 20])
    for i, style in enumerate(plt.style.available) :
        with plt.style.context(style) :
            plt.subplot(6, 5, i + 1)
            # plt.plot(x, np.log(x), 'rx')
            # plt.plot(x, np.sin(x))

            plt.bar(x, x + np.random.randint(-5, 6, len(x)), color=colors.TABLEAU_COLORS)


    plt.tight_layout()          # 주변 공백을 없애준다.
    # plt.show()
    plt.savefig('data/plt_styles.png')          # 그래프 파일 생

def plot_6() :
    x = np.arange(10)
    y = x + np.random.randint(-5, 6, len(x))

    # 문제
    # subplot2grid 함수를 사용해서 플롯 3개 추가하세

    ax1 = plt.subplot2grid([3, 3], [0, 0], colspan=3)
    ax2 = plt.subplot2grid([3, 3], [1, 0], colspan=3)
    ax3 = plt.subplot2grid([3, 3], [2, 0], colspan=3)

    ax1.plot(x, y, 'r')
    ax2.plot(x, y, 'go')
    ax3.plot(x, y, 'r')

    plt.show()

# plot_1()
# plot_2()
plot_3()
# plot_4()
# plot_5()
# plot_6()