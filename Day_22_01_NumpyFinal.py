# Day_22_01_NumpyFinal.py
import numpy as np

# a = np.arange(12).reshape(3, 4)
# print(a)

# 문제
# 2차원 넘파이 배열(a)을 거꾸로 출력하세요

# print(a[:,::-1][::-1])
# print(a[::-1, :])   # 행 정렬
# print(a[:, ::-1])   # 열 정렬
# print('-'*30)
#
# print(a[::-1, ::-1])    # 거꾸로 출력

a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

# print(a)    # [[0 1 2] [3 4 5]]
# print(b)    # [[6 7 8] [9 10 11]]

# (2, 3)과 (2, 3) 연결 -> 행 연결, 열 연결
# print(np.concatenate([a, b]))       # 행으로 두 배열을 합칠 때 사용, 2차원 배열을 1차원으로 바꿀 때 사용
# print(np.concatenate([a, b], axis=1))   # 기본값은 0, 0 -> (4, 3) , 1 -> (2, 6)
#
# print(np.vstack([a, b]))    # (4, 3) v : vertical
# print(np.hstack([a, b]))    # (2, 6) h : horizontal



c = np.arange(12).reshape(3, 4)
# print(c)
# print()
#
# print(np.transpose(c))          # 행이 열이되고 열이 행이된다.
# print(c.transpose())
# print(c.T)

# 행렬 곱셈(점곱 연산, point-wise 곱셈)
# print(np.dot(c, c))         # 에러. (3, 4) @ (3, 4)
# print(np.dot(c, c.T))       # (3, 4) @ (4, 3) = (3, 3)
# print(np.dot(c.T, c))         # (4, 3) @ (3, 4) = (4, 4)

# 문제
# 2차원 넘파일 배열을 반복문을 사용해서 전치 형태로 출력하세요
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# for j in range(4) :
#     for i in range(3) :
#         print(c[i, j], end=' ')
#     print()


# for i in range(c.shape[1]) :
#     print(c[:,i])
print('-' * 30)

# 문제
# 테두리는 1로 속은 0으로 채워진 5x5 배열을 만드세요 (zeros 함수를 사용)

d = np.zeros([5, 5], dtype=np.int32)

# d[0, :] = 1
# d[:, 0] = 1
# d[-1, :] = 1
# d[:, -1] = 1
#
# print(d)

# 문제
# 테두리는 1로, 속은 0으로 채워진 5ㅌ5 배열을 만드세요 (ones 함수 사용)

e = np.ones([5, 5], dtype=np.int32)
e[1:-1, 1:-1] = 0
# print(e)

# 문제
# 5x5 배열의 대각선 방향으로 숫자 3을 채우세요
# e = np.ones([5, 5], dtype=np.int32)
# for i in range(5) :
#     e[i, i] = 3
#     e[i, -1-i] = 3

print(e)