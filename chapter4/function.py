# def add(a, b):
#     return a+b

# print(add(1,2))

# def say():
#     return 'Hi'
# a = say()
# print(a)

# 입력값 여러개 받는 함수1
# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result
# print(add_many(1,2,3,4,5))

# 입력값 여러개 받는 함수2
# def add_mul(choice, *args):
#     if choice == 'mul':
#         result = 1
#         for i in args:
#             result = result * i
#     elif choice == 'add':
#         result = 0
#         for i in args:
#             result = result + i
#     return result
# print(add_mul('mul', 1,2,3,4,5))

# 키워드 매개변수
# def print_kwargs(**kwargs):
#     print(kwargs)
# print(print_kwargs(a=1))
# print(print_kwargs(name='kim', age=3))

# lambda 예약어
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식
# add = lambda a, b, c : a + b + c