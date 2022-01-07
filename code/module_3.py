### BeautifulSoup : 가장 널리 알려진 파이썬의 웹페이지 분석 모듈

## BeautifulSoup 모듈로 날씨 가져오기
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨 읽기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup을 사용해 웹 페이지를 분석
soup = BeautifulSoup(target, "html.parser")

# location 태그 찾기
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()

# -------------------------------------------------------------------------------------------------------- #

### Flask 모듈: 작은 기능만 제공하는 웹 개발 프레임워크

# Flask 모듈 사용하기
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"df

### BeautifulSoup 스크래이핑 실행하기

# 모듈 읽기
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨를 읽는다.
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup를 사용해 웹 페이지를 분석
    soup = BeautifulSoup(target, "html.parser")

    # location 태그 찾기
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )
        output += "<hr/>"
    return output