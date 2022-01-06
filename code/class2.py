# 어떤 클래스의 인스턴스인지 확인하기
''' isinstance(인스턴스, 클래스) '''
class Student:
    def __init__(self):
        pass

student = Student()

print("isinstance(studend, Student):", isinstance(student, Student))

# isinstance() 함수와 type() 함수로 확인하는 것의 차이
class Human:
    def __init__(self):
        pass

class Student(Human):
    def __init__(self):
        pass

student = Student()

# 인스턴스 확인
print("isinstance(student, Human):", isinstance(student, Human))    # isinstance(): 상속까지 확인
print("type(student) == Human:", type(student) == Human)            # type(): 상속 관계 확인 x

# isinstance() 활용: 리스트 내부에 여러 종류의 인스턴스가 들어 있을 때, 인스턴스들을 구분하며 속성과 기능을 사용할 때 사용.
# 학생 클래스 선언
class Student:
    def study(self):
        print('공부를 한다.')

# 선생님 클래스 선언
class Teacher:
    def teach(self):
        print("학색을 가르친다.")

# 교실 내부의 객체 리스트를 생성
classroom = [Student(), Student(), Teacher(), Student(), Student()]

# 반복을 적용해서 적절한 함수를 호출하게 한다.
for person in classroom:
    if isinstance(person, Student):
        print("공부를 한다.")
    elif isinstance(person, Teacher):
        print("학생을 가르친다.")

# __str__() 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    # __str__()이라는 이름으로 함수 선언
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

students = [
    Student("윤인성", 87, 98, 80, 83),
    Student("연하진", 92, 98, 91, 94),
    Student("구지연", 76, 96, 96, 71),
    Student("나선주", 98, 92, 59, 66),
    Student("윤아린", 95, 78, 99, 90),
    Student("윤명월", 64, 100, 88, 92)
]

print("이름", "총점", "평균", sep='\t')
for student in students:
    print(str(student))     # str() 함수의 매개변수로 넣으면 student의 __str__() 함수가 호출됨

# 크기 비교 함수
# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

# 학생 리스트를 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, +2),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

# 학생을 선언
student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

# 출력
print("student_a == student_b =", student_a == student_b)
print("student_a != student_b =", student_a != student_b)
print("student_a > student_b =", student_a > student_b)
print("student_a >= student_b =", student_a >= student_b)
print("student_a < student_b =", student_a < student_b)
print("student_a <= student_b =", student_a <= student_b)

# TypeError 발생시키기

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() == value.get_sum()

student_a = Student("윤인성", 87, 98, 88, 95)
student_a == 10

# 클래스 변수
# 클래스 선언
class Student:
    cnt = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        Student.cnt += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.cnt))

# 학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

# 출력
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.cnt))     # 클래스 내부와 외부에서 클래스 변수에 접근할 때는 (클래스 이름.변수이름)을 사용.

# 클래스 함수
# 클래스 선언
class Student:
    # 클래스 변수
    cnt = 0
    students = []

    # 클래스 함수
    @classmethod    # decorator
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:    # Student.students라고 해도 상관없지만, 매개변수로 받은 cls를 활용
            print(str(student))
        print("------ ------ ------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.cnt += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.english + self.math + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

# 학생 리스트 선언
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

# 현재 생성된 학생을 모두 출력
Student.print()