# Day_12_01_PythonFunction.py

# a = (2 , 9) # 튜플은 값을 변경할 수 없다.
# print(a)
# print(a[0], a[1])
#
# # a[0] = 99 // 에러
#
# b = 2, 9 # 괄호를 생략하면 튜플로 적용
# print(b)
#
# # c, d = 2, 9 # 다중 치환
# c, d = b # 위와 같은 코드
# # c, d, c = b 는 안된다. 논리상으로 맞지 않음
# print(c, d)

def f_5(a, b) :
    return a + b, a * b

e = f_5(3, 5)
print(e)

f, g = f_5(3, 5) # 함수로 다중 리턴이 가smd
print(f, g)
print('-'* 30)

def f_6(a, b, c) :
    print(a, b, c)

f_6(1, 2, 3)                # positional argument : 매개변수 순서에 따라 넣는다.
f_6(a=1, b=2, c=3)          # keyword argument : 매개변수에 직접 값을 넣는다. (순서 바뀌어도 좋다.)
                            # 둘중에 좋은 건 없고 상황에 맞게
f_6(1, 2, c = 3)            # 섞어서 사용가능 이렇게 가장 많이 사용
# f_6(a = 1, 2, c = 3)      # positional은 keyword 앞에 사용해야한다. 앞에 keyword사용하고 뒤에 positional사용 불가

def f_7(a=0, b=0, c=0) :    # default parameter : 매개변수를 전달하지 않으면 알아서 처
    print(a, b, c)

# f_7을 호출하는 방법을 찾아보세요

f_7()
f_7(1)
f_7(1, 2)
f_7(1, 2, 3)

f_7(a=1)
f_7(a=1, c=3)

f_7(1, c=3)

