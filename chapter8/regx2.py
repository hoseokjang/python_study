import re

# | 문자 : | 문자는 or 와 동일한 의미
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

# ^ 문자 : 문자열의 맨 처음과 일치
# print(re.search('^Life', 'My Life is too short'))

# $ 문자 : 문자열의 끝과 일치
# print(re.search('short$', 'Life is too short'))

# \A : 문자열의 처음과 매치 -> ^은 줄에서 처음, \A는 전체 문자열에서 처음

# \Z : 문자열의 끝과 매치 -> \A와 동일

# \b : 단어 구분자, 보통은 공백에 의해 구분
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))

# \B : \b와 반대. 즉, 공백으로 구분된 단어가 아닌 경우에만 매치

# Grouping : ex) ABC 문자열이 계속해서 반복하는지 체크 -> (ABC)+
# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
# m = p.search('park 010-1234-1234')
# print(m.group(2))