# 1부터 999까지 3의 배수와 5의 배수의 합 구하기 예제

result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)