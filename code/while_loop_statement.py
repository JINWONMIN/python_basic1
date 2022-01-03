### for 반복문 법위와 함께 사용
'''  for 숫자 변수 in 범위:
     코드
'''
for i in range(5):
    print(str(i) + "=반복 변수")
print()

for i in range(5,10):
    print(str(i) + "=반복 변수")
print()

for i in range(0,10,3):
    print(str(i) + "=반복 변수")
print()

### for 반복문: list와 range 조합하기

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))

### for 반복문: 반대로 반복하기

# range() 변수를 사용하는 경우
for i in range(4, 0 -1, -1):    # "0까지 반복하고 싶어서 이 코드를 사용했어" 강조하기 위해 -1 대신 0 -1 사용
    print("현재 반복 변수: {}".format(i) )

# reversed() 사용
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

### while 반복문
'''
list 또는 dictionary 내부의 element을 모두 순회하는 경우, 즉 특정 횟수만큼 반복하는 경우에는
for 반복문을 사용. 하지만 파이썬에서는 for 반복문 이외에도 범용적으로 사용할 수 있는 while 반복문이 있음.

--- while 반복문의 기본 형태 ---
while 불 표현식:
    문장
'''
while True:            # 무한 루프
    # "."을 출력합니다.
    # 기본적으로 end가 "\n"이라 줄바꿈이 일어나는데
    # 빈 문자열 ""로 바꿔서 줄바꿈이 일어나지 않게 합니다.
    print(".", end="")

# while 반복문을 for 반복문처럼 사용하기

i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# while 반복문: 상태를 기반으로 반복하기

list_test = [1, 2, 1, 2]
value = 2

# list_test 내부에 value가 있다면 반복
while value in list_test:
    list_test.remove(value)

print(list_test)

# while 반복문: 시간을 기반으로 반복하기
''' 
유닉스 타임: 세계 표준시(utc)로, 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가 지났는지를 정수로 나타낸 것
'''
import time
time.time()

# 5초 동안 반복하기
import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))

# while 반복문: break 키워드/continue 키워드
''' break 키워드 '''
i = 0

while True:
    print("{}번째 반복문입니다.".format(i))
    i = i + 1

    input_text = input(">종료하시겠습니까?(y/n): ")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다.")
        break

'''continue 키워드'''
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)

# 연습문제2. 키와 값으로 이루어진 각 리스트를 조합해 하나의 딕셔너리로 만들어 보시오.

# 숫자는 무작위로 입력해도 상관없음.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0,len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)

''' 연습문제3. 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다. 몇을 더할 때 1000을 넘는지 구해 보세요.
그리고 그때의 값도 출력해 보세요. 다음은 10000이 넘는 경우를 구한 예입니다.
1, 1+2 =3, 1 + 2 +3 = 6, 1+ 2+ 3+ 4 = 10 ...'''

limit = 10000
i = 1

sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으면 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

''' 연습문제4. 1부터 100까지의 숫자가 있다고 합시다. 이를 다음과 같이 계산한다고 했을 때, 최대가 되는 경우는 어떤 숫자를
곱했을 때인지를 찾아 주세요.
1 * 99, 2 * 98, 3 * 97, ..., 98 * 2, 99 * 1
실행결과: 최대가 되는 경우: 50 * 50 = 2500 '''

max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - 1
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
