# Day_18_03_Comprehension.py요
import random

# comprehension : (함수 매개 변수로 전달함) 컬렉션을 만드는 한 줄짜리 반복문

for i in range(5) :
    i

print([i for i in range(5)])
print(tuple((i for i in range(5))))
print({i for i in range(5)})

# 문제
# 20보다 작은 양수에서 짝수로 구성된 리스트를 만드세요

print([i for i in range(0, 21, 2)])

# 문제
# 0~100 사이의 난수 중에서 10개를 뽑아 리스트로 만드세

# print([random.randint(0, 100) for _ in range(10)])
numbers = [random.randrange(100) for _ in range(10)]
print(numbers)

# 문제
# 앞에서 만든 난수 리스트로부터 홀수만 뽑아서 새로운 리스트를 만드세요

for i in numbers :
    if i % 2:
        print(i)

print([i for i in numbers if i % 2])