# 메모장 만들기

import sys

# option = sys.argv[1]
# memo = sys.argv[2]

# print(option)
# print(memo)


# 입력으로 받은 메모를 파일에 쓰기
# 작성한 메모 출력
option = sys.argv[1]
if option == '-a':
    memo = sys.argv[2]
    with open('./chapter6/memo.txt', 'a') as f:
        f.write(memo)
        f.write('\n')
elif option == '-v':
    with open('./chapter6/memo.txt') as f:
        memo = f.read()
    print(memo)