# Day_18_01_NumpyBasic.py
import numpy as np

# print([1, 2, 3])           # 리스트를 numpy로 변환
# print(np.array([1, 2, 3]))

# 문제
# 넘파이 배열을 리스트로 변환하세요

# print(list(np.arange(0, 5)))
# print(np.array([1, 2, 3]).tolist())

# 문제
# 리스트를 사용해서 2행 3열의 넘파이 배열을 만드세요 (3가지)
# (코드에 리스트가 포함되기만 하면 인정)

# a = [1, 2, 3]
# a_2 = [4, 5, 6]

# b_3 = []
# b_3.append(a)
# b_3.append(a_2)
# print(np.array(b_3))

# b = np.array(a)
# print(b.reshape(2, 3))
# print(b.reshape(2, -1))
# print(b.reshape(-1, 3))

# b_2 = np.array([[1, 2, 3],[4, 5, 6]])

# print(np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3))
# print(np.asarray([[1, 2, 3], [4, 5, 6]]))
# print(np.int32([[1, 2, 3],[4, 5, 6]]))        # 추천

# print(np.array([range(3), range(3, 6)]))
# print(np.array([np.arange(3), np.arange(3, 6)]))

# print(np.array([range(6)]).reshape((2, 3)))

# print(np.zeros([2, 3]))     # 0을 초기값으로 주는 함수
# print(np.zeros((2, 3)))     # 뭘 하든 같다.
# print(np.ones([2, 3]))      # float 타입
# print(np.ones([2, 3]).dtype)        # float64
# print(np.ones([2, 3], dtype=np.int32).dtype)

# 문제
# -1로 채워진 2행 3형의
# print(np.full([2, 3], -1))

a = [[1, 2, 3], [4, 5, 6]]
# print(a)
# print(np.zeros_like(a))     # 객체를 전달
# print(np.ones_like(a))
# print(np.full_like(a, -1))

# 문제
# a와 동일한 모양의 배열을 zeros 함수로 만드세요 (zeros_like 사용 금지)
# b = np.array(a)
# print(np.zeros(np.array(a).shape))
# print(np.zeros(np.shape(a)))

print(np.arange(0, 10, 1))
print(np.arange(0, 10, 0.7))    # range 함수는 불가능

# 문제
# 0~1 사이의 구간을 10개로 나누세요

print(np.arange(0, 1.1, 0.1))
print(np.linspace(0, 1, 11))        # 1을 포함한다. (시작, 종료, n개로 분할)

print('-' * 30)

b = np.arange(10)
print(b)

# for i in range(len(b)) :
#     b[i] += 7

# broadcast 연산
# 장점 : 입력 감소, 가독성 향상, 성능 향상, 어려운 코드 대신 코딩
print(b + 7)
print(b * 7)
print(b ** 2)
print(b > 3)
print(np.logical_and(b > 2, b < 5))
print()

c = b.reshape(2, 5)
print(c)

print(c + 7)
print(c * 7)
print(c ** 2)
print(c > 3)
print(np.logical_and(c > 2, c < 5))
print('-' * 30)

# vector 연
print(b + b)
print(b*b)
print(b ** b)
print()

print(c + c)
print(c * c)
print(c ** c)
print()

# print(b + [1, 2, 3])      # 에러
# print(b + np.array([1, 2, 3]))      # 에러 ( 배열의 크기가 다르면 호환이 되지 않는다. )
print(b + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])   # 성공 ( 리스트랑 넌파이 호환 가능 개수만 중요 )
print(b + range(10))    # 성공
print('-' * 30)

# universal function 똑같은 모양을 리턴
print(np.sin(b))

