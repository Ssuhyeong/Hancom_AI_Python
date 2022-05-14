# Day_36_01_ReSongs.py
import re
import requests

# 문제
# 지드래곤의 첫 번째 페이지를 파싱해서 반환하 지드래곤의 노래에 대해 제목, 가수, 작사, 작곡, 편곡 데이터를 출력하세요
def fetch_songs(code, page):
    payload = {
        'S_PAGENUMBER': page,
        'S_MB_CD': code,          # 'W0726200'
        # 'S_HNAB_GBN': 'I',
        # 'hanmb_nm': '지드래곤',
        # 'sort_field': 'SORT_PBCTN_DAY',
    }
    url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    received = requests.post(url, data=payload)

    tbodies = re.findall(r'<tbody>(.+?)</tbody>', received.text, re.DOTALL)

    # table_main = tbodies[1].replace(' <img src="/images/common/control.gif" alt="" />', '***')
    # table_main = table_main.replace(' <img src="/images/common/control.gif"  alt="" />', '***')
    # table_main = table_main.replace(' <img src="/images/common/No_control.gif" alt="" />', '***')
    # table_main = table_main.replace(' <img src="/images/common/No_control.gif"  alt="" />', '***')

    table_main = re.sub(' <img.+?/>', '', tbodies[1])
    table_main = re.sub(r'<br/>', ',', table_main)

    table_rows = re.findall(r'<tr>(.+?)</tr>', table_main, re.DOTALL)

    songs = []
    for row in table_rows:
        tds = re.findall(r'<td>(.*?)</td>', row)
        # tds[0] = tds[0].strip()
        tds = [td.strip() for td in tds]
        # print(tds)

        songs.append(tds)
    return songs


# 문제
# 지드래곤의 전체 노래를 가져오세요

def fetch_all(code):
    page = 1
    while True:
        songs = fetch_songs(code, page)

        if not songs:
            break

        print(page, '-' * 80)
        print(*songs, sep='\n')
        page += 1

# fetch_all('W0726200')
fetch_all('W0654100')               # 크롤러, clawling bot

# 윈도우 작업 스케줄 또는 리눅스 크론탭
# 파이썬 실행 파일 python3 Day_36_01_ReSongs.py
# 서버에서 제공하는 robots.txt 파일 규정에 따라 읽어오기

# html: GET, POST
# GET method
# http://www.goole.com/search ? q=한국음악저작권협회
# 보안 취약, 길이 제한, 폼 전송

