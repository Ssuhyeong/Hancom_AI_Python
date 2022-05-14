# Day_19_01_NumpyAdvanced.py
import numpy as np
import random

# scalar + scalar : 3 + 7
# vector + scalar : [1, 3] + 5
# vector + vector : [1, 3] + [2, 4]

a = np.arange(3)                        # [0, 1, 2]
b = np.arange(6)                        # [0, 1, 2, 3, 4, 5]
c = np.arange(3).reshape(1, 3)          # [[0, 1, 2]]
d = np.arange(6).reshape(2, 3)          # [[0, 1, 2], [3, 4, 5]]
e = np.arange(3).reshape(3, 1)          # [[0], [1], [2]]

# print(a + b)            # 에러
# print(a + c)            # 1차원 배열이 2차원 배열과 연산을 수행하는 경우 1차원 배열이 2차원 배열로 승격한다.
# print((a + c).shape)    # (1, 3)
# print(a + d)            # broadcast + vector // 1행에 [0, 1, 2] 더하고 2행에도 [0, 1, 2]를 더한다.
# print((a + d).shape)    # (2, 3)
# print(a + e)              # broadcast + broadcast
                          # 각 열을 더해준다 [[0, 1, 2][1, 2, 3][2, 3, 4]]

# 문제
# b와 나머지 변수들 , c와 나머지 변수들, d와 나머지 변수들의 연산을 직접 수행하세요 (6개)
# print(b + c) # 실패
# print(b + d) # 실패
# print(b + e) # 성공             # broadcast + broadcast
# print('-'* 30)
# print(c + d) # 성공             # broadcast + vector
# print(c + e) # 성공             # broadacst + broadcast
# print('-'* 30)
# print(d + e) # 실패
# print('-'* 30)

np.random.seed(1)           # 한마디로 시드를 다르게 사용

# print(np.random.random([2, 3]))         # 0 ~ 1 난수발생
# print(np.random.randn(2,3))             # 표준 정규분포
# print(np.random.uniform(size=[2, 3]))   # 균등 분포
# print(np.random.rand(2, 3))             # uniform 단순 버전
#
# print(np.random.choice([1, 3, 7]))      # 리스트중에서 하나를 랜덤으로 선택
# print(np.random.choice([1, 3, 7], 5))   # 리스트 중에서 5개를 랜덤으로 선택

# 문제
# 100보다 작은 난수 12개로 구성된 배열을 만드세요

a = np.random.choice(range(100), 12)
# a = np.random.randint(0, 100, 12)
# print(a)

# print(a.max())
# print(np.max(a))

# print(a.sum())
# print(np.sum(a))

# 문제
# 1차원 배열 a를 2차원으로 3행 4열로 변환하세요
# print(a.reshape(3, 4))
# print(np.reshape(a, (3, 4)))
# print(np.reshape(a, [3, 4])
# print()

b = a.reshape(3, 4)

print(b.max())
print(b.max(axis=0))        # 열에서 가장 큰 값 찾기
print(b.max(axis=1))        # 행에서 가장 큰 값 찾기
# sum 등등 axis 적용 가능
# print(b.max(axis=2))        # 에러


# 문제
# 1차원 배열 a를 정렬하세요 (2가지)
# print(np.array(sorted(a)))
# print(np.sort(a))                 # 정렬된 배열 반환
# a.sort()
# print(a)                            # 정렬을 해준다. 반환값이 없다.