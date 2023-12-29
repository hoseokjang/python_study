# 클래스(class) 생성
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

# 객체(Object) 생성
cal1 = Calculator()
cal2 = Calculator()
# cal1은 객체, cal1은 Calculator의 인스턴스


class FourCal:
    # 생성자 __init__
    # 인스턴스 생성시 변수명 = 함수이름(변수1, 변수2) 이런 형태로 생성 해줘야함
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result
    
    def sub(self):
        result = self.num1 - self.num2
        return result
    
    def mul(self):
        result = self.num1 * self.num2
        return result
    
    def div(self):
        result = self.num1 / self.num2
        return result

# a = FourCal()
# a.setdata(3,5)
# print(a.add())

# b = FourCal(4, 2)
# print(b.div())

# 클래스의 상속
# 상속 했으므로 FourCal의 기능은 사용 가능
class MoreFourCal(FourCal):
    pass

# Method Overriding
class SafeFourCal(FourCal):
    # 0으로 나누는 경우 오류 발생하므로 예외 처리
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2
        
c = SafeFourCal(4, 0)
print(c.div())

