# Day_23_01_NumpyFinal.py
import numpy as np

a = np.arange(12)
print(a)
print()

print(a[0], a[7], a[11])
b = [0, 7, 11]
print(a[b])                      # 인덱스 배열.   [ 0  7 11]
print(a[[0, 7, 11]])

c= [[2, 9], [3, 8]]
# print(a[c])                      # 에러
d = np.int32(c)
print(a[d])                        # [[2 9] [3 8]]. 넘파이 배열은 인덱스로 가능
print(a[d.reshape(-1)])            # [2 9 3 8]
print(a[d.reshape(-1).reshape(2, 2)])
print('-' * 30)

e = a.reshape(3, 4)
print(e)

print(e[0], e[-1], e[1])
print(*e[[0, -1, 1]])
print()

f = [[0, 1], [2, 3]]
# print(e[f])                       # [2 7], deprecated <오류>
print(e[[0, 1], [2, 3]])            # [2 7], 팬시 인덱싱 + 인덱스 배열 0행 2열, 1행 3열
print(e[(0, 1), (2, 3)])            # [2 7]
print()

# 팬시 인덱싱 : 정수(스칼라), 슬라이싱, 리스트(튜플, 배열)
print(e[0, (2, 3)])                 # 정수, [2 3]
print(e[:2, (2, 3)])                # 슬라이싱  [[2 3] [6 7]]
print(e[(1, 2), (2, 3)])            # 튜플.    [6 11]
print('-' * 30)

# 문제
# 테두리는 1로, 속은 0으로 채워진 5x5 배열을 만드세요 ( zeros 함수 사용 )

g = np.zeros([5, 5], dtype= np.int32)
g[[0, -1]] = 1
g[:, [0, -1]] = 1

# print(g)

# 문제
# 앞에서 만든 5x5 2차원 배열에 대해 대각선 양쪽(x자 형태)으로 3을 넣어주세요
# for i in range(len(g)) :
#     g[i, i] = 3
#     g[i, -i-1] = 3

# for i in range(len(g)) :
#     g[i, [i, -i-1]] = 3

# g[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]] = 3
# g[[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]] = 3

# h = np.arange(g.shape[0])
# g[h, h] = 3
# # g[h, h[::-1]] = 3
# g[h, 4-h] = 3

# g[0, [0, 4]] = 3
# g[1, [1, 3]] = 3
# g[2, [2, 2]] = 3
# g[3, [3, 1]] = 3
# g[4, [4, 0]] = 3

# g[range(5), range(5)] = 3
# g[range(5), list(reversed(range(5)))] = 3
# g[range(5), range(5-1, -1, -1)] = 3

# print(g)
print('-' * 30)

# print(a)
# print(a > 5)
# print(a[a>5])         # 참인 값만 필터
# print()

print(e)
print(e > 5)
print(e[e > 5])

e[e>5] = 99
print(e)
print('-' * 30)

np.random.seed(1)

# k = np.random.random_integers(0, 10, 12)                # 끝 값이 포함된 난수
k = np.random.randint(0, 100, 12)
print(k)                # [37 12 72  9 75  5 79 64 16  1 76 71]
print(np.max(k))        # 79
print(np.argmax(k))     # 6 ( 가장 큰 값의 인덱스를 반환 )
print(k[np.argmax(k)])  # 79
print('-' * 30)

m = np.reshape(k, [3, 4])
print(m)
print(np.argmax(m))     # 6
print(np.argmax(m, axis = 0))       # 수직에서 비교
print(np.argmax(m, axis = 1))       # 수평에서 비교
print()

print(np.sort(k))           # [ 1  5  9 12 16 37 64 71 72 75 76 79]

# 문제
# argsort 함수를 사용해서 정렬된 결과를 출력하세요

print(np.argsort(k))        # [ 9  5  3  1  8  0  7 11  2  4 10  6]

print(k[np.argsort(k)])
print('-' * 30)

t = [1, 0, 3, 0, 0, 2]
print(np.nonzero(t))        # (array([0, 2, 5]),) 0이 아닌 숫자들에 대한 인덱스
# print(t[np.nonzero(t)])   # 리스트는 에러

w = np.int32(t)
print(w[np.nonzero(w)])     #[1 3 2]
print(w[w>0])           # 음수 고려 안함
print()

v = np.reshape(t, [2, 3])
print(v)
print(np.nonzero(v))  # (array([0, 0, 1]), array([0, 2, 2]))
print('-' * 30)

print(np.eye(5, dtype=np.int32))        # 단위 행렬
print(np.identity(5, dtype=np.int32))       # 단위 행렬