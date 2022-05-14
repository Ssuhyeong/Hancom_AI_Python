# Day_18_02_ReLibrary.py
import requests
import json
import re

# 문제
# 수지도서관의 노트북실에 있는 빈 좌석 갯수를 알려주세요
url = 'http://211.251.214.168:8080/seatmate_sj/seatmate.php?classInfo=2'
received = requests.get(url)
text = received.content.decode('euc-kr')

# empty = re.findall(r'좌석번호:([0-9]+)', text)
# empty = re.findall(r'.좌석번호:([0-9]+).', text)

# empty = re.findall(r'<li class=.txt4.>([0-9]+) </li>', text)
# empty = re.findall(r"<li class='txt4'>([0-9]+) </li>", text)
# empty = re.findall(r"<li class='txt4'>(.+) </li>", text)
# print('빈 좌석 갯수 :', int(*empty))

# empty = re.findall(r'color: #003366; ">(.+?)</div>', text)
# print('빈 좌석 갯수 :', len(empty))

# 복습이 필요하다