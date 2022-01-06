# Inheritance : 어떤 클래스가 갖고 있는 기능을 물려받는 것
# 상속의 활용
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

# 자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출
child = Child()
child.test()
print(child.value)

# 사용자 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)

raise CustomException

# ---------------------------------------------------------------------------------- #

# 자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("### 커스텀 오류 생성 ###")
    def __str__(self):
        return "오류 발생"

raise CustomException
''' __str__() 함수는 부모(Exception 클래스)에도 정의되어 있다.
이처럼 부모에 정의되어 있는 함수를 자식에게 다시 정의하는 것을 재정의 또는 오버라이드라고 부른다.'''

# ---------------------------------------------------------------------------------- #

# 자식 클래스로써 부모에 없는 새로운 함수 정의하기

# 사용자 정의 예외 생성
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("##### 오류 정보 #####")
        print("메세지:", self.message)
        print("값:", self.value)
# 예외 발생
try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()