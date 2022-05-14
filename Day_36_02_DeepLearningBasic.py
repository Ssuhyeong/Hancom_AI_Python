# Day_36_02_DeepLearningBasic.py
import matplotlib.pyplot as plt

# 회귀 : 리니어, 멀티플 (아날로그 숫자 예측)
# 분류 : 로지스틱, 소프트맥스 (카테고리 예측)

# Cost Function
#   x : 1 2 3
# ------------------
# 가설 1 : 1 1 1 = 1+1+1 = 3,        1*1 + 1*1 + 1*1 = 3
# 가설 2 : 0 0 2(이상치) = 0+0+2 = 2,  0*0 + 0*0 2*2 = 4
#      mae(Mean Absolute Error)         mse(Mean Square Error)
#       평균 절대값 오차                       평균 제곱 오
# cost가 낮아야 성능이 좋다.

# 1. 가설 계산(결과 예측) -> 모든 데이터에 대해
# 2. 가설과 정답 사이의 거리 계산 -> 모든 데이터에 대해
# 3. 패널티 부여 (제곱) -> 모든 데이터에 대해
# 4. 모든 데이터에 대해서 계산한 오차(error) 평

def cost(x, y, w):
    s = 0
    for i in range(len(x)):
        hx = w * x[i]           # 1번
        c = (hx - y[i])         # 2번
        c **= 2                 # 3번
        s += c                  # 4-1

    return s / len(x)           # 4-2번

def show_cost():
    # y = ax + b
    # hx = wx + b
    #       1 + 0
    # y = 1x + 0
    x = [1, 2, 3]
    y = [1, 2, 3]

    # print(cost(x, y, -1))       # 18.666666666666668
    # print(cost(x, y, 0))        # 4.666666666666667
    # print(cost(x, y, 1))        # 0.0
    # print(cost(x, y, 2))        # 4.666666666666667
    # print(cost(x, y, 3))        # 18.666666666666668

    for i in range(-30, 50):
        w = i / 10
        c = cost(x, y, w)
        print(w, c)

        plt.plot(w, c, 'go')
        # 기울기를 빼면서 값을 측정한다.
    plt.show()

def show_gradient():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w = 5
    for i in range(10) :
        g = gradient_descet(x, y, w)
        w -= g

# show_cost()
show_gradient()

# 미분 : 기울기
#        x축으로 1만큼 이동했을 때 y축으로 이동한 거리
#        x가 y에 미치는 영향

# y = 3             => 0, 미분 상수
# y = ax + b
# y = x             => 기울기 1
# y = 2x            => 기울기 2
# y = (x + 1)       => 기울기 1
# y = xz      1z=1, 2z=2, 3z=3     => 기울기 z
#             1x=1, 2x=2, 3x=3     => 기울기 x

# y = x ^ 2   1=1, 4=2, 9=3     => 기울기가 상황에 따라 다르다
#             x ^ 2 => 2x ^ (2-1) => 2x
#             x ^ 2 => 2x ^ (2-1) * 지수의 대상이 되는 것 (x) 미분
#             x ^ 2 => 2x ^ (2-1) * (x를 ㅌ에 대해 미분)

# y = (x + 1) ^ 2
#            (x + 1) ^ 2 => 2(x_+ 1) ^ (2-1) = 2(x+1)
#            (x + 1) ^ 2 => 2(x_+ 1) ^ (2-1) = 2(x+1) * (x+1의 미분