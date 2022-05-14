# Day_04_01_PythonOperator.py
# 변수 -> 연산자 -> 제어문 -> 반복문 -> 컬렉션(리스트, 딕셔너리) -> 함수

# 연산 : 산술(+,-), 관계(<, >), 논리(AND, OR)

# 산술 : + - * // % ** /

a, b = 7, 3

# 개행을 띄고 복사하면 자동으로 띄어져서 복사 가능

print(a + b)
print(a - b)
print(a * b)
print(a // b) # 나눗셈 (정수)
print(a % b) # 나머지
print(a ** b) # 지수
print(a / b) # 나눗셈 (실수)

# 문제
# 변수 c를 만올림해서 정수로 만드세요

c = 3.12
d = c - c//1
e = (d*2)//1
print(c//1+e)

# 가장 간편한 코드
print((c + 0.5) // 1) # 이 경우는 함수 하
print(int(c+0.5)) # str, float, bool 함수 이름과 짝지은 괄호 하나당 함수다 이 경우는 함수가 2개

# int('hello') # 에러
# int('123') # 이 경우만 가

# 관계연산자 : > >= < <= !=

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

print(int(a!=b)) # 부울식을 숫자로 표현할 수 있다.

# 참 : 1(대표 참), True , 0이 아닌 모든 숫
# 거짓 : 0 , False

# 논리연산자 : and or not

# and 연산
# T and T = T
# T and F = F
# F and T = F
# F and F = F

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or 연산
# T or T = T
# T or F = T
# F or T = T
# F or F = F

print(True or True)
print(True or False)
print(False or True)
print(False or False)

