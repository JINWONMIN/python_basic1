### 딕셔너리와 반복문 ###
'''
list가 '인덱스를 기반으로 값을 저장하는 것'이라면
dictionary는 '키를 기반으로 값을 저장하는 것'
{     키   값
    "키A": 10,       # 문자열을 키로 사용
    "키B": 20,
    "키C": 30,
    1:     40,      # 숫자를 키로 사용
    FALSE: 50,      # 불을 키로 사용
}
'''

# 딕셔너리 선언 및 요소에 접근

dict_a = {
    "name": "어밴저스 엔드게임",
    "type": "히어로 무비"
}

dict_a["name"]
dict_a["type"]

dict_b = {
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
}

dict_b
dict_b["director"]

# 딕셔너리의 요소에 접근
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])

# 딕셔너리 값 변경
dictionary["name"] = "8D 건조 망고"
print("naem:", dictionary["name"])

# 딕셔너리 내 리스트키 인덱스 출력
dictionary["ingredient"]
dictionary["ingredient"][1]

# 딕셔너리에 값 추가 및 제거
'''  딕셔너리[새로운 키] = 새로운 값  '''
dictionary["price"] = 5000
dictionary

del dictionary["ingredient"]
dictionary

dictionary = {}
print("요소 추가 이전:", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"
print("요소 추가 이후:", dictionary)

print("요소 제거 이전:", dictionary)

del dictionary["name"]
del dictionary["head"]
del dictionary["body"]
print("요소 제거 이후", dictionary)

'''
KeyError 예외
> 리스트의 길이를 넘는 인덱스에 접근하면 IndexError가 발생한다.
  딕셔너리도 존재하지 않는 키에 접근하면 마찬가지로 KeyError가 발생한다.
'''

### 딕셔너리 내부에 키가 있는지 확인하기

# in 키워드 활용 예제
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

key = input("> 접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# get(): 키 존재 유무 확인
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")

# for 반복문: 딕셔너리와 함께 사용하기
''' 주의할 점: 딕셔너리 내부에 있는 키가 변수에 들어감 
    for 키 변수 in 딕셔너리:
        코드
'''
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

for key in dictionary:
    print(key, ":", dictionary[key])

'''
키워드 정리
1. dictionary: 키를 기반으로 여러 자료를 저장하는 자료형
2. key: 딕셔너리 내부에서 값에 접근할 때 사용하는 것
3. value: 딕셔너리 내부에 있는 각각의 내용을 의미
'''

pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]
print("# 우리동네 애완 동물들")

for pet in pets:
    print(pet["name"], str(pet["age"]) + "살")

# 연습문제
'''
1. numbers 내부에 들어 있는 숫자가 몇 번 등장하는지를 출력하는 코드를 작성하시오.
'''
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1

print(counter)

'''
2. 다음과 같은 방법으로 특정 값이 어떤 자료형인지 확인할 수 있습니다.
    type("문자열") is str  # 문자열인지 확인
    type([]) is list       # 리스트인지 확인
    type({}) is dict       # 딕셔너리인지 확인
    이를 활용해 실행결과와 같이 출력되게 만드시오.
'''
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])