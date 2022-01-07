### time 모듈: 일반적으로 유닉스 타임을 구할 때, 특정 시간 동안 코드 진행을 정지할 때 많이 사용함.

import time

print("지금부터 5초 동안 정지한다.")
time.sleep(5)
print("프로그램을 종료합니다.")

### urllib 모듈: URL(Uniform Resource Locator)을 다루는 라이브러리

from urllib import request

target = request.urlopen("https://google.com")      # urlopen() 함수로 구글의 메인 페이지를 읽는다.
output = target.read()

print(output)

## os 모듈

# 현재 디렉터리를 읽어 들이고 파일인지 디렉터리인지 구분하기
import os

# 현재 폴더의 파일/폴더를 출력
output = os.listdir(".")
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더를 구분
print("# 폴더와 파일 구분")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)


# 현재 폴더 내부에 있는 모든 파일 탐색

def read_folder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("파일:", item)
read_folder(".")