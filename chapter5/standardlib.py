import datetime

# 1. datetime.date
# day1 = datetime.date(2021,12,14)
# day2 = datetime.date(2023,4,5)
# diff = day2 - day1
# print(diff.days)
# print(day1.weekday()) # 0 : 월요일, 1 : 화요일 ...
# print(day1.isoweekday()) # 1 : 월요일, 2 : 화요일 ...


# 2. time
import time

# 현재 시간을 실수형으로 리턴
# print(time.time())

# time.time()인 현재 시간을 연,월,일,시,...의 형태로 바꾸어 리턴
# print(time.localtime(time.time()))

# time.localtime을 알아보기 쉬운 형태로 리턴
# print(time.asctime(time.localtime(time.time())))

# time.asctime을 간단하게 표현
# print(time.ctime())

# 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷 코드를 제공
# print(time.strftime('%x %X', time.localtime(time.time())))

# 일정 시간 간격을 둘때 사용
# for i in range(5):
#     print(i)
#     time.sleep(1) # 1초 간격


# 3. Math
import math

# 최대 공약수 구하기
# print(math.gcd(60, 80, 100))

# 최소 공배수 구하기
# print(math.lcm(15, 25))


# 4. Random
import random

# 0.0과 1.0 사이의 실수 중에 난수 값을 리턴
# print(random.random())

# 1에서 10 사이의 정수값 리턴
# print(random.randint(1, 10))

# 1에서 55 사이의 정수값 리턴
# print(random.randint(1, 55))


# 5. itertools.zip_longest
import itertools

# zip 함수를 사용할 때 객체끼리 길이가 다르면 긴 객체의 남는 값은 버려지는데 
# itertools.zip_longest 함수를 사용하면 긴 객체에 맞춰 채울수 있음
# students = ['한민서', '황지민', '이영철', '이광수', '김승민']
# snacks = ['사탕', '초콜릿', '젤리']

# print(list(zip(students, snacks))) # students의 뒤에 두 객체가 버려짐
# print(list(itertools.zip_longest(students, snacks, fillvalue = '새우깡')))

# 반복 가능 객체 중에서 r개를 선택한 순열을 이터레이터로 리턴
# 즉, 리스트와 반복 r을 받아 순열 생성
# print(list(itertools.permutations(['1', '2', '3'], 2)))

# 조합 구하기
# print(list(itertools.combinations(range(1, 4), 2)))
# print(len(list(itertools.combinations(range(1, 4), 2)))) # 길이 구하기


# 6. functools
import functools

# data = [1,2,3,4,5]
# reduce로 합 구하기
# print(functools.reduce(lambda x, y : x + y, data))

# num_list = [1, 9, 2, 3, 8, 4, 5]
# reduce로 최댓값 구하기
# print(functools.reduce(lambda x, y : x if x > y else y, num_list))


# 7. operator
from operator import itemgetter
# 튜플 일때는 itemgetter, 객체 일때는 attrgetter 사용

# students = [
#     ("jane", 22, 'A'),
#     ("dave", 32, 'B'),
#     ("sally", 17, 'B'),
# ]

# 나이 순으로 정렬
# print(sorted(students, key = itemgetter(1)))

# students = [
#     {"name": "jane", "age": 22, "grade": 'A'},
#     {"name": "dave", "age": 32, "grade": 'B'},
#     {"name": "sally", "age": 17, "grade": 'B'},
# ]

# print(sorted(students, key=itemgetter('age')))


# 8. shutil
# 파일을 복사하거나 이동할 때 사용하는 모듈
import shutil
# shutil.copy('c:/aaa/a.txt', 'c:/temp/temp.txt')
# shutil.move('c:/aaa/a.txt', 'c:/temp/temp.txt')


# 9. glob
import glob

# 디렉토리에 있는 파일들을 리스트로 만들기
# glob.glob('c:/aaa/a*')


# 10. pickle
import pickle

# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올수 있게하는 모듈
# dump를 사용하여 저장 가능, load를 사용하여 불러오기 가능
# f = open('test.txt', 'wb')
# data = {1 : 'python', 2 : 'you need'}
# pickle.dump(data, f)
# f.close()

# f = open('test.txt', 'rb')
# data = pickle.load(f)
# print(data)


# 11. os
import os

# 환경 변수나 디렉토리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
# print(os.environ['PATH'])

# 디렉토리 위치 변경하기
# os.chdir('C:\WIMDOWS')

# 디렉토리 위치 리턴
# print(os.getcwd())

# 시스템 명령어 호출하기
# print(os.system("dir"))

# 실행한 시스템 명령어의 결과값 돌려받기
# f = os.popen("dir")
# print(f.read())

# 디렉토리 생성
# os.mkdir(디렉토리)

# 디렉토리 삭제
# os.rmdir(디렉토리)

# 파일 삭제
# os.remove(파일)

# rename
# os.rename(변경 전, 변경 후)


# 12. zipfile
import zipfile
# 여러 개의 파일을 zip 형식으로 합치거나 해체할 때 사용하는 모듈

# 파일 합치기
# with zipfile.ZipFile('test.zip', 'w') as testzip:
#     testzip.write('a.txt')
#     testzip.write('b.txt')
#     testzip.write('c.txt')

# 해제하기
# with zipfile.ZipFile('test.zip') as testzip:
#     testzip.extractall()

# 특정 파일만 해제하기
# with zipfile.ZipFile('test.zip') as testzip:
#     testzip.extractall('a.txt')


# 13. json
import json
# json 파일 읽기
# with open('info.json') as f:
#     data = json.load(f)


# 14. urllib
import urllib.request
# URL을 읽고 분석할 때 사용하는 모듈

# def get_wikidocs(page):
#     resource = 'https://wikidocs.net/{}'.format(page)
#     with urllib.request.urlopen(resource) as s:
#         with open('wikidocs_%s.html' %page, 'wb') as f:
#             f.write(s.read())


# 15. webbrowser
import webbrowser
# 시스템 브라우저를 호출할 때 사용하는 모듈

# 새창으로 열 때
# webbrowser.open_new('http://python.org')

# 이미 열려있는 창으로 열 때
# webbrowser.open('http://python.org')