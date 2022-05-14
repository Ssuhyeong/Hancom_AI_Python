# Day_24_01_ReOpenHangul.py
import re
import requests

# 구글 입력창
# http://www.google.com/search ? q=python & newsindow=1
#             함수                        매개변수
# http://openhangul.com/nlp_ko2en ?     q=핸드폰


# 문제
# 오픈한글 사이트로부터 한글을 입력하면 키보드상의 알파벳을 알려주는 웹사이트를 파싱합니다.
# 사이트에 전달한 한글이 어떤 영문 글자를 가리키는지 알려주세요

# url = 'http://openhangul.com/nlp_ko2en?q=%EA%BC%AC%EA%B9%94%EC%BD%98'     # get 방식

word = '핸드폰'
# url = 'http://openhangul.com/nlp_ko2en?q=' + word
url = 'http://openhangul.com/nlp_ko2en?q={}'.format(word)
received = requests.get(url)

text = received.content.decode('utf-8')
# print(text)

# result = re.findall(r'<img src="images/cursor.gif"><br>(.+)</pre>', text, re.DOTALL)
# print(result[0].strip())

result = re.findall(r'<img src="images/cursor.gif"><br>(.+)', text)

print(result[0].strip())

