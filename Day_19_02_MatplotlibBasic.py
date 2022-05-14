# Day_19_02_MatplotlibBasic.py
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([10, 20, 30, 40, 50])

# plt.plot([1, 2, 3, 4], [1, 2, 3, 4])            # 꺾은 선 그래프 (x, y)
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'ro')      # marker, 점 (red o), 'ro'에서 r은 색깔, o는 모양

# 문제
# 여러분이 좋아하는 마커를 검정색으로 표시하세요
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'b*')      # blue , * 모양

# def plot_1() :
#     plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'k*')      # black, * 모양
#     plt.show()

# 문제
# x의 범위가 -10에서 10일때, x^2 그래프를 그려주세
def plot_2() :
    # 1번
    # for x in range(-10, 11) :
        # plt.plot(x, x**2, 'rx')       # 너무 많이 호출해서 비효율적이다. 또한 선 그래프는 그려지지 않는다.

    # 2번
    # x, y = [], []                     # 너무 많은 코드가 들어가서 조금 비효율
    # for i in range(-10, 11) :
    #     x.append(i)
    #     y.append(i*i)
    # plt.plot(x, y, 'rx')적

    # 3번
    # x = range(-10, 11)
    # y = [i ** 2 for i in x]
    # plt.plot(x, y, 'rx')

    # 4번
    # x = np.arange(-10, 11)
    # plt.plot(x, x**2, 'rx')

    # 5번
    x = np.linspace(-10, 10, 31)
    plt.plot(x, x**2, 'rx')         # scatter
    plt.plot(x, x**2)               # line

    # a = np.array(range(-10, 11))
    # plt.plot(a, a**2, 'k*')
    plt.show()

def plot_3() :
    t = np.arange(0, 5, 0.2)

    plt.plot(t, t, 'r--')
    plt.plot(t, t**2, 'g>')
    plt.plot(t, t**3, 'bp')

    plt.show()

# 문제
# desmos.com에서 그렸던 로그 그래프 4개를 한 개의 플롯에 그려보세
def plot_4() :
    x = np.arange(0.01, 2.0, 0.01)
    plt.grid(True)          # 선 생성

    plt.plot(x, np.log(x))
    plt.plot(x, -np.log(x))
    plt.plot(-x, np.log(x))
    plt.plot(-x, -np.log(x))

    plt.show()


# plot_1()
# plot_2()
# plot_3()
plot_4()