# 클래스 선언
'''
class 클래스 이름:
    클래스 내용
'''
# 인스턴스 이름(변수 이름) = 클래스 이름()  ----> 생성자 함수라고 부른다.

# 생성자 : 클래스 이름과 같은 함수를 생성자(constructor)라고 부른다.
'''
class 클래스 이름:
    def __init__(self, 추가적인 매개변수):
        pass
'''
# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

# 학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 80, 83),
    Student("연하진", 92, 98, 91, 94),
    Student("구지연", 76, 96, 96, 71),
    Student("나선주", 98, 92, 59, 66),
    Student("윤아린", 95, 78, 99, 90),
    Student("윤명월", 64, 100, 88, 92)
]

# Student 인스턴스의 속성에 접근하는 방법
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

# 소멸자(destructor): 생성자와 반대로 인스턴스가 소멸될 때 호출되는 함수,
#                     클래스 내부에 __del__(self) 형태로 함수를 선언해서 만든다.
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))

test = Test("A")

# 메소드(method): 클래스가 가지고 있는 함수
'''
class 클래스 이름:
    def 메소드 이름(self, 추가적인 매개변수):
        pass
'''
# 클래스 내부에 함수(메소드) 선언하기
# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return  self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

# 학생 리스트를 선언
students = [
    Student("윤인성", 87, 98, 80, 83),
    Student("연하진", 92, 98, 91, 94),
    Student("구지연", 76, 96, 96, 71),
    Student("나선주", 98, 92, 59, 66),
    Student("윤아린", 95, 78, 99, 90),
    Student("윤명월", 64, 100, 88, 92)
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep='\t')
for student in students:
    print(student.to_string())

### 클래스는 객체를 위한 설계도이고, 이러한 클래스를 기반으로 만들어진 객체를 인스턴스라고 한다.