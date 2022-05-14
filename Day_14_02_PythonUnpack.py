# Day_14_02_PythonUnpack.py

a = 3, 5                # packing
print(a)

b ,c = a                # unpacking
print(b, c)

def f_7(a1, a2) :
    return a1 + a2, a1 * a2

d = f_7(3, 5)           # packing
print(d)


def f_8(*args) :        # packing, 가변 매개 변수 (튜플)
    # print('f_8', args)
    print('f_8', *args)  # unpacking 튜플을 벗어남

f_8()
f_8(1)
f_8(1, 'hello')
f_8(1, 'hello', 3.14)
print()

print([1, 2, 3])
print(*[1, 2, 3])       # unpacking (force)
print(1, 2, 3)
print('-'* 30)

# 문제
# f_9 함수를 호출하는 3가지 코드를 만드세요
def f_9(**kwargs) :     # keyword 가변 매개 변수
    print('f_9', kwargs)
    f_10(t = kwargs)
    f_10(**kwargs)          #unpacking (force)

def f_10(**kwargs) :
    print('f_10', kwargs)

f_9()
f_9(a=1)
f_9(a=1, b='hello')
