# Day_20_01_PythonClass.py

# 프로그램 구성 요소 : 함수, 변수
# 클래스 : 함수 + 변수


class Fake:
    pass

class Info:
    dummy = 'dummy'             # 클래스 변수

    def __init__(self):
        print('Info')
        local = 'local'         # 지역 변수 -> 함수를 벗어나면 사용할 수 없음

        self.age = 25           # 맴버 변수
        # self.name = 25
        # self.addr = 25
        # self.city = 25

    def show_age(self):
        print('show_age :', self.age)



f = Fake()          # 생성자(constructor)
a = Info()          # Info.__init__()
b = Info()
c = Info()

# print(a)
# print(b)
print('-'* 30)

# print(Info.dummy)
# Info.dummy = 123

# print(a.dummy)          # 오해가 있는 코드
# print(b.dummy)          # 사용하지 않았으면 하는 코드
# print(c.dummy)

# print(a.local)          # 에러, 지역 변수는 해당 함수 안쪽에서만 사용

# a.age = 99
# print(a.age)
# print(b.age)
# print(c.age)

# a.hobby = 'walking'      # class를 동적으로 할당할 수 있다.(사용 권장하지 않음)
# print(a.hobby)
# print(b.hobby)         # 에러

# 문제
# show_age 함수를 호출하세요 (3가지)

print(a.show_age())
print(Info.show_age(a))
# print(Info.show_age(123))     # 123은 Info 객체가 아니라서
