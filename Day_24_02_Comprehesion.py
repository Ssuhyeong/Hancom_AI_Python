# Day_24_02_Comprehesion.py
import re
import string

word = 'naver' * 3

# for i, c in enumerate(word) :
#     print(i, c)

# print([(i, c) for i, c in enumerate(word)])       # list
# print({(i, c) for i, c in enumerate(word)})       # set
# print({i:c for i, c in enumerate(word)})          # dictionary
# print({c:i for i, c in enumerate(word)})          # 단어는 사라질 수 있다. 키 값과 value가 크기가 다르면
print()


# 문제
# 1 ~ 10000 사이에 포함된 8의 갯수를 구하세요 ( 구글 입사문제 )

# def count_8(n) :
#     cnt = 0
#     while n > 0:
#         cnt += (n%10 ==8)
#         n //= 10
#     return cnt
# print(sum([count_8(i) for i in range(10001)]))
# print(sum([len(re.findall(r'8', str(i))) for i in range(10000)]))
# print(sum([str(i).count('8') for i in range(10000)]))
# print(str(list(range(10000))).count('8'))
