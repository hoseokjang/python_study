# 1. [] 문자 : 문자 클래스
# [0-9] : 모든 숫자
# [a-zA-Z] : 모든 알파벳

# 2. . 문자 : \n을 제외한 모든 문자
# a + 모든 문자 + b
# a.b
# a[.]b -> a + . + b를 의미

# 3. * 문자 : * 앞에 문자가 0부터 무한대까지 반복 가능
# ca*t -> a 반복

# 4. + 문자 : + 앞에 문자가 1부터 무한대까지 반복 가능
# ca+t -> a 반복

# 5. {m,n} 문자 : {} 앞의 문자를 m번부터 n번까지 반복 가능
# ca{2,5}t

# 6. ? 문자 : {0,1}을 의미
# ca?t


# re 모듈
import re
p = re.compile('[a-z]+')

# match() : 문자열의 처음부터 정규식과 매치되는지 조사
# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall() : 정규식과 매치되는 모든 문자열 (substring)을 리스트로 리턴
# finditer() : 정규식과 매치되는 모든 문자열 (substring)을 반복 가능한 객체로 리턴

# match()
# m = p.match('python')
# print(m) # p 조건에 부합하므로 <re.Match object; span=(0, 6), match='python'> 리턴
# n = p.match('3 python')
# print(n) # # 3으로 시작해 조건에 부합하지 않아 None 리턴

# match 객체의 메소드
# print(m.group()) # 매치된 문자열 리턴
# print(m.start()) # 매치된 문자열의 시작 위치 리턴
# print(m.end()) # 매치된 문자열의 끝 위치 리턴
# print(m.span()) # 매치된 문자열의 시작, 끝에 해당하는 튜플 리턴

# search()
# m = p.search('python')
# print(m)
# n = p.search('3 python')
# print(n)

# findall
# result = p.findall("life is too short")
# print(result)

# finditer
# result = p.finditer("life is too short")
# for i in result:
#     print(i)

# 역슬래시
# \section으로 입력하면 \s가 whitespace로 인식
# \\section으로 입력해야함
# p = r.compile('\\section')