# Day_32_01_MatplotlibColorMap.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm       # colormap

def colormap_1():
    x = np.random.rand(100)
    y = np.random.rand(100)

    # print(np.min(x), np.max(x))

    # plt.plot(x, y, 'ro')        # 산점도. simple version
    # plt.scatter(x, y)             # 산점도. full version

    t = np.arange(len(x))
    plt.scatter(x, y, c=t)          # c = 갯수 컬러에 관한 갯수, 데이터의 갯수와 일치해야한다.

    plt.show()

# 문제
# x 데이터를 사용해서 대각선(X)을 그려보세요
def colormap_2():
    x = np.arange(100)

    # plt.scatter(x, x, c=x)
    # plt.scatter(x[::-1], x, c=x)

    # plt.scatter((x, x[::-1]), (x, x))

    plt.figure(figsize=[10, 5])

    # 문제
    # 100개의 색상이 아니라 2개의 색상 만으로 대각선을 그려보세요
    plt.subplot(1, 4, 1)
    plt.scatter(x, x, c=[0] * 50 + [1] * 50)              # (0, 0) (1, 1) ...
    plt.scatter(x, x[::-1])        # (0, 99) (1, 98) ...

    plt.subplot(1, 4, 2)
    plt.scatter(x, x, c=x)
    plt.scatter(x, 99-x, c=x)           # (0, 99-0) (1, 99-1) ...

    plt.subplot(1, 4, 3)
    plt.scatter(x, x, c=x)              # x: 0 ~ 99
    plt.scatter(x, np.flip(x), c=-x)    # -x: 0 ~ -99

    # viridis 컬러맵의 첫 번째와 마지막 번째 색상
    # (0.267004, 0.004874, 0.329415, 1.0) (0.993248, 0.906157, 0.143936, 1.0)
    print(cm.viridis(0), cm.viridis(255))

    plt.subplot(1, 4, 4)
    plt.scatter(x, x, c=x)

    t = np.arange(0, 10000, 100)
    # plt.scatter(x, list(reversed(x)), c=-t)
    plt.scatter(x, list(reversed(x)), c=t, cmap='viridis_r')

    plt.tight_layout()
    plt.show()


# 문제
# rand 함수가 반환한 데이터를 이용해서 2개의 대각선을 완성하세요
def color_map_3():
    x = np.random.rand(1000)
    x.sort()

    plt.scatter(x, x, c=x)
    plt.scatter(x, 1-x, c=x)      # wrong

    plt.show()

def color_map_4():
    # print(plt.colormaps())
    # ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2',
    # 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r',
    # 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr',
    # 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r',
    # 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia',
    # 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn',
    # 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r',
    # 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r',
    # 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern',
    # 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv',
    # 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink',
    # 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer',
    # 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo',
    # 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

    # 문제
    # 컬러맵 4가지를 골라 각각의 플롯에 적용하세요

    x = np.arange(100)

    plt.figure(figsize=[10, 5])

    plt.subplot(1, 4, 1)
    plt.scatter(x, x[::-1], c=x, cmap='summer')

    plt.subplot(1, 4, 2)
    plt.scatter(x, 99 - x, c=x, cmap='bone')

    plt.subplot(1, 4, 3)
    plt.scatter(x, np.flip(x), c=x, cmap='tab10')

    plt.subplot(1, 4, 4)
    plt.scatter(x, list(reversed(x)), c=x, cmap='twilight_shifted')

    plt.tight_layout()
    plt.show()

def color_map_5():
    # size = 100
    # x = np.random.rand(size ** 2).reshape(size, size)
    # plt.imshow(x)
    # plt.show()

    size = 100
    x = np.arange(size ** 2).reshape(size, size)
    # plt.imshow(x, cmap='cubehelix')
    plt.show()

def color_map_6():
    plasma = cm.get_cmap('plasma')

    # print(plasma(-1))           # (0.050383, 0.029803, 0.527975, 1.0)
    # print(plasma(0))            # (0.050383, 0.029803, 0.527975, 1.0)
    # print(plasma(1))            # (0.063536, 0.028426, 0.533124, 1.0)
    # print(plasma(255))          # (0.940015, 0.975158, 0.131326, 1.0)
    # print(plasma(256))          # (0.940015, 0.975158, 0.131326, 1.0)
    # print()
    #
    # print(plasma(0.1))
    # print(plasma(0.3))
    # print(plasma(0.7))
    # print(plasma(1.0))          # (0.940015, 0.975158, 0.131326, 1.0)

    # 같은 1이지만 실수와 정수에 따라 값이 다르다 즉 값에 따라 범위가 정해진다.

    # 문제
    # 컬러맵에서 가운데에 위치한 색상을 출력하세요  (2가지)

    print(plasma(128))
    print(plasma(0.5))

    print(plasma(127))
    print(plasma(127/255))
    print()

    # for c in np.arange(0, 0.1, 0.001):      # 실제 색은 무제한이아니라 256개의 색상을 사용하고 있다.
    #     print(plasma(c))

    print(plasma(0), plasma(255))
    print(plasma([0, 255]))
    # print(plasma(range(0, 256, 64)))        # 마지막 색상은 포함하지 않는다.
    print(plasma(np.linspace(0, 1, 5)))       # 마지막 까지 포함하여 5가지 색상


# colormap_1()
# colormap_2()
# color_map_3()
# color_map_4()
# color_map_5()
color_map_6()