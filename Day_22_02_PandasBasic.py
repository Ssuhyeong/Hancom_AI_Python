# Day_22_02_PandasBasic.py
import pandas as pd

# DataFrame : 테이블(표), 엑셀 시트  <절대 까먹으면 안된다>
# Series : 데이터프레임에서 컬럼(열)을 담당하는 객체

def series_basic():
    a = pd.Series([5, 1, 2, 9])         # 인덱스와 내가 입력한 값 출력 그리고 마지막으로 데이터타
    print(a, end='\n\n')
    # 0    5
    # 1    1
    # 2    2
    # 3    9
    # dtype: int64

    print(a.index)               # RangeIndex(start=0, stop=4, step=1)
    print(a.values)              # [5 1 2 9]
    print(type(a.values))        # <class 'numpy.ndarray'>

    print('-' * 30)

    b = pd.Series([5, 1, 2, 9], index=['a', 'b', 'c', 'd'])
    print(b, end='\n\n')

    # a    5
    # b    1
    # c    3
    # d    9
    # dtype: int64

    print(b.index)      # Index(['a', 'b', 'c', 'd'], dtype='object')
    print('-' * 30)

    # 문제
    # 앞에서 만든 시리즈에서 두 번쨰 위치한 값(1)을 읽어오세요 (3가지)
    # print(b['b'])
    # print(b.values[1])
    # print(b[1])
    # print(b.b)      # 도트 표기법

    # 문제
    # 앞에서 만든 시리즈에서 두 번째와 세 번쨰 위치한 값(1과 2)들을 읽어오세요 (3가지)
    print(b['b':'c'].values)        # b에서 c까지
    print(b.values[1:-1])
    print(b[1:-1].values)

def dataframe_basic():
    df = pd.DataFrame({
        'city': ['jeju', 'jeju', 'jeju', 'gunsan', 'gunsan', 'gunsan'],
        'year' : [2018, 2019, 2020, 2018, 2019, 2020],
        'population' : [300, 400, 350, 400, 450, 500]
    })

    print(df)
    #      city  year  population
    # 0    jeju  2018         300
    # 1    jeju  2019         400
    # 2    jeju  2020         350
    # 3  gunsan  2018         400
    # 4  gunsan  2019         450
    # 5  gunsan  2020         500

    # print(df.head())        # 앞쪽에 5개
    # print(df.tail())        # 뒤쪽에 5개

    # print(df.head(2), end = '\n\n')       # 앞쪽에 2개
    # print(df.tail(2), end = '\n\n')       # 뒤쪽에 2개
    print('-' * 30)

    df.info()           # 테이블의 정보를 알려준다.
    print('-' * 30)

    print(df.index)     # RangeIndex(start=0, stop=6, step=1)
    print(df.columns)   # Index(['city', 'year', 'population'], dtype='object')
    print(df.values)
    # [['jeju' 2018 300]
    #  ['jeju' 2019 400]
    #  ['jeju' 2020 350]
    #  ['gunsan' 2018 400]
    #  ['gunsan' 2019 450]
    #  ['gunsan' 2020 500]]
    print('-' * 30)

    df.index = ['zero', 'one', 'two', 'three', 'four', 'five']
    print(df)
    #          city  year  population
    # zero     jeju  2018         300
    # one      jeju  2019         400
    # two      jeju  2020         350
    # three  gunsan  2018         400
    # four   gunsan  2019         450
    # five   gunsan  2020         500
    print('-' * 30)

    # 열 데이터에 접근
    # print(df["year"])       # 컬럼만 가능
    print(df["city"])
    # print(df.population)    # 도트 표기법 // 에러가 날 수 있다.
    # print('-' * 30)

    # 행 데이터에 접근
    # print(df.loc["one"])      # 인덱스의 이름을 써준다. 인덱스 행을 출력해준다.
    # print(df.iloc[1])         # 숫자만 써

    # print('-'* 30)

    # 문제
    # one부터 three까지의 행을 출력하세요

    # print(df.loc["one":"three"].values)
    # print(df.iloc[1:4].values)
    # print(df.values[1:4])
    # print('-' * 30)

    # ---------------------------- #

    # print(df.ix['one'])             # 에러
    # print(df.ix[1])                 # 에러

    # print(df['year'])
    # print(df['year':'population'])      # 에러
    # print(df[0])                        # 에러
    # print(df[0:3])                        # iloc 단순 버전
    print(df['year'].values)

# serise_basic()

dataframe_basic()