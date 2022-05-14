# Day_31_01_seaborn.py

import ssl
import seaborn as sns
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context
# seaborn에서 ssl 오류 발생시 사용

def seaborn_1():
    print(sns.get_dataset_names())

    iris = sns.load_dataset('iris')
    print(iris, end='\n\n')
    print(type(iris))
    print(iris.columns)

    sns.swarmplot(x='species', y='sepal_length', data=iris)
    plt.show()

def seaborn_2():
    titanic = sns.load_dataset('titanic')
    print(titanic.columns)

    sns.factorplot('class', 'survived', 'sex', data=titanic, kind ='bar', legend=False)
    plt.show()

# 문제
# seaborn 홈페이지로부터 마음에 드는 그래프를 골라서 실행해 보세요

def seaborn_3():
    sns.set_theme(style="whitegrid")

    diamonds = sns.load_dataset("diamonds")
    clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

    sns.boxenplot(x="clarity", y="carat",
                  color="b", order=clarity_ranking,
                  scale="linear", data=diamonds)
    plt.show()


# seaborn_1()
# seaborn_2()
seaborn_3()
