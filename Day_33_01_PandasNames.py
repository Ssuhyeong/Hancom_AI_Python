# Day_33_01_PandasNames.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors, cm

# 문제
# 구글에서 미국 신생아 이름 데이터(yob1880.txt)

babies = pd.read_csv('data/yob1880.txt',
                     header=None,
                     names = ['name', 'gender', 'births'])
# print(babies)
#            name gender  births
# 0          Mary      F    7065
# 1          Anna      F    2604
# 2          Emma      F    2003
# ...         ...    ...     ...

# 문제
# 남자와 여자 아기 이름의 갯수를 알려주세요 (2가지)

# females = babies[babies['gender'] == 'F']
# males = babies[babies['gender'] == 'M']

# print(females['name'].count())
# print(males['name'].count())

# print(babies.gender.value_counts())
# print(pd.Series.value_counts(babies.gender))
# print()

# 1번
f_bools = (babies.gender == 'F')
m_bools = (babies.gender == 'M')
# print('w: {}, m: {}'.format(sum(f_bools), sum(m_bools)))
# print('w: {}, m: {}'.format(f_bools.sum(), m_bools.sum()))
print()


# 2번
females = babies[f_bools]
males = babies[m_bools]
# print('w: {}, m: {}'.format(len(females), len(males)))
# print('w: {}, m: {}'.format(females.shape[0], males.shape[0]))
# print('w: {}, m: {}'.format(females.name.count(), males.name.count()))

# 3번
# print(pd.DataFrame.groupby(babies, by='gender').size())
# print(babies.groupby('gender').size())
# print()

# 4번
# print(babies.pivot_table(values='name', index='gender', aggfunc=np.count_nonzero))
# print()

# 5번
# print(''.join(babies.gender).count('F'))
# print(''.join(babies.gender).count('M'))

# 문제
# 남자와 여자 아기 숫자의 합계를 알려주세요 (2가지)

# 내가한거
# females = babies[babies['gender'] == 'F']
# males = babies[babies['gender'] == 'M']
#
# print(females.births.sum())
# print(males.births.sum())
#
# print(babies.groupby('gender').births.sum())

# 1번 (독특한 코드)
# print(sum(babies.births * f_bools), sum(babies.births * m_bools))
# print()

# 2번
# print(babies.groupby('gender').sum())
# print(babies.groupby('gender').sum('births'))
# print(babies.groupby('gender').births.sum())
# print('-' * 30)

# 문제
# 1880년에 부모님들이 가장 좋아한 여자 또는 남자 아이의 이름 top5를 막대 그래프
males = babies[babies['gender'] == 'M']

babies_top5 = pd.DataFrame.sort_values(males, by ='births', ascending=False)[:5]
babies_top5.index = babies_top5.name
del babies_top5['name']

# babies_top5.plot(kind='bar',y='births', title='Male_baby_top5', color=colors.TABLEAU_COLORS)
# babies_top5.plot(kind='bar',y='births', title='Male_baby_top5', color=colors.TABLEAU_COLORS)
# babies_top5.plot(kind='pie', y='births', legend=False, autopct='%2.1f%%', cmap='winter')



# 문제
# matplotlib 모듈의 pie 함수를 사용해서 파이 그래프를 만드세요 (컬러맵 적용)
# (plt.pie에는 cmap 옵션 없음)
# plt.pie(babies_top5.births, labels=babies_top5.index, colors=colors.BASE_COLORS, autopct='%2.1f%%')
# plt.pie(babies_top5.births, labels=babies_top5, autopct='%2.1f%%')

winter = cm.get_cmap('winter')
bar_colors = winter(np.linspace(0, 1, 5))
# plt.bar(range(len(babies_top5)), babies_top5.births, color=bar_colors)
# plt.pie(range(len(babies_top5)), babies_top5.births, colors=bar_colors)


plt.show()