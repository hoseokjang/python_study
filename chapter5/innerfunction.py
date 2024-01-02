# 1. abs - 절대값
# print(abs(-3))

# 2. all - 요소 전부 판별 > 참/거짓
# print(all([0]))
# print(all([1, 2, 3, -1]))

# 3. any - 요소 중 일부 판별 > 모두 거짓일때만 False 
# print(any([1, 2, 3, 0]))
# print(any([0, ""]))

# 4. chr - 유니코드 입력받아 문자 리턴
# print(chr(97))

# 5. dir - 객체가 지닌 변수나 함수를 보여줌
# print(dir([1, 2, 3]))

# 6. divmod - 두 개의 숫자를 입력 받아 몫과 나머지를 튜플로 리턴
# print(divmod(7,2))

# 7. enumerate - 순서가 있는 데이터를 입력 받아 인덱스 값을 포함하는 객체를 리턴
# for i, name in enumerate(['body', 'foo', 'bar']):
    # print(i, name)

# 8. eval - 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행후 리턴
# print(eval('1+2'))

# filter - filter(함수, 반복_가능_데이터)
# def positive(x):
#     return x > 0
# print(list(filter(positive, [1, -3, 2, -5, 7, 0])))
# print(list(filter(lambda x: x > 0, [1, -3, 2, -5, 7, 0])))

# 9. hex - 정수를 입력받아 16진수 문자열로 변환하여 리턴
# print(hex(16))

# 10. id - 객체를 입력받아 객체의 고유 주소값을 리턴
# print(id(7))

# 11. int - 문자열 형태의 숫자 혹은 소수점이 있는 숫자를 정수로 리턴
# print(int(3.4))

# 12. isinstance - isinstance(object,class) 입력받은 객체가 그 클래스의 인스턴스인지 판별
# class Person: pass
# a = Person()
# print(isinstance(a, Person))

# 13. len - 입력값의 길이 리턴
# print(len([1, 2, 3]))

# 14. list - 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴
# print(list('python'))

# 15. map(f, iterable) - 함수 f와 반복 가능한 데이터 입력 받음
# def two_times(x):
    # return x * 2
# print(list(map(two_times, [1, 2, 3, 4])))

# 16. oct - 정수를 8진수 문자열로 변환
# print(oct(5))

# 17. ord - 문자의 유니코드 숫자 값을 리턴
# print(ord('가'))

# 18. pow(x, y) - x를 y 제곱한 값을 리턴
# print(pow(5, 2))

# 19. round - 숫자를 입력받아 반올림 후 리턴
# print(round(4.55, 1))

# 20. sorted - 데이터 정렬
# print(sorted([3, 1, 2]))

# 21. str - 문자열 객체로 리턴
# print(str(3))

# 22. sum - 입력 데이터의 합 리턴
# print(sum([1, 2, 4]))

# 23. tuple(iterable) - 반복 가능한 데이터를 튜플로 변환해 리턴
# print(tuple("abc"))

# 24. type - 입력값의 자료형 리턴
# print(type(1.4))

# 25. zip - 동일한 개수로 이루어진 데이터들을 묶어서 리턴
# print(list(zip([1, 2, 3], [4, 5, 6])))