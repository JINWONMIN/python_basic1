# not 연산자 조합하기
x = 10
under_20 = x < 20
print("under_20: ", under_20)
print("not under_20: ", not under_20)

# if 조건문의 기본적인 형태

if True:
    print("True입니다...!")
    print("정말 True입니다...!")

if False:
    print("False입니다...!")

### 조건문의 기본 사용

# 입력을 받습니다.
number = input("정수입력> ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다.")

# 음수 조건
if number < 0:
    print("음수입니다.")

# 0 조건
if number == 0:
    print("0입니다.")

### 날짜 / 시간 출력하기

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "월")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")