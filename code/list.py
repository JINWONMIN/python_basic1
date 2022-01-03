### 리스트와 반복문
'''리스트란? 여러가지 자료를 저장할 수 있는 자료
             즉, 숫자나 문자, 수식 등의 개별적인 독립 자료를 모아 사용하게 해주는 특별한 형태의 자료'''

# 여섯 개의 자료를 가진 리스트를 선언한 예

array = [273, 32, 103, "문자열", True, False]
print(array)
print(type(array))

# 리스트 선언하고 요소에 접근하기

list_a = [273, 32, 103, "문자열", True, False]     # 인덱스는 0부터 시작
list_a[0]
list_a[1]
list_a[2]
list_a[1:3]

# 리스트 element 변경

list_a = [273, 32, 103, "문자열", True, False]
list_a[0] = "변경"
list_a

# [] 안에 음수를 넣어 뒤에서부터 요소 선택

list_a = [273, 32, 103, "문자열", True, False]
list_a[-1]
list_a[-2]
list_a[-3]

# 리스트 접근 연산자 이중 사용

list_a = [273, 32, 103, "문자열", True, False]
list_a[3]
list_a[3][0]

# 리스트 안에 리스트 사용

list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_a[1]
list_a[1][1]

### 리스트 연산자: 연결(+), 반복(*), len()

# 리스트 선언
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 출력
print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)

# 기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =",list_a * 3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) =", len(list_a))

### 리스트에 elements 추가하기: append, insert
''' 리스트명.append(요소)
    리스트명.insert(위치,요소) '''

# 리스트에 요소 추가

list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

# extend() : 한 번에 여로 요소를 추가할 때

list_a = [1, 2, 3]
list_a.extend([4, 5, 6])
print(list_a)

# 리스트 연결 연산자와 요소 추가의 차이

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a + list_b
list_a                  # list_a와 list_b에는 어떠한 변화도 없음.(비파괴적 처리)
list_b


list_a.extend(list_b)   # 실행결과로 아무 것도 출력하지 않음.
list_a                  # 앞에 입력했던 list_a 자체에 직접적인 변화 존재(파괴적 처리).
list_b

### 리스트에서 요소 제거하기 ( 인덱스로 제거하기, 값으로 제거하기)

# 인덱스로 제거하기: del, pop
'''  del 리스트명[인덱스]    리스트명.pop(인덱스) '''

# 리스트 연결 연산자와 요소 추가의 차이

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)                   # pop()의 매개변수에 아무 것도 입력하지 않으면 자동으로 -1이 들어가 마지막 요소 제거
print("pop(2):", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
list_b

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
list_c

list_d = [0, 1, 2, 3, 4, 5, 6]
del list_d[3:]
list_d

# 값으로 제거하기: remove
''' 리스트.remove(값) '''

list_c = [1, 2, 1, 2]
list_c.remove(2)        # 함수로 지정한 값이 리스트 내부에 여러 개 있어도 내부에서 가장 먼저 발견되는 하나만 제거
list_c

# 모두 제거하기: clear
'''  리스트.clear()  '''

list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
list_d          # 요소가 모두 제거

### 리스트 내부에 있는지 확인하기: in/not in 연산자
'''  값 in 리스트  '''

list_a = [273, 32, 103, 57, 52]
273 in list_a
99 in list_a
100 in list_a
52 in list_a

# not in 연산자: 리스트 내부에 해당 값이 없는지 확인하는 연산(in 연산자와 반대로 동작)

list_a = [273, 32, 103, 57, 52]
273 not in list_a
99 not in list_a
100 not in list_a
52 not in list_a
not 273 in list_a

''' 
★in 연산자를 사용하고 전체를 not으로 감싸는 방법도 사용할 수 있지만, not in 연산자를 사용하는 것이 훨씬 효율적
'''

### for 반복문

for i in range(100):
    print('출력')

### for 반복문 리스트와 함께 사용
''' 
for 반복자 in 반복할 수 있는 것:
    코드
'''

# for 반복문과 리스트

array = [273, 32, 103, 57, 52]

for elements in array:
    print(elements)
'''
for 반복문 리스트에 있는 요소 하나하나가 element라는 변수에 들어가며, 차례차례 반복하게 된다.
print() 함수로 elements 를 출력하므로 리스트의 요소를 차레차례 출력하게 되는 것.
'''

# for 반복문과 문자열
'''
for 반복문은 문자열을 함께 사용할 수도 있음.
문자열을 for 반복문 뒤에 넣으면 글자 하나하나에 반복이 적용된다.
실행결과를 보면 어떤 식으로 실행되는지 쉽게 이해할 수 있다.
'''
for character in "안녕하세요":
    print("-", character)


### 키워드 정리
'''
1. list: 여러 가지 자료를 저장할 수 있는 자료형
2. element: 리스트 내부에 있는 각각의 내용을 의미
3. index: 리스트 내부에서 값의 위치를 의미
4. for 반복문은 특정 코드를 반복해서 실행할 때 사용하는 기본적인 구문
'''

# 연습문제
'''
1. 다음 반복문 내부에 if 조건문의 조건식을 채워서 100 이상의 숫자만 출력하게 만들어 보세요. 
(if 조건문과 for 반복문을 조합)
'''
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print("- 100 이상의 수:",number)

''' 
2. 실행결과에 해당하는 프로그램을 완성해 보세요.
'''
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(number,"는 짝수입니다.")
    else:
        print(number,"는 홀수입니다.")

for number in numbers:
    print(number, "는", len(str(number)), "자릿수입니다.")


'''
3. 숫자를 하나하나 모두 출력해 보세요.
'''
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
]

for line in list_of_list:
    for item in line:
        print(item)

'''
4. 코드의 빈칸을 채워서 실행결과처럼 출력되도록 완성해 보시오.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number)

print(output)
