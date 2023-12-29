# 1. try-except
# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# 2. try-finally
# 예외 여부에 상관없이 항상 finally 수행
# try:
#     f = open('foo.txt', 'r')
# finally:
#     f.close()

# 3. 여러개의 오류 처리하기
# try:
#     a = [1, 2]
#     print(a[3])
#     4/0
# except(ZeroDivisionError, IndexError) as e:
#     print(e)

# 4. try-else
# try:
#     age = int(input('나이를 입력하세요:'))
# except:
#     print('입력이 정확하지 않습니다.')
# else:
#     if age <= 18:
#         print('미성년자는 출입 금지 입니다.')
#     else:
#         print('환영합니다.')

# 5. 오류 회피하기
# try:
#     f = open('없는 파일', 'r')
# except:
#     pass

# 6. 오류 일부러 발생시키기
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

# 7. 예외 만들기
# class MyError(Exception):
#     pass

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)

# say_nick('바보')
# say_nick('천사')