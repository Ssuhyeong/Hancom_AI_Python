# Day_17_02_NumpyBasic.py
import numpy as np # 배열 라이브러리

# 문제
# arange 함수를 사용하는 코드 두가지를 만드세
print(np.arange(10))           # array range / 슬라이싱과 비슷하다.
print(np.arange(0, 10))
print(np.arange(0, 10, 1))     # [0 1 2 3 4 5 6 7 8 9]

print(list(range(10)))         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('-' * 30)

# 배열 : 같은 공간, 같은 자료형        [1, 5, 2] 가장 빠르게 데이터에 접근 가능 / 사용하기 어렵다.
# 리스트 : 같은 공간, 다른 자료형       [3, 0.5, 'hello'] 성능에서 손해 발생 / 사용하기 쉽다.

a = np.arange(6)
print(a.shape, a.dtype, a.size, a.ndim) # (6,) int64 6 1
# shape : 넌파이 구조를 알려줌 -> 튜플로 알려줌 (튜플인 것을 나타내기 위해 , 도 포함)
# dtype : 넌파이의 타입을 알려줌
# size : 넌파이의 원소 개수
# ndim : 몇 차원인지

print(type(a.shape), type(a[0]))    # <class 'tuple'> <class 'numpy.int64'>

# a.shape = 99          # 속성은 변경 불가
# ndarray : N-dimensional array(다차원 배열)

print(type(a))          # <class 'numpy.ndarray'>

# b = a.reshape(2, 3)     # reshape : 차원을 변경
# b = a.reshape(1, 2)       # 원의 개수가 초과되거나 부족하면 오류
b = a.reshape(-1, 2)        # -1 : 최대

# print(b)
# print(b.shape, b.dtype, b.size, b.ndim)

# print(a.reshape(2, 1, 3))

# 문제
# 앞에서 만든 2차원 배열 변수 b를 1차원으로 변환하세 (3가지 코드 구현)
print(b.reshape(6))
print(b.reshape(-1))
print(b.reshape(b.size))
