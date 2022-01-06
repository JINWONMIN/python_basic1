# exception object
'''
try:
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 as 예외 객체를 활용할 변수 이름:
    예외가 발생했을 때 실행할 구문
'''
'''
예외가 발생하면
예외 정보가 생기고
예외 정보는 예외 객체에 저장된다.
'''
try:
    pi = 3.14
    number_input_a = int(input("정수 입력>"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * pi * number_input_a)
    print("원의 넓이:", pi * number_input_a * number_input_a)

except Exception as ex:
    print("type(exception):",type(ex))
    print("exception:", ex)

# 예외 구분하기
# 여러 가지 예외가 발생할 수 있는 코드
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소:{}".format(number_input, list_number[number_input]))
except Exception as ex:
    print("type(ex):", type(ex))
    print("ex:", ex)
'''
try:
    예외가 발생할 가능성이 있는 구문

except 예외의 종류A:
    예외A가 발생했을 때 실행할 구문
except 예외의 종류B:
    예외B가 발생했을 때 실행할 구문
except 예외의 종류C:
    예외C가 발생했을 때 실행할 구문    
'''
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요")
except IndexError:
    print("리스트의 인덱스를 벗어났습니다.")

# ----------------------------------------------------------------------------------------------- #

# 예외 구분 구문과 예외 객체

list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다.")
    print("exception:", exception)

# ----------------------------------------------------------------------------------------------- #

# 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수 입력")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스 범위 벗어남")
    print(type(exception), exception)
except Exception as exception:      # ValueError와 IndexError가 아닌 예외가 발생했을 때 실행된다.
    print("파악하지 못한 예외 발생")
    print(type(exception), exception)