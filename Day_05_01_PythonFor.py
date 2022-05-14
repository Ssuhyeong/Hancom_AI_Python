# Day_05_01_PythonFor.py

# print('weekend')
# print('weekend')
# print('weekend')
# print('weekend')
# print('weekend')

# 0~5 까지 1씩 증가
for i in range(0, 5, 1) : # 시작, 종료, 증감
    print('weekend')
print()

for i in range(0, 5, 1) :
    print(i, end =  ' ')
print()

for i in range(0, 5) : # 증감을 생략가능 그러면 자동으로 1씩 증가
    print(i, end =  ' ')
print()

for i in range(5) : # 시작도 생략가능 그러면 자동으로 시작(0)으로 설정
    print(i, end =  ' ')
print()

# 문제
# 1. 100보다 작은 양수에서 짝수만 출력하세요

for i in range(100) :
    if i % 2 == 0 :
        print(i, end = ' ')
# 이 경우는 비효율적

for i in range(2, 10, 2) :
    print(i, end = ' ')
print()

# 2. 5,4,3,2,1 순서로 숫주라르 출력하세요
for i in range(5, 0 , -1) :
    print(i, end = ' ')
print()