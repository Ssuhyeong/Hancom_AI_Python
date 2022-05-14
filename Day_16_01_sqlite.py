# Day_16_01_sqlite3.py
import sqlite3
import time

# 데이터베이스 : 오라클, MS-SQL , 마리아, MongoDB, sqlite3\
# sqlite3 : 파일 기반

# CRUD : Create, Read, Updata, Delete
# 기상청 데이터로 만든 weather.txt 파일을 읽어서 반환하는 하수를 만드세요

# 문제
# 기상청 데이터로 만든 weather.txt 파일을 읽어서 반환하는 함수를 만드세요
# 테이블 형식의 반환값 작성
# 함수 안에서 출력 금지
new_list = []
def read_weather() :
    f = open('data/weather.txt', 'r', encoding='utf-8')

    rows = []
    for line in f :
        row = line.strip().split(',')
        rows.append(row)
    f.close()
    return rows

def create_db() :
    conn = sqlite3.connect('data/weather.sqlite3')
    cur = conn.cursor()     # 마우스 커서 / db의 위치를 알 수 있게 되었다.

    query = 'CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)'
    # 위에 대문자로 쓰이는 것은 sqlite3에서 제공되는 것, 우리가 명시하는 건 소문자
    # BLOB 대용량 데이터 / DATE, DATETIME 언제 파일을 찾을 수 있다.
    # INTEGER type, VARCHAR 문자.

    cur.execute(query)

    conn.commit() # 읽기만 한다면 사용할 필요 없다.
    conn.close() # 닫아줘야한다.

def insert_row(rows) :
    conn = sqlite3.connect('data/weather.sqlite3')
    cur = conn.cursor()

    base = 'INSERT INTO kma (prov, city, mode, tmEf, wf, tmn, tmx, rnSt) '\
           'VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")' # 여기 value에서 숫자는 그냥 문자는 큰 따옴
    # query = base.format(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])
    query = base.format(*rows)          # unpacking (force)

    cur.execute(query)

    conn.commit()
    conn.close()

def insert_all(rows) :
    conn = sqlite3.connect('data/weather.sqlite3')
    cur = conn.cursor()

    base = 'INSERT INTO kma (prov, city, mode, tmEf, wf, tmn, tmx, rnSt) '\
           'VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")' # 여기 value에서 숫자는 그냥 문자는 큰 따옴

    for row in rows :
        query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        cur.execute(query)

    conn.commit()
    conn.close()

def fetch_all() :       # db 읽기
    conn = sqlite3.connect('data/weather.sqlite3')
    cur = conn.cursor()

    # rows = []
    query = 'SELECT * FROM kma'     # * : all / 좋은 코드는 아니다.
    # for row in cur.execute(query) : # SELECT city, mode FROM 특정 컬럼만 필요할
    #     rows.append(row)
    rows = list(cur.execute(query))
    conn.close()

    return rows

def search_city(city):
    conn = sqlite3.connect('data/weather.sqlite3')
    cur = conn.cursor()

    # query = 'SELECT * FROM kma WHERE city="추자도"'
    # query = 'SELECT * FROM kma WHERE city="' + city + '"'
    query = 'SELECT * FROM kma WHERE prov="{}"'.format(city)
    rows = list(cur.execute(query))

    # conn.commit()             # 읽기만 하기 때문에 필요없다
    conn.close()

    return rows


# rows = read_weather()
# print(*rows, sep='\n')
# create_db()

# start = time.time()
# for row in rows :       # 소요 시간 :  0.24722504615783691
#     insert_row(row)
# insert_all(rows)          # 소요 시간 : 0.0032241344451904297
# print('소요 시간 : ', time.time() - start)

# pk : Primary Key (현재 테이블에서 중복되지 않는 컬럼)
# fk : Foreign Key (다른 테이블의 pk)

# 문제
# 헤르메스 사이트를 참고해서 fetch_all 함수를 완성하세
# rows = fetch_all()
# print(*rows, sep='\n')

# 문제
# 아래 코드가 동작하도록 함수를 완성하세요

city = input("Enter city : ")

rows = search_city(city)
print(*rows, sep='\n')

# -----------------------------------------------------------------------------------------------