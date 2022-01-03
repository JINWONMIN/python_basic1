# 재귀함수

# 반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

factorial(0)

# 재귀 함수를 사용해 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

# 재귀 함수로 구현한 피보나치 수열(1)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(1):",fibonacci(1))
print("fibonacci(2):",fibonacci(2))
print("fibonacci(3):",fibonacci(3))
print("fibonacci(4):",fibonacci(4))
print("fibonacci(5):",fibonacci(5))
print(fibonacci(35))

# 재귀 함수로 구현한 피보나치 수열(2)
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))

# 메모화
dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
print("fibonacci(10):",fibonacci(10))
print("fibonacci(20):",fibonacci(20))
print("fibonacci(30):",fibonacci(30))
print("fibonacci(40):",fibonacci(40))
print("fibonacci(50):",fibonacci(50))

# 조기 리턴
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    output = fibonacci(n - 1) + fibonacci(n - 2)
    dictionary[n] = output
    return output

''' 연습문제1.
다음 빈칸을 재귀 함수로 만들어서 리스트를 평탄화하는 함수를 만들어 보세요.'''
example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

print("원본:", example)
print("변환:", flatten(example))

''' 연습문제2.
패밀리 레스토랑에서 여러 개의 테이블에 나누어 앉으려고 합니다. 이때 한 사람만 앉는 테이블이 없게 그룹을 지어야 합니다.
인원 수를 나누는 패턴만 구하면 되며, 누가 어디에 앉는지 등은 고려하지 않아도 괜찮습니다. 예를 들어 6명이라면
다음과 같은 네 가지 경우를 생각할 수 있습니다.
2명 + 2명 + 2명    2명 + 4명    3명 + 3명     6명
한 개의 테이블에 앉을 수 있는 최대 사람의 수는 10명입니다. 100명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴을 구하세요.
'''

min_party = 2
max_party = 10
people = 100
memo = {}

def issue(a, b):
    key = str([a,b])
    # 종료 조건
    if key in memo:
        return memo[key]
    if a < 0:
        return 0
    if a == 0:
        return 1
    count = 0
    for i in range(b, max_party + 1):
        count += issue(a - i, i)

    memo[key] = count
    return count

print(issue(people, min_party))
