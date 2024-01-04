# 문서 파일을 읽어서 그 문서 파일 안에 있는 Tap 문자를 공백 4개 문자로 바꾸는 예제

import sys

src = sys.argv[1]
dst = sys.argv[2]

# print(src)
# print(dst)

with open('./chapter6/memo.txt', 'r') as f:
    tap_content = f.read()
space_content = tap_content.replace("\t", " " * 4)
# print(space_content)

with open(dst, 'w') as f:
    f.write(space_content)