# Day_13_03_PythonLambda.py

# 람다 : 반환값을 갖는 한 줄짜리 함수

def twice(n) :
    return n * 2

def proxy(f, n) :
    return f(n)


l = lambda n : n * 2     # 매개변수 : 조건식 // return은 생략된다.
# l = lambda n, k : n * k 가능
f = twice             # 함수 포인


# print(twice(3))
# print(twice)
# print(f)
# print(f(3))
#
# print(l)
# print(l(2))
# print((lambda n : n * 2)(3))        # 함수를 만들면서 호출까지

# 장점 : 프로그램의 성능이 좋아진다. 보통 함수는 사용하기 위해서 그 주소로 가야한다. 함수 호출 비용이 발생
# 람다는 갈 필요없이 바로 실행가능 -> 성능이 좋아진다.
# 최적화하기 좋다.

# 단점 : 여러번 사용하면 메모리를 많이 사용한다.

print(proxy(twice, 7))
print(proxy(l, 7))
print(proxy(lambda n : n * 2, 7))
print('-' * 30)

a = [39, 72, 46, 58]

print(sorted(a))

# 문제
# 마지막 자리로 정렬하세요
print(sorted(a, key=lambda n : n % 10)) # key를 어떻게 정할지를 보낸다 함수로

b = ['RED', 'YELLOW', 'blue', 'Green']
print(sorted(b))

# 문제열 리스트를 길이에 맞게 정렬 (내림차순)
print(sorted(b, key = lambda s : -len(s)))
print(sorted(b, key = lambda s: len(s), reverse =True)) # reverse 역순으로 할래?

print(sorted(b, key=lambda s: s.lower()))