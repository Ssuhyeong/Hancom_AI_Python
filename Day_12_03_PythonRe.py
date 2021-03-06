# Day_12_03_PythonRe.py
import re       # regular expression(정규 표현식) / 데이터 수집에 관련

# 특정한 규칙을 가진 문자열의 집합 -> 문자열에 대해서만 사용가능 숫자, 그림 등 특별한 데이터는 불가
# 문자열의 검색과 치환을 수행한다.( 텍스트 편집기, 프로그래밍 언어 )
# 정규 표현식을 제공하지 않는 프로그래밍 언어는 없다.
# 문자열을 검색하고 치환하는 건 정규표현식이 최고
# 6가지 문자를 알면 정규 표현식을 충분히 할 수 있다.

# . : 글자 한개라는 의미 1개의 문자와 일치한다 (모든 문자)
# 3글자 : ... => abc '123'

# 대괄호 : [] 안에 들어있는 문자들 중에서 1글자
# 1글자 : [abc] => a, b, c 3글자를 찾아내는
# ex) [abc]d => ad, bd, cd를 뜻한다.
# "-" 기호와 범위 지정 가능 [a-z] a부터 z중의 하나

# 꺽세 대괄호 : [^ ] (부정) : 문자 클래스 안의 문자를 제외한 나머지
# [^abc]d는 ad, bd, cd 는 포함하지 않는 모든 문자

# 양의 지정
# 1) ? : 물음표는 0번 또는 1번차례까지의 발생 있거나 없는것미
# - colou?r -> "color"또는 "colour"을 말한다. 물음표는 문자 앞을 적용

# 2) * : 0번 이상의 발생을 의미한다.
# - ab*c => "ac", "abc", "abbc", "abbbc" 앞에 있는 문자의 0번 이상의 발생

# 3) + : 1번 이상의 발생을 의미한다
# - ab+c => "abc", "abbc" ... 이렇게

# 여기서 하나의 문자가 아닌 유닛을 말한다 즉, ., [], [ ^]도 적용 가능

# regex crossword
# A|Z = A or Z, A|B = A or B 양쪽 모두를 만족시키는 것 A
# [] 대괄호에서 중 한글자, 대괄호에서 한글자 B
# [^ ] 이 안에는 제외
# A* 는 A여러번 가능 하고 안나와도 되고 1번도 가능하고
# A?B?는 공백, A, B, AB가 나온다.

# (A)(12)(가나다)\1 둥근 괄호를 함수라 생각 첫번 째 괄호를 불러온다
# (A)(12)(가나다)\3 은 3번쨰 괄호를 가지고 온다.
# (A)(12)(가나다)\1\3\1 은 첫번 째 괄호를 2번 3번째를 1번
# (A)([12])([가나다])\1\3\1 A1다A다 이런식 랜덤으로 출
# 하지만 파이썬에서는 사용하지 않는다.

# ([ABC])\1 => AA, BB, CC # 반드시 같은문자가 된다. 이건 기억
# 문자{2} 이건 횟수를 정해주는 것 A{2} AA
# \s : space
# \d : decimal(10진수, [0-9])

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# print(db)

# r : raw
print(re.findall(r'3', db)) # r을 쓰던 안쓰던 거의 똑같다 하지만 항상 붙인다. 혹시 모르
print(re.findall('3', db)) # (패턴, 찾을려는 것)

# 문제
# db로부터 모든 숫자를 찾아보세요
# print(re.findall(r'[0123456789]', db))
# print(re.findall(r'[0-9]', db))
# print(re.findall(r'\d', db)) # 하지만 오류의 가능성이 있다.니

# 문제
# db로부터 전화번호와 아이디를 찾아보세요
# print(re.findall(r'[0-9]+', db))
# # 숫자 1개, 숫자 2개, 숫자 3개, ...

# # 문제
# # db로부터 전화번호를 찾아보세요
# print(re.findall(r'[0-9][0-9][0-9][0-9]', db))
# print(re.findall(r'[0-9]{4}', db))

# # 문제
# # db로부터 이름만 찾아보세요
# print(re.findall(r'[a-zA-Z]+', db)) # 위에가 정답이 된다.
# print(re.findall(r'[A-z]+', db)) # A~z사이에 다른 문자를 가지고 있다.
# print(re.findall(r'[A-Z][a-z]+', db))
#
# # 문제
# # db로부터 T로 시작하는 이름을 출력하세요
# print(re.findall(r'T[a-z]+', db))
#
# # db로부터 T로 시작하지 않는 이름을 출력하세요
# print(re.findall(r'[ABCDEFGHIJKLMNOPQRXUVWXYZ][a-z]+', db))
# print(re.findall(r'[A-SU-Z][a-z]+', db))

print(re.findall(r'Peter.+Alice', db, re.DOTALL)) # 찾고자 하는 것이 여러ㅂ줄에 걸쳐있을 때
