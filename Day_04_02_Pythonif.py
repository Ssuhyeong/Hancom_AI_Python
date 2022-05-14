#Day_04_02_Pythonif.py

# 홀짝

a = 31

if 1 == a%2 :     #파이썬은 콜론(:)나오면 무조건 들여쓰기가 나와야한다.
    print('홀수')
else :
    print('짝수')

if a % 2 : # 동작 가능
    print('홀수')
else :
    print('짝수')

print(type('hello'))
print(type(123))
print()

b = int(input('정수를 입력하세요 : '))
print(b)

# 문제
# if만 사용해서 입력한 정수가 음수인지 양수인지 0인지 알려주세

# cmd + 슬래쉬 영역 주석
# shift + Tap : 내어 쓰기

if b > 0 :
    print('양수')
else :
    if b == 0 :
        print('0')
    else :
        print('수')

# elif 적용

if b > 0 :
    print('양수')
elif b == 0 :
    print('0')
else :
    print('수')
