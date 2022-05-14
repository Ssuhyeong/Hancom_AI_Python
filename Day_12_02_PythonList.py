# Day_12_02_PythonList.py
import random

a = [[0, 1],
     [2, 3, 4],
     [5, 6, 7, 8, 9]]           # 3개의 요소를 가지고 있다.

print(a)
print(a[0], a[1], a[2])     # 1차원
print(a[0][0], a[1][0], a[2][0]) # 각 요소들의 요소를 출력

print('-' * 40)

# 문제
# 2차원 리스트에 들어있는 데이터의 갯수를 구하세요

# s = 0         # sum은 이미 있는 함수이기 떄문에 사용하면 좋지 않다.
# for i in range(len(a)) :
#     s += len(a[i])
# print(s)
#
# cnt = 0      # 이 경우가 깔끔
# for i in a:
#     cnt += len(i)
# print(cnt)
#
# s = 0           # 이 코드는 좋지 않다 ( 반복문을 2번 사용하고 복잡 )
# for i in a :
#     for _ in i :
#         s += 1
# print(s)

# print(random.randrange(0, 100, 1)) # range함수를 사용하는 것과 비슷 // 시작, 종료, 간격
# print(random.randrange(0, 100))
# print(random.randrange(1, 100, 2) - 1)

# 문제
# 앞에서 만든 2차원 리스트의 값을 100보다 작은 홀수 난수로 주세요

# for i in range(len(a)) :
#     for j in range(len(a[i])) :
#         a[i][j] = random.randrange(1, 100, 2)
#
# print(a)

# for i in a :            # 동작하는 코드 : 리스트의 값을 변경하기 위해서는 [] 문법을 사용해야한다.
#     i[1] = random.randrange(1, 100, 2)
#
# print(a)

# for row in a :            # 좋은 코
#     for j in range(len(row)) :
#         row[j] = random.randrange(1, 100, 2)
# print(a)
# print('-' * 40)

# 문제
# 2차원 리스트를 1차원 리스트로 변환하세요

# b = []
# for row in a :
#     for col in row :
#         b.append(col) # 추가
# print(b)

# b = []
# for i in a :
#     b += i
# print(b)

# c = [1, 2]
# c.append([5, 7, 9]) # 새로운 요소로 추가되는 것이다. 이렇게 하는 경우 c에 3번에 요소에 1차원 배열이 추
# print(c)

# d = [1, 2]   # 하나의 요소가 되는 것이아니라 확장한다.
# d.extend([5, 7, 9])
# d += [4, 6]  # extend와 동일하다.
# print(d)

