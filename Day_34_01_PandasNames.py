# Day_34_01_PandasNames.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors, cm

babies = pd.read_csv('data/yob1880.txt',
                     header=None,
                     names = ['name', 'gender', 'births'])

# 문제
# 남자와 여자에 공통적으로 사용된 이름을 알려주세

# 내가
# females = babies[babies['gender'] == 'F']
# males = babies[babies['gender'] == 'M']

# my_name = [m for w in females['name'] for m in males['name'] if w == m]

# 1번
by_name = babies.groupby('name').size()
# print(by_name, end = '\n\n')
# print(by_name > 1, end='\n\n')
# print('공통 :' ,sum(by_name > 1), end='\n\n')     # 공 : 111통
# print(by_name[by_name > 1], end='\n\n')
# print(by_name[by_name > 1].index, end='\n\n')
# print('-' * 30)

# 2번
# f_name = babies[babies.gender == 'F']['name']
# m_name = babies[babies.gender == 'M']['name']
# print(f_name.isin(m_name), end='\n\n')
# print(sum(f_name.isin(m_name)), end='\n\n')

print()

# 문제
# 공통 이름에 대해 성별 빈도를 보여주세요

# 1번
by_gender = babies.pivot_table(values='births', index='name', columns='gender')
# print(by_gender, '\n\n')

# commons = by_name[by_name > 1].index.values
# print(by_gender.loc[commons].astype(int), end='\n\n')

# 2번
# np.where 함수를 이용해서 공통 이름의 빈도를 알려주세요
# where: 참의 위치(인덱스)를 알려주는 함수
# bools = by_name > 1
# print(np.where(bools))              # 불린 배열 사용

pos = np.where(by_name > 1)
# print(by_gender.iloc[pos].astype(int), end='\n\n')
# print('-' * 30)

# print(by_gender)

# 3번 - notna 함수 사용(groupby 사용 안함)
# f = pd.Series.notna(by_gender.F)
# m = pd.Series.notna(by_gender.M)
# print(pd.concat([f, m], axis=1), end='\n\n')
#
# print(f == m)
# print(by_gender[f == m].astype(int), end='\n\n')
#
# print()

# T T : 찾고자 하는
# T F
# F T
# F F : 존재하지 않음

# 4번 - isna 함수 사용(groupby 사용 안함)
# 문제
# isna 함수를 사용해서 공통 이름을 찾아보세요

# 1번
f = pd.Series.isna(by_gender.F)
m = pd.Series.isna(by_gender.M)
print(pd.concat([f, m], axis=1), end='\n\n')
print(by_gender[f == m].astype(int), end='\n\n')

# 2번
# print(f != m)
# print(not(f != m))  # error
# print(~(f != m))
print(by_gender[~(f != m)].astype(int), end='\n\n')

# 3번
print(by_gender[np.logical_and(f == False, m == False)])
print(by_gender[np.logical_and(~f, ~m)])

# 4번
f_name = babies.name[babies.gender == 'F']
m_name = babies.name[babies.gender == 'M']
print(pd.merge(f_name, m_name))
