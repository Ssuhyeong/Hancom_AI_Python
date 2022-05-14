# Day_11_02_PythonFuntion.py

# 프로그램 : 코드(함수), 데이터(변수)

# 교수 => 데이터 => 학생 : 매개 변수
# 교수 <= 데이터 <= 학생 : 반환

# 매개 변수 없고 , 반환값 없고.
def f_1():
    print('f_1')

f_1() #함수 호출

# 매개 변수 있고, 반환값 없고.
def f_2(a, b):
    print('f_2', a*b)

# 문제
# f_2를 호출하는 두 가지 코드는 무엇일까요?

f_2(123, 5)
f_2('123', 5)

# 매개 변수 없고, 반환값 있고.
def f_3():
    print('f_3')

c = f_3()
print(c)

def f_4():
    a, b = 3, 5
    print('f_4', a*b)

    return a * b
d = f_4()

print(d)
print(f_4()) # 둘다 효율이 좋다.

# 매개 변수 있고, 반환값 있고.
# 문제
# 2개의 정수 중에서 큰 숫자를 찾느 함수를 만드세요

def max_2(a, b):
    # if a>b :
    #     return a
    # else :
    #     return b

    # if a>b:
    #     return a
    # return b

    if a > b:
        b = a
    return b

    # return 'same' 이런식으로 하면 코드가 죽어버린다.

print(max_2(3, 7))
print(max_2(7, 3))
print()

# 문제
# 4개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요

def max_4(a, b, c, d):          # 시간이 좀 걸리더라도 명확하게 비교하는 것이 좋다.

    # 확장성이 떨어짐 알고리즘은 좋은데 비교가 많아지면 문제가 생김
    # if a >= b and a >= c and a >= d :   return a
    # if b >= a and b >= c and b >= d :   return b
    # if c >= a and c >= b and c >= d :   return c
    #
    # return d

    # 매우 좋은 코드 (정답이라고 해도 무방하다)
    # if a < b : a = b
    # if a < c : a = c
    # if a < d : a = d
    #
    # return a

    # 복면가왕
    # return max_2(max_2(a, b), max_2(c, d)) # 베스트 (정답) / 재사용성이 좋다 즉, 안전하다.

    # 한국시리즈
    return max_2(max_2(max_2(a, b), c), d)

print(max_4(2,4,6,8))
print(max_4(4,6,8,2))
print(max_4(6,8,2,4))
print(max_4(8,2,4,6))