# garbage collector: 더 사용할 가능성이 없는 데이터를 메모리에서 제거하는 역할

# garbage collector: 변수에 저장하지 않은 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

Test("A")
Test("B")
Test("C")

# garbage collector: 변수에 저장한 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")

# 원의 둘레와 넓이를 구하는 객체 지향 프로그램
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return  math.pi * (self.radius ** 2)

circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

''' Circle 클래스의 radius 속성에 음수를 넣으면 둘레가 음수가 발생됨 '''
circle = Circle(10)
circle.radius = -2
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

# 프라이빗 변수: __<변수 이름>
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return  math.pi * (self.__radius ** 2)

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

# __radius에 접근
print("# __radius에 접근합니다.")
print(circle.__radius)

# getter and setter
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    # 게터 세터 변수를 안전하게 사용하기
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 한다.")
        self.__radius = value

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

print("# __radius에 접근합니다.")
print(circle.get_radius())
print()

circle.set_radius(-2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

# 데코레이터를 사용해 게터와 세터 만들기
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    # 게터 세터 선언
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 한다.")
        self.__radius = value

print("# 데코레이터를 사용한 Getter와 Setter.")
circle = Circle(10)
print("원래 원의 반지름:", circle.radius)
circle.radius = 2
print("변경된 원의 반지름:", circle.radius())
print()

print("# 강제로 예외 발생")
circle.radius = -10