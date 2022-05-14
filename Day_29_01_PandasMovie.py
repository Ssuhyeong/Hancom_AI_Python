# Day_29_01_PandasMovie.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)      # 보여주는 columns 확장
pd.set_option('display.width', 1000)            # 보여주는 width 확

#      pk(primary key)
# UserID::MovieID::Rating::Timestamp
# UserID::Gender::Age::Occupation::Zip-code
# MovieID::Title::Genres

def read_movie_lens() :
    # 문제
    # users.dat 파일을 읽고 내용을 출력하세
    users = pd.read_csv('ml-1m/users.dat', delimiter='::', engine='python', header=None,
                        names=['UserID','Gender','Age','Occupation','Zip-code'])

    # print(users)

    # 문제
    # moives.dat와 ratings.dat 파일을 읽고 내용을 출력하세요

    movies = pd.read_csv('ml-1m/movies.dat', delimiter='::', engine='python', header=None,
                        names=['MovieID','Title','Genres'])

    ratings = pd.read_csv('ml-1m/ratings.dat', delimiter='::', engine='python', header=None,
                        names=['UserID','MovieID','Rating','Timestamp'])
    # print(movies)
    # print(ratings)

    df = pd.merge(pd.merge(users, ratings), movies)       # pd.merge columns 에서 동일한 것이 있다면 합병 가능
    return df
    # print(df)

# 내 파일에서의 __name__ : __main__
# 다른 파일에서 나의 __name__ : Day_29_01_PandasMovie
# print(__name__)

if __name__ == '__main__':
    df = read_movie_lens()

    # 문제
    # 남녀 성별에 따른 영화 평점을 알고 싶어요

    by_1 = df.pivot_table(values='Rating', columns='Gender')       # 데이터 프레임에서 index, columns, values
    print(type(by_1))
    print(by_1)
    # <class 'pandas.core.frame.DataFrame'>
    # Gender         F         M
    # Rating  3.620366  3.568879

    by_2 = df.pivot_table(values='Rating', index='Gender')
    print(type(by_2))
    print(by_2)

    # 문제
    # pivot_table을 사용하지 말고 남녀 성별 평점 평균을 구하세요 (넘파이 활용)
    males = df[df['Gender'] == 'M'].Rating
    females = df[df['Gender'] == 'F'].Rating
    print("Gender")
    print("F\t    {0:.6f}".format(np.mean(females)))
    print("M\t    {0:.6f}".format(np.mean(males)))

    # 문제
    # 남녀 성별과 연령대에 따른 영화 평점을 알고 싶다.

    by_3 = pd.DataFrame.pivot_table(df, values='Rating', index='Age', columns='Gender')
    by_3 = df.pivot_table(values='Rating', index='Age', columns='Gender')
    print(by_3)

    # 문제
    # 팬더스로 플롯을 그리는데, x축의 이름을 아래 문자열로 바꿔주세요
    ages = ["Under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"]
    # by_3.index = ages

    by_3.plot(kind='bar')
    plt.xticks(range(len(ages)), ages, rotation=45)

    plt.show()


    by_4 = df.pivot_table(values='Rating', index=['Age', 'Gender'])
    print(by_4, end='\n\n')

    # 문제
    # 25, 남자 데이터에 해당하는 3.526780를 읽어오는 코드를 만드세요 (2가지)

    print(by_4.iloc[5].values)
    print(by_4.loc[25].loc['M'].values)
    print('-' * 30)

    print(by_4.unstack(), end='\n\n')       # index를 columns로 이동
    print(by_4.stack())                     # columns를 index로 이동


    # 문제
    # 남녀 성별과 연령대, 직업 따른 영화 평점을 알고 싶어요
    by_5 = df.pivot_table(values=['Rating'], index=['Age','Occupation'], columns=['Gender'])
    print(by_5)


    # 팬더스는 결측치에 대한 처리가 깔끔하지 않다.
    by_6 = df.pivot_table(values=['Rating'], index=['Age','Occupation'], columns=['Gender'], fill_value=(1+5)/2)
    print(by_6)

    by_7 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=[np.mean,np.sum])
    print(by_7)

    by_8_1 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=np.mean)
    by_8_2 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=np.sum)

    print(pd.concat([by_8_1, by_8_2], axis=0), end='\n\n')
    print(pd.concat([by_8_1, by_8_2], axis=1))