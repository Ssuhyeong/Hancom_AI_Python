# Day_30_02_PandasMovie.py
import Day_29_01_PandasMovie
import pandas as pd
import numpy as np

# 영화별 평점 계산
# 여성들이 좋아하는 영화 top10

df = Day_29_01_PandasMovie.read_movie_lens()
# print(df)

# 문제
# 영화에 대해 성별 평점을 구하세요

by_gender =  df.pivot_table(values='Rating', index='Title', columns='Gender')
# print(by_gender)

# 문제
# 영화 평점 갯수가 500번 이상 나온 영화 제목을 구하세요
# for t in by_gender.index.values[:10]:
#     print(t, np.sum([df.Title == t]))

freq = df.groupby('Title').size()
# print(freq)

index500 = freq[freq >= 500]
# print(index500, end='\n\n')

title500 = index500.index.values
# print(title500, end='\n\n')

# 문제
# by_gender로부터 title500에 있는 영화를 추출하세요

rating500 = by_gender.loc[title500]
# print(rating500)



print('-' * 30)

# 문제
# 여성들이 선호하는 영화를 알려주세요

# print(pd.DataFrame.sort_values(rating500, by='F', ascending=False))


# 문제
# 남성들보다 여성들이 선호하는 영화를 알려주세요
# 남성  여성
# 3.5  4.3 -> 더 선호
# 4.3  4.4

# 여성들이 남성보다 좋아하는 영화만 추출(어느 정도 좋은지 생략)
rating500['Diff'] = abs(rating500['F'] - rating500['M'])

# print(pd.DataFrame.sort_values(rating500, by='Diff', ascending=False).index[:9])

# 문제
# 남성과 여성들 모두에 대해 호불호가 갈리지 않는 영화를 알려주세요
# 남성  여성
# 3.5  3.9
# 4.3  4.5
# 3.1  3.0  -> 호불호가 없음

rating500['Dist'] = abs(rating500['F'] - rating500['M'])
# print(pd.DataFrame.sort_values(rating500, by='Dist'))


