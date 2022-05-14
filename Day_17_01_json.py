# Day_17_01_json.py
import json
import requests
import re

# 원격으로 떨어진 단말기간의 통신 : xml(html), json, yaml
# 프로그래밍언어의 상위 개념을 적용 모든 프로그래밍 언어에서 공통적으로 사용하능

# save : 메모리(단기 기억장치)의 내용을 하드 디스크(영구 기억장치)에 쓰겠다.
# load : 하드 디스크(영구 기억장치)의 내용을 메모리(단기 기억장치)에 쓰겠다.
# loads, dumps -> 문자

t1 = '{ "ip" :  "8.8.8.8" }'    # <class 'dict'>
# print(type(t1))

j1 = json.loads(t1)             # 문자열을 객체로 변환
# print(type(j1))
# print(j1['ip'])

print('-'*30)

t2 = { "ip" :  "8.8.8.8" }      # <class 'dict'>
# print(type(t2))

# 문제
# t2를 json을 사용해서 변환하세요

j2 = json.dumps(t2)         # 객체를 문자열로 변환
# print(type(j2))             # <class 'str'>

date_and_time = '''{ 
   "시간" :  "03:53:25 AM" , 
   "milliseconds_since_epoch" :  1362196405309 , 
   "date" :  "03-02-2013 "
}'''
j3 = json.loads(date_and_time)
# print(j3.keys())
# print(j3.values())
for k, v in j3.items() :
    print(k, v)

print('-' * 30)

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
# received = requests.get(url)
# print(received)
# print(received.text)
# print(received.content)


# text = received.content.decode('utf-8')     # 깨진 글자 디코딩
# print(text)

# 문제
# 기상청 코드 데이터로부터 코드와 값만 뽑아서 깔끔하게 출력하세요 (json)
text = '[{"code":"11","value":"서울특별시"},{"code":"26","value":"부산광역시"},{"code":"27","value":"대구광역시"},{"code":"28","value":"인천광역시"},{"code":"29","value":"광주광역시"},{"code":"30","value":"대전광역시"},{"code":"31","value":"울산광역시"},{"code":"41","value":"경기도"},{"code":"42","value":"강원도"},{"code":"43","value":"충청북도"},{"code":"44","value":"충청남도"},{"code":"45","value":"전라북도"},{"code":"46","value":"전라남도"},{"code":"47","value":"경상북도"},{"code":"48","value":"경상남도"},{"code":"50","value":"제주특별자치도"}]'
# j4 = json.loads(text)
# for i in j4 :
#     for j in i.values() :
#         print(j, end =' ')
#     print()

# data = json.loads(text)
# print(type(text))
# print(data)
# print(type(data), len(data))

# for item in data :
    # print(*item.values())

# for item in data :
#     for k in item :
#         print(item[k], end=' ')
#     print()

# for item in data :
#     print(item['code'], item['value'])

# 문제
# 앞에서 풀었던 문제를 정규 표현식으로 풀어보세요
# print(re.findall(r'Peter.+Alice', db, re.DOTALL)) # 찾고자 하는 것이 여러ㅂ줄에 걸쳐있을 때

# a = re.findall(r'"[^code][^value](.+?)"', text)
# print(*a)

# for i in range(len(a)) :
#     if(i%2 == 1) :
#         print(a[i], end= ' ')
#     if i%4 == 0 :
#         print()

codes = re.findall(r'"code":"(.+?)"', text)
# areas = re.findall(r'"value":"(.+?)"', text)      # 이런식이 더 좋은 코드
areas = re.findall(r'[가-힣]+', text)

# print(codes)
# print(areas)

# for i in range(len(codes)) :
#     print(codes[i], areas[i])
#
# print('-' * 30)
#
# print(zip(codes, areas))
# print(list(zip(codes, areas)))
# for code, area in zip(codes, areas) :
#     print(code, area)

codes_and_values = re.findall(r'{"code":"(.+?)","value":"(.+?)"}', text)
print(codes_and_values)

for code, value in codes_and_values :
    print(code, value)