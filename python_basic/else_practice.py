### 14. else를 사용하여 두 방향으로 분기하기

""" if 조건식:
         코드1
    else:
        코드2
"""

x = 5

if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

### 14.2 else와 들여쓰기

x = 5

if x == 10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')


x = 10

if x == 10: # x가 10이라 조건식이 참
    print('10입니다.')  #출력
else:
    print('x에 들어있는 숫자는')
print('10이 아닙니다.') #출력되지 않아야 하는데 출력됨

### 14.3 if 조건문의 동작 방식 알아보기

if True:
    print('참')      # True는 참
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')     # False는 거짓

if None:   # False로 취급
    print('참')
else:
    print('거짓')     # None은 거짓


### 14.3.1 if 조건문에 숫자 지정하기

f_else_number.py
if 0:
    print('참')
else:
    print('거짓')  # 0은 거짓

if 1:
    print('참')  # 1은 참
else:
    print('거짓')

if 0x1F:  # 16진수
    print('참')  # 0x1F는 참
else:
    print('거짓')

if 0b1000:  # 2진수
    print('참')  # 0b1000은 참
else:
    print('거짓')

if 13.5:  # 실수
    print('참')  # 13.5는 참
else:
    print('거짓')

### 14.3.2 if 조건문에 문자열 지정하기

if 'Hello':  # 문자열
    print('참')  # 문자열은 참
else:
    print('거짓')

if '':  # 빈 문자열
    print('참')
else:
    print('거짓')  # 빈 문자열은 거짓

# 0, None, 빈 문자열을 not으로 뒤집으면?

if not 0:
    print('참')  # not 0은 참

if not None:
    print('참')  # None은 참

if not '':
    print('참')  # not 빈 문자열은 참

### 14.4 조건식을 여러 개 지정하기

x = 10
y = 20

if x == 10 and y == 20:  # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')

### 14.4.1 중첩 if 조건문과 논리 연산자

if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')

if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')

if 0 < x < 20:
    print('20보다 작은 양수입니다.')

### 14.6 연습문제: 합격 여부 판단하기

written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')

"""14.7 심사문제: 합격 여부 판단하기
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 여기서 네 과목의 평균 점수가 
80점 이상일 때 합격이라고 정했습니다. 평균 점수에 따라 '합격', '불합격'을 출력하는 
프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
단, 점수는 0점부터 100점까지만 입력받을 수 있으며 범위를 벗어났다면 
'잘못된 점수'를 출력하고 합격, 불합격 여부는 출력하지 않아야 합니다."""

kor, eng, mat, sci = map(int,input().split())
avg = (kor + eng + mat + sci)/4

if avg >= 80:
    print('합격')
else:
    print('불합격')
if kor < 0 or kor > 100 or eng < 0 or eng > 100 or mat < 0 or mat > 100 or sci < 0 or sci > 100:
    print('잘못된 점수')