# Day_14_01_PythonFile.py

# data

# poem.txt

def read_1():
    f = open('data/poem.txt', 'r', encoding='utf-8') # 윈도우는 \사용가능 \\도 가능
    # utf-8, euc-kr 어떤 언어로 해석할 지 ASKII같이

    lines = f.readlines() # 바이너리 파일은 동영상, 이미지 등을 사용
    print(lines)

    for line in lines :
        # print(line, end = '') # 메모장 안에도 개행문자가 있고 print에도 있기 때문에 이렇게 사용
        line = line.strip()
        print(line)
    f.close() # 만약 close를 쓰는 습관을 길러라

def read_2():
    f = open('data/poem.txt', 'r', encoding='utf-8')

    while True :            # 무한루프
        line = f.readline()

        # 참 : 0 제외한 모든 문자
        # 거짓 : 0, 0.0, False, None it, '', [], {}, ()

        #if len(line) == 0 :
        if not line :
            break

        print(line.strip())


    f.close()

def read_3():
    f = open('data/poem.txt', 'r', encoding='utf-8')

    for line in f :
        print(line.strip())

    f.close()

def read_4():
    with open('data/poem.txt', 'r', encoding='utf-8') as f :     # as로 별명을 만듬
        for line in f :
            print(line.strip())
        # f.close()         이렇게 사용하면 close를 사용하지 않아도 된다.


def write() :
    f = open('data/sample.txt', 'w', encoding='utf=8')

    f.write('hello')
    f.write('\n')
    f.write('python')

    f.close()

# 문제
# 파일 복사를 수행하는 copy_file 함수를 완성하세
# src : source
# dst : destination
def copy_file(src, dst) :       # 파일 복사
    f_1 = open(src, 'r', encoding='utf=8')
    f_2 = open(dst, 'w', encoding='utf=8')
    # for line in f_1 :
    #     f_2.write(line.strip())
    #     f_2.write('\n')

    f_2.write(f_1.read()) # read(숫자) 몇 글자를 읽어올 것인지 공백이면 전체
    # f_2.writelines(f_1.readlines())

    # for line in f_1 :
    #     f_2.write(line)

    f_1.close()
    f_2.close()


# strip : 문자열 양쪽 끝에 있는 공백들 제거 ( 하나가 아닌 양쪽끝에 있는 모든 공백 제거 )
# 공백 : space, tab, enter(new line)

# s = '\n   \t\n\t rainbow   \n\t   \n\t'
# print('[{}]'.format(s)) # 문자열이 사용하는 범위를 알 수 있음
# print('[{}]'.format(s.strip()))

# read_1()
# read_2()
# read_3()
# read_4()
# write()
copy_file('data/poem.txt', 'data/sample.txt')