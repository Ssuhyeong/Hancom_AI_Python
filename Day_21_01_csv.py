# Day_21_01_csv.py
import csv          # comma(,) Separated Values
import sqlite3

# 구분자: separtor, delimeiter

# 문제
# 복습 :
def read_weather():
    # f = open('data/weather.txt', 'r', encoding='utf-8')
    f = open('data/weather.txt', 'r', encoding='utf-8', newline='')     # windows에서 빈 줄 발생하는 버그 문제해결

    # rows = []
    # for line in f:
    #     row = line.strip().split(',')
    #     rows.append(row)
    # print(rows)

    for row in csv.reader(f):
        print(row)
    f.close()

def read_us500():
    f = open('data/us-500.csv', 'r', encoding='utf-8')

    # for row in csv.reader(f):
    for row in csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL):        # 구분자가 쉼표가 아닌 경우 delimiter 사용
        assert len(row) == 12
        print(row)


    f.close()

# weather.txt 파일을 읽어서 각각의 컬럼에 큰 따옴표를 추가하고 구분자는 세미콜론으로 변환해서
# weather.csv 파일로 만드세요

def write_weather():
    # f1 = open('data/weather.txt', 'r', encoding='utf-8')
    # f2 = open('data/weather.csv', 'w', encoding='utf-8')
    #
    # writer = csv.writer(f2, delimiter=',', quoting=csv.QUOTE_ALL)
    #
    # for row in csv.reader(f1):
    #     # print(row)
    #     # csv.writer(f2, delimiter=',', quoting=csv.QUOTE_ALL).writerow(row)
    #     writer.writerow(row)
    #
    # f1.close()
    # f2.close()


    # 두 번째 방법
    f1 = open('data/weather.txt', 'r', encoding='utf-8')

    # 1번
    # rows = []
    # for row in csv.reader(f1):
    #     rows.append(row)

    # 2번
    rows = [row for row in csv.reader(f1)]

    # 3번
    rows = list(csv.reader(f1))

    f1.close()

    f2 = open('data/weather.csv', 'w', encoding='utf-8')
    csv.writer(f2, delimiter=';', quoting=csv.QUOTE_ALL).writerows(rows)

    f2.close()

read_weather()
# read_us500()
# write_weather()