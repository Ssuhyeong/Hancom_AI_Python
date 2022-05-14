# Day_05_02_PythonList.py

#               []              ()           {}             {}
# collection : list(많이 사용), tuple, set(거의 사용X, 무시), dict(많이 사용)

a = [7, 1, 9, 4]
print(a)
print(a[0], a[1], a[2])
print(a[0] + a[1] + a[2])
# print(a[3]) # 에러
print()

for i in range(len(a)) :
    print(i, a[i])
print()

# 동일

for i in a :    # 이 경우가 가장 좋지만 이 리스트의 끝까지 수행한다.
    print(i, end = ' ')
print()

print(a[3], a[len(a) - 1], a[-1]) # 마지막 원소를 출력할 떄 사용하는 것들 마지막이 파이썬에서 가장 많이 사용
