# 튜플
''' 리스트와 비슷한 자료형,
리스트와 다른 점은 한번 결정된 요소를 바꿀 수 없다는 것,
주로 함수와 함께 많이 사용되는 자료형
'''
tuple_test = (10, 20, 30)

tuple_test[0]
tuple_test[1]
tuple_test[2]

# 요소를 하나만 가진 튜플 선언
tuple_test1 = (273, )
print(tuple_test1)

# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a:" , a)
print("b:" , b)
print("c:" , c)
print("d:" , d)

# 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40                 # 튜플을 입력한 것
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

a, b, c = 10, 20, 30                        # 튜플을 입력한 것
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c", c)

# 변수의 값을 교환하는 튜플
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

a, b = b, a     # 값 교환

print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 튜플과 함수
def test():
    return(10, 20)

a,b = test()

print("a:", a)
print("b:", b)

# 튜플을 리턴하는 함수의 예
for i, value in enumerate([1, 2, 3, 4, 5, 6]):
    print("{}번째 요소는 {}입니다.".format(i, value))

a, b = 97, 40
a // b
a % b

# divmod(): 튜플을 리턴하는 대표적인 함수, 몫과 나머지를 리턴한다.
a, b = 97, 40
divmod(a,b)
x, y = divmod(a, b)
print(x,y)


# 람다 : 함수라는 '기능'을 매개변수로 전달하는 코드를 조금 더 효율적으로 작성할 수 있도록 파이썬은 람다라는 기능을 제공
# 함수의 매개 변수로 함수 전달
def call_10_times(func):    # 매개변수로 받은 함수를 10번 호출하는 함수
    for i in range(10):
        func()

def print_hello():          # 간단한 출력하는 함수
    print("안녕하세요")

call_10_times(print_hello)  # 조합하기

# map() 함수와 filter() 함수

def power(item):
    return item * item
def under_e(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)     # map(), 함수를 매개변수로 사용
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_e, list_input_a)    # filter(), 함수를 매개변수로 사용
print("# filter() 함수의 실행결과")
print("filter(under_e, list_input_a):", output_b)
print("filter(under_e, list_input_a):", list(output_b))

# 람다의 사용
# 함수 선언
power = lambda x: x * x
under_3 = lambda x: x < 3

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print()

# in line lambda
list_input_a = [1, 2, 3, 4, 5, 6]
list_input_b = [1, 2, 3, 4, 5, 6]

output_a = map(lambda x: x * x, list_input_a)   # power() 함수를 선언하지 않고, 매개변수로 바로 넣을 수 있음.
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(lambda  x: x < 3, list_input_a)   # filter() 함수를 선언하지 않고, 매개변수로 바로 넣을 수 있음.
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print()

# 매개 변수가 여러 개인 람다
test_output = lambda x, y: x * y
test_output_1 = map(test_output, list_input_a, list_input_b)
print(list(test_output_1))

''' 파일 처리 '''

# 파일 열고 닫기
''' 파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)'''
file = open("basic.txt", "w")

# 파일에 텍스트 작성
file.write("프로그램이 외부 파일, 외부 네트워크 등과 통신할 때는 데이터가 흐르는 길을 만들어야 한다.")

# 파일 닫기
file.close()

# with 키워드: 조건문과 반복문이 들어가다 보면 파일을 열고 닫지 않는 실수를 하는 경우가 종종 발생한다.
#              이런 실수를 방지하기 위해 with 키워드라는 기능이 생겼음.
''' with open(문자열: 파일 경로, 문자열: 모드) as 파일 객체:
            문장
'''
with open("basci.txt","w") as file:
    file.write("이를 스트림이라고 부릅니다.")
# 텍스트 읽기: read()
with open("../info.txt", "r") as file:
    contents = file.read()  # 파일을 읽고 출력
print(contents)

# 랜덤하게 1000명의 키와 몸무게 만들기
import random   # 랜덤한 숫자를 만들기 위해 가져온다.

hanguls = list("가나다라마바사아자차카타파하")    # 간단한 한글 리스트 생성

with open("../info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))

# 키와 몸무게로 bmi(비만도) 계산
# 반복문으로 파일 한 줄씩 읽기
with open("../info.txt", "r") as file:
    for line in file:
        # 변수 선언
        (name, weight, height) = line.strip().split(", ")

        # 데이터가 문제없는지 확인: 있으면 지나감
        if not (name or weight or height):
            continue
        # 결과 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        # 출력
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "bmi: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))

        print()

