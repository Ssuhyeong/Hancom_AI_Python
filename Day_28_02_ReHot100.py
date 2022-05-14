# Day_28_02_ReHot100.py

import re
import requests


# 문제
# 빌보드 Hot 100 차트 사이트로부터 등수, 노래 이름, 가수를 파싱해서 출력하세요

url = 'https://www.billboard.com/charts/hot-100'
received = requests.get(url)
text = received.text
# text = received.content.decode('utf-8')

# print(text)
# title = re.findall(r'<span class="chart-element__information__song text--truncate color--primary">(.+)</span>', text)
# rank = re.findall(r'<span class="chart-element__rank__number">([0-9]+)</span>', text)
# singer = re.findall(r'<span class="chart-element__information__artist text--truncate color--secondary">(.+)</span>', text)

# html 엔퍼센트 숫자표현을 다 바꿔주어야 한다.

# for i in range(len(title)) :
#     print(rank[i], title[i], singer[i], sep=":", end='\n\n')

# 1번

items = re.findall(r'<li class="chart-list__element display--flex">(.+?)</li>', text, re.DOTALL)
# print(len(items))       # 100

for item in items:
    rank = re.findall(r'<span class="chart-element__rank__number">(.+?)</span>', item)
    song = re.findall(r'truncate color--primary">(.+?)</span>', item)
    singer = re.findall(r'truncate color--secondary">(.+?)</span>', item)

    rank, song, singer = rank[0], song[0], singer[0]

    # for sp, ch in ([('&amp;', '&'), ('&#039;', "'")]) :
    #     song = song.replace(sp, ch)
    #     singer = singer.replace(sp.ch)

    song = song.replace('&amp;', '&')
    song = song.replace('&#039;', "'")
    singer = singer.replace('&amp;', '&')
    print('{:3} : {} : {}'.format(rank, song, singer))

print('===========================================')


# 2번

songs = re.findall(r'truncate color--primary">(.+?)</span>', text, re.DOTALL)
singers = re.findall(r'truncate color--secondary">(.+?)</span>', text, re.DOTALL)
# print(len(songs), len(singers))       # 100, 100

for rank, (song, singer) in enumerate(zip(songs, singers), 1):
    song = song.replace('&amp;', '&')
    song = song.replace('&#039;', "'")
    singer = singer.replace('&amp;', '&')
    print('{:>3} : {:25} : {}'.format(rank, song, singer))
