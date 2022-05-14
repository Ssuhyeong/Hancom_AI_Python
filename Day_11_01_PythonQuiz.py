# Day_11_01_PythonQuiz.py

# 문제
# 100보다 작은 짝수의 합계를 구하세요
# sum = 0
# for i in range(0, 100, 2) :
#     sum += i
# print(sum)

# 문제
# 아래 모양 처럼 출력하세요 (3가지)

# for _ in range(5) :       # _: place holder
#     print('* * * * *')
#
# for i in range(5):
#     for j in range(10):
#         if j%2 == 1:
#             print("*",end =" ")
#     print()
#
# for i in range(5) :
#     print("* " * 5)
#
# for i in range(30):
#     if i%6 != 0 :
#         print("*", end = ' ')
#     else :
#         print()
#
# print('* * * * *' * 5)

def draw_star():          # 함수 선언 후 들여쓰기 2번 이상을 해야한다.
    for _ in range(5):
        print('* ', end='')
    print()


for _ in range(5):
    draw_star()

print('-' * 30)

# 문제
# 아래와 같은 형태로 출력하세요

# *
# **
# ***
# ****

for i in range(5):
    print("*"*i)
print()
for i in range(4,0,-1):
    print("*"*i)
print()
for i in range(5):
    print(" "*(4-i), "*"*i)
print()
for i in range(5):
    print(" "*i, "*"*(4-i))
print()

for i in range(4-1, -1, -1):
    print(' ' * (4-1-i) + '*'*(i+1))

print('-'*30)

# 0123

for i in range(4):
    for j in range(4):
        if i == j:
            print('*', end='')
        else:
            print('-', end='')
    print()

for i in range(4):
    for j in range(4):
        print('*' if i >= j else '-', end = ' ')
    print()

print()

# for i in range(4-1, -1, -1): # 같은 코
for i in reversed(range(4)):
    for j in range(4):
        print('*' if i >= j else '-', end = ' ')
    print()

for i in range(4):
    for j in reversed(range(4)):
        print('*' if i >= j else '-', end = ' ')
    print()

for i in reversed(range(4)):
    for j in reversed(range(4)):
        print('*' if i >= j else '-', end = ' ')
    print()

# 공부할 때 코드들은 다 지우고 문제만 남긴다.