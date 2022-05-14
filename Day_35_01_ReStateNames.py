# Day_35_01_ReStateNames.py
import requests
import re
import pandas as pd
import csv

# 문제
# 아래 사이트에서 미국 주의 이름 데이터를 파싱해서 data 폴더 states.csv 파일로 저장하세에요

# 내가 한거 : 미국 주의 이름만 추
# url = 'https://developers.google.com/public-data/docs/canonical/states_csv'
# received = requests.get(url)
# text = received.text
#
# states = re.findall(r'<td>([A-Z][a-z].+?)</td>', text, re.DOTALL)
# print(len(states))
# rows = [row for row in csv.reader(states)]
# # print(rows)
# f = open('data/states.csv', 'w')
# csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL).writerows(rows)
#
# f.close()

def get_states_1():
    # 구글링으로 states.csv 검색 후, 첫 번째 항목 선택
    url = 'https://developers.google.com/public-data/docs/canonical/states_csv'
    received = requests.get(url)
    text = received.text

    table = re.findall(r'<table>(.+?)</table>', text, re.DOTALL)
    # print(table[0])
    # print(len(table))

    table_rows = re.findall(r'<tr>(.+?)</tr>', table[0], re.DOTALL)
    # print(*table_rows, sep='\n')
    # print(len(table_rows))

    states = []
    header = re.findall(r'<th scope="col">(.+?)</th>', table_rows[0])
    # print(header)
    states.append(header)

    for item in table_rows[1:]:
        row = re.findall(r'<td>(.+?)</td>', item)
        # print(row)
        states.append(row)

    return states

def get_states_2():
    url = 'https://developers.google.com/public-data/docs/canonical/states_csv'
    received = requests.get(url)
    text = received.text


    data = re.findall(r'<td>(.+?)</td>', text)
    # print(data[:10])
    # print(len(data))

    states = []
    for i in range(0, len(data), 4):
        states.append([data[i], data[i+1], data[i+2], data[i+3]])
    return states

    return [data[i:i+4] for i in range(0, len(data), 4)]


# print(*get_states_1())
# states = get_states_2()
# print(*states, sep='\n')출

# 문제
# get_states_1 함수에서 만든 결과를 data 폴더에 states_1.csv 파일로 저장하세요 (2가지 방식)
# (csv 사용하지 않기, csv 사용하기)

# f = open('data/states_1.csv', 'w')
# csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL).writerows(get_states_1())
# f.close()

# data = pd.DataFrame(get_states_1())
# data = data.drop(data.index[0])
# data.to_csv('data/states_1.csv', header=False, index=False,  sep=',')

def write_state_1(states):
    f = open('data/state_1.csv', 'w', encoding='utf-8')

    # 1번
    # for row in states:
    #     f.write('{},{},{},{}\n'.format(row[0], row[1], row[2], row[3]))

    # 2번
    # for state, latitude, longitude, name in states:
    #     f.write('{},{},{},{}\n'.format(state, latitude, longitude, name))

    # 3번
    for row in states:
        f.write(','.join(row) + '\n')

    f.close()

def write_state_2(states):
    f = open('data/state_2.csv', 'w', encoding='utf-8')

    # 1번
    # writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    # for row in  states:
    #     writer.writerow(row)

    # 2번
    csv.writer(f).writerows(states)

    f.close()


states = get_states_1()
write_state_1(states)
# write_state_2(states)



# 수 : 정규표현식, 딥러닝(텐서플로)
# 목 : 사이킷런, 딥러닝(텐서플로)
# 금 : 딥러닝(텐서플로)
# 월 : 딥러닝(케라스), 결과물 작업
# 화 : 딥러닝(케라스)

# 시각지능, 언어지능

# 10p 만들어야한다. 프로젝