# Day_33_02_ReMenu.py
import re
import requests

# 문제
# 전북대학교 식당 중에 진수원의 1주일치 점심과 저녁 메뉴를 파싱하세요

# 내가 한
url = 'http://sobi.chonbuk.ac.kr/chonbuk/m040101'
received = requests.get(url)
text = received.content.decode('utf-8')

# menu = re.findall(r'<p style="line-height: 1.2;">(.+?)</p>', text)
# menu = str(menu).replace('<br />', ', ')
# menu = menu.replace('&amp;', '&')
# menu = menu.replace("'중식 ', '백반', ", '')
# menu = menu.replace(" '석식 ', '백반'", '')
# menu = menu.replace('[', '')
# menu = menu.replace(']', '')
# menu = menu.replace("'", '')
# menu = menu.replace(',', '')
# menu = menu.split(' ')
# print(len(menu))

# 1번
url = 'http://sobi.chonbuk.ac.kr/chonbuk/m040101'
received = requests.get(url)
text = received.content.decode('utf-8')
# print(text)

tables = re.findall(r'<table.+?</table>', text, re.DOTALL)

# print(tables[0])
# print(len(tables))            # 4

results = re.findall(r'<p style="line-height: 1.2;">(.+?)</p>', tables[0])
# print(*results, sep='\n')
# print(len(results))

print('점심')
for row in results[2:7]:
    # print(row.split('<br />'))
    # for item in row.split('<br />'):
    #     print(item.replace('&amp;', '&'))
    print([item.replace('&amp;', '&') for item in row.split('<br />')])

print('저녁')
for row in results[9:]:
    print([item.replace('&amp;', '&') for item in row.split('<br />')])
print('-' * 30)

# 2번
tables = re.findall(r'<table.+?</table>', text, re.DOTALL)
menu_text = tables[0].replace('&amp;', '&')
results = re.findall(r'<p style="line-height: 1.2;">(.+?)</p>', menu_text)

print('점심')
for row in results[2:7]:
    print(row.split('<br />'))

print('저녁')
for row in results[7:]:
    print(row.split('<br />'))

print('-' * 30)

# 3번 - 나머지 코드는 2번과 동일
# results = re.findall(r'<p style="line-height: 1.2;">(.+?)</p>', text)
# print(len(results))
# print(*results, sep='\n')

# 4번 - 중식, 석식, 백반에 대한 특별 처리
results = re.findall(r'<p style="line-height: 1.2;">(....+?)</p>', text)
# print(len(results))
print(*results, sep='\n')
for row in results:
    print(row.split('<br />'))
print('-' * 30)

# 5번
# results = re.findall(r'<td bgcolor="#ffffff" class="">.*?<p style="line-height: 1.2;">(.+?)</p>', text, re.DOTALL)
# print(len(results))
# print(*results, sep='\n')
# for row in results:
#     print(row.split('<br />'))