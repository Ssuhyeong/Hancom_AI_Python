# Day_13_01_PythonDict.py
import random

a = [2, 1, 3] * 5

# 문제
# 1차원 리스트에서 중복된 요소를 삭제하세요 ( 중복되지 않는 리스트 생성 )

# b = []
# for i in a :
#     if i not in b :         # true나 false를 i가 b에 들어 있지 않으
#         b.append(i)
# b.sort() # 정렬
# print(b)

# 변환 : int, float, str, bool, list, tuple, set, dict

# 순서 : list, tuple (순서를 보장) (리스트는 원소 검색 시 첫 원소부터 하나씩 찾음)
# 검색 : set, dict (검색을 하기 위해서) (더 효율적으로 검색한다.) (특정 순서를 정할 수 없음)

# c = set(a)      # {1, 2, 3}
# # c[0]          # error dict은 이런식 불가
#
# c = list(c)     # 이런 후처리 사용
# print(c)
#
# c2 = {}
# print(type(c2))     # <class 'dict'>
#
# c3 = set()
# print(type(c3))     # <class 'set'>
#
# for _ in range(100) :
#     # c3.append(7)    # dict, set 은 사용할 수 없다.
#     c3.add(random.randrange(10))
# print(c3) # 앞에 있는 데이터에서 똑같은 데이터는 덮어씀, 즉, 중복을 허용하지 않음

# 딕셔너리(map) : key를 이용해서 value를 검색하는 자료구조
# 영한 사전 : 영어 단어(key)를 이용해서 한글 설명(value)을 찾는 책

d = {}

d['age'] = 25
d['addr'] = '경기도'          # key 추가 (존재하지 X)

print(d)

e = {'age' : 25, 'addr' : '경기도'}

e['addr'] = '군산'        # value 갱신 (존재 시)
e['habby'] = '영화'

print(e)
print('-' * 30)

print(e.keys())     # dict_keys(['age', 'addr', 'habby']) / 리스트를 내부적으로 담고있다. 인덱스로 불러오는 건 안
print(e.values())   # dict_values([25, '군산', '영화'])
print(e.items())    # dict_items([('age', 25), ('addr', '군산'), ('habby', '영화')])

# print(e.keys()[0]) # error

for k in e.keys() :
    print(k, e[k])
print()
#
# for k in e :
#     print(k, e[k])
#
# for i in e.items() :
#     print(i)
#     print(i[0], i[1])

# for k, v in e.items() :         # 효율적인 items 사용
#     # print(k, v)
# print()
#
# for ikv in enumerate(e.items()) :     # enumerate 앞에 인덱스를 출력해준다.
#     # print(ikv)
#     # print(ikv[0], ikv[1]) # 0 ('age', 25) 이런식으로 인덱스, 튜플
#     print(ikv[0], ikv[1][0], ikv[1][1]) # 0 age 25
# print()

# 문제
# 아래 코드를 파이썬 다운 코드로 수정하세요.

for i, (k, v) in enumerate(e.items()) :
    print(i, k, v)

