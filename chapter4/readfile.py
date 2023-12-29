# f = open("새파일.txt", 'w')
# f.close()

# r : 읽기 모드
# w : 쓰기 모드
# a : 추가 모드. 파일의 마지막에 새로운 내용 추가

# 파일을 쓰기 모드로 열어 내용 쓰기
# f = open("C:/mongta/newfile.txt", 'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()

# readline -> 파일을 읽기 모드로 열어 파일의 첫 번째 줄을 읽어 출력
# f = open("C:/mongta/newfile.txt", 'w')
# line = f.readline()
# print(line)
# f.close()

# 모든 줄 읽어 출력
# f = open("C:/mongta/newfile.txt", 'w')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.closs()

# readlines -> 파일의 모든 줄을 읽어 각각의 줄을 요소로 가지는 리스트를 리턴
# ex) ["1번째 줄입니다.\n", "2번째 줄입니다.\n", ..., "10번째 줄입니다.\n"]를 리턴
# '\n' 제거하기
# f = open("C:/mongta/newfile.txt", 'w')
# lines = f.readlines()
# for line in lines:
#     line = lines.strip() # 줄 끝의 줄 바꿈 문자 제거
#     print(line)
# f.close()

# read -> 파일의 내용 전체를 문자열로 리턴
# f = open("C:/doit/새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# 파일에 새로운 내용 추가
# f = open("C:/doit/새파일.txt", 'r')
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

# with문 사용하기
# with open('foo.txt', 'w') as f:
#     f.write("Life is too short, you need Python")
