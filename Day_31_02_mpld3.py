# Day_31_02_mpld3.py
import mpld3
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def mpld3_1():
    def sample_plot(df, title) :
        df.plot(kind='line',
                marker='p',
                color=['blue', 'red'],
                lw=3,
                ms=20,
                alpha=0.7)

        plt.title(title)
        plt.text(s='blue line', x=1.7, y=2.5, color='blue')
        plt.text(s='red line', x=2.6, y=1.1, color='red')

    c1 = [1, 3, 2, 4]
    c2 = [3, 4, 1, 2]

    df = pd.DataFrame({'c1':c1, 'c2':c2})

    # sample_plot(df, 'base')

    plt.xkcd()
    sample_plot(df, 'xkcd')     # xkcd 손글씨 같은 모양을 보여줌

    # plt.show()
    mpld3.show()


# 문제
# seaborn 홈페이지로부터 마음에 드는 그래프르 골라서 실행해 보세요 (mpld3)

def mpld3_2():
    sns.set_theme(style="white")

    # Load the example mpg dataset
    mpg = sns.load_dataset("mpg")

    # Plot miles per gallon against horsepower with other semantics
    sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
                sizes=(40, 400), alpha=.5, palette="muted",
                height=6, data=mpg)
    mpld3.show()


# mpld3_1()
mpld3_2()
