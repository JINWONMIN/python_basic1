### 15. elif를 사용하여 여러 방향으로 분기하기

# 15.1 elif 사용하기
x = 20
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')

# 15.1.1 if, elif, else를 모두 사용하기
x = 30

if x == 10:  # x가 10일 때
    print('10입니다.')
elif x == 20:  # x가 20일 때
    print('20입니다.')
else:  # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')

# 15.1.2 음료수 자판기 만드릭
button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

# 15.3 연습문제: if, elif, else 모두 사용하기
if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

"""15.4 심사문제: 교통카드 시스템 만들기
표준 입력으로 나이(만 나이)가 입력됩니다(입력 값은 7 이상 입력됨). 
교통카드 시스템에서 시내버스 요금은 다음과 같으며 각 나이에 맞게 
요금을 차감한 뒤 잔액이 출력되게 만드세요(if, elif 사용). 
현재 교통카드에는 9,000원이 들어있습니다.

어린이(초등학생, 만 7세 이상 12세 이하): 650원
청소년(중∙고등학생, 만 13세 이상 18세 이하): 1,050원
어른(일반, 만 19세 이상): 1,250원"""

age = int(input())
balance = 9000

if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif age >= 19:
    balance -= 1250

print(balance,"원")