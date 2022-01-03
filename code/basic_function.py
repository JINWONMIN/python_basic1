''' 문자열, 리스트, 딕셔너리와 관련된 기본 함수'''

# 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()

numbers = [103, 52, 273, 32, 77]
min(numbers)
max(numbers)
sum(numbers)

# 리스트를 사용하지 않고 최솟값, 최댓값 구하기

min(103, 52, 273)
max(103, 52, 273)

# reversed() 함수로 리스트 뒤집기

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)

''' 확장 슬라이싱
리스트에 [::-1]을 붙이면 리스트의 내용이 뒤집힘. 비파괴적 코드이므로 원본 numbers에는 영향이 없음.'''

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[::-1])

# enumerate() 함수와 반복문 조합하기

# 방법 1
example_list = [ "요소A", "요소B", "요소C"]
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1

# 방법 2
example_list = [ "요소A", "요소B", "요소C"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

'''enumerate() 함수와 리스트'''

example_list = [ "요소A", "요소B", "요소C"]

print(enumerate(example_list))
print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

# 딕셔너리의 items() 함수와 반복문 조합하기

example_dictionary = {
    "키a": "값a",
    "키b": "값b",
    "키c": "값c",
}

print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

# 반복문을 사용한 리스트 생성

array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

# list 안에 for문 사용하기 (리스트 내포)

array = [i * i for i in range(0, 20, 2)]
print(array)

# 조건을 활용한 리스트 내포

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)

# if 조건문과 여러 줄 문자열(1)

number = int(input("정수 입력>"))

if number % 2 == 0:
    print('''\
                입력한 문자열은 {}입니다.
                {}는(은) 짝수입니다.'''.format(number, number))
else:
    print('''\
                입력한 무자열은 {}입니다.
                {}는(은) 홀수입니다.'''.format(number,number))

# 괄호로 문자열 연결하기
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성된다."
)

print(type(test))
print(test)

# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1)

number = int(input("정수 입력> "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
              "입력한 문자열은 {}입니다.\n"
              "{}는(은) 홀수입니다."
          ).format(number, number))

# 문자열의 join() 함수
''' 문자열.join(문자열로 구성된 리스트'''
print("::".join(["1", "2", "3", "4", "5"]))

# reversed() 함수와 이터레이터

numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# 10진수와 2진수 변환
"{:b}".format(10)
int("1010",2)

# 10진수와 8진수 변환
"{:o}".format(10)
int("12",8)

# 10진수와 16진수 변환
"{:x}".format(10)
int("10",16)

"안녕안녕하세요".count("안")

''' 연습문제
1~100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드를 만드시오.
'''
output = [i for i in range(1, 100 + 1)
          if "{:b}".format(i).count("0") == 1 ]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))
