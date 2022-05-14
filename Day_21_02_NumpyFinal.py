# Day_21_02_NumpyFinal.py
import numpy as np

a = np.arange(12).reshape(3, 4)
# print(a)

# 문제
# 2차원 배열에서 첫 번째와 마지막 번째 요소(int)를 출력하세요

# print(a[0][0])
# print(a[-1][-1])

print(a[0, 0])
print(a[-1, -1])        # fancy indexing <중요>
print('-' * 30)

# 문제
# 첫 번째 행을 출력하세요
# 첫 번쨰 열을 출력하세요

print(a[0])
print(a[:,0])
print(a[0, :])