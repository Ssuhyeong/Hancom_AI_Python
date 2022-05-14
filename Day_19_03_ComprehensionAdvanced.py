# Day_19_03_ComprehensionAdvanced.py
import numpy as np

# for i in range(2) :
    # for j in range(3) :
        # print(i, j)
# exit()         # 여기까지 프로그램 실행하고 끝
# print([(i, j) for i in range(2) for j in range(3)])

# 문제
# 2차원 리스트를 1차원 리스트로 변환하세요

a = [[1, 2],
     [3, 4, 5],
     [6, 7, 8, 9]]

# b = []
# for i in a :
#     # print(i)
#     for j in i :
#         b.append(j)
# print(b)

# print([j for i in a for j in i])

# 문제
# 2차원 리스트의 합계를 구하세요 (2가지 방법)
# print(sum([j for i in a for j in i]))
# print(sum([sum(i) for i in a]))

# 문제
# 2차원 리스트의 홀수 합계를 구하세요 (2가지)

# for i in a :
#      for j in i:
#           if j%2 ==1 :
#                print(j)

# print(sum([j for i in a for j in i if j%2]))

# print([sum([j for j in i]) for i in a])                #[3, 12, 30]
# print(sum([sum([j for j in i if j%2]) for i in a]))    # 25