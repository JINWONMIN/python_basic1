

# 기본적인 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# 매개변수의 기본

def print_n_times(values, n):
    for i in range(n):
        print(values)

print_n_times("안녕하세요",5)

#가변 매개변수 함수

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()     # 단순한 줄바꿈

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# 기본 매개변수
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")

# 키워드 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n = 3)

# 기본 매개변수 중에서 필요한 값만 입력하기
def test(a, b = 10, c = 100):
    print(a + b + c)

test(10, 20, 30)    # 기본 형태
test(a = 10, b = 100, c = 200)  # 키워드 매개변수로 모든 매개변수를 지정한 형태
test(c = 10, a = 100, b = 200)  # 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(10, c = 200)   # 키워드 매개변수로 일부 매개변수만 지정한 형태

# 자료 없이 리턴하기
def return_test():
    print("a위치")
    return          # 함수를 실행했던 위치로 돌아가라는 뜻으로, 함수가 끝나는 위치를 의미
    print("b위치")

return_test()

# 자료와 함께 리턴하기
def return_test1():
    return 100

value = return_test1()
print(value)

# 아무것도 리턴하지 않았을 때의 리턴값
def return_test2():
    return

value1 = return_test2()
print(value1)

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0

    for i in range(start, end + 1):
        output += i
    return output


print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))

# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start = 0, end = 100, step = 1):
    output = 0

    for i in range(start, end + 1, step):
        output += i
    return output

print("a.", sum_all(0, 100, 10))
print("b.", sum_all(end = 100))
print("c.", sum_all(end = 100, step = 2))

# 보기와 같은 방정식을 파이썬 함수로 만드시오.
# (1) f(x) = 2x + 1

def f(x):
    return 2 * x + 1
print(f(10))

# (2) f(x) = x제곱 + 2x + 1

def f(x):
    return x ** 2 + 2 * x + 1
print(f(10))

# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만드시오.

def mul(*values):
    i = 1
    for value in values:
        i *= value
    return i

print(mul(5, 7, 9, 10))
