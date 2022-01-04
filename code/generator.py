# 제너레이터 함수
''' 제너레이터는 파이썬의 특수한 문법 구조이다. 제너레이터는 이터레이터를 직접 만들 때
사용하는 코드이다. 함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터 함수가 되며,
일반 함수와는 달리 함수를 호출해도 함수 내부의 코드가 실행되지 않는다.'''
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A 지점 통과")
test()      # 제러에리터 함수는 제너레이터를 리턴한다. (출력 값 확인)

print("B 지점 통과")
test()
print(test())

# 제너레이터 객체와 next() 함수
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test()
# ---------- next() 호출 ----------- #
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)

next(output)    # 한 번 더 실행

# 코드의 실행결과를 확인해보면 제너레이터는 직접 이터레이터를 만드는 코드라는 것을 알 수 있음.
# yield 값 까지만 코드를 실행해준다. 메모리의 효율성 업.

# 연습문제1.
numbers = [1, 2, 3, 4, 5, 6]
print(type(numbers))

print("::".join(map(str, numbers)))

# 연습문제2. 다음 코드의 빈칸을 채워서 실행결과처럼 나오게 해주세요.
numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x **2 < 50, numbers)))
print()