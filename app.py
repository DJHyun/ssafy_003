from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("nice to meet you")
    return """
    <h1>유병재 잘생겼다</h1>
    <img src="https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
    <h3>ssafy 화이팅ㅎㅎ</h3>
    """
    
@app.route('/naver_toon')
def naver_toon():
    today = time.strftime("%a").lower()
    '''
    1. 네이버 웹툰을 가져올 수 있는 주소(url)를 파악하고 url 변수에 저장한다.
    
    2. 해당 주소로 요청을 보내 정보를 가져온다.
    
    3. 받은 정보를 bs를 이용해 검색하기 좋게 만든다.
    
    4. 네이버 웹툰 페이지로 가서, 내가 원하는 정보가 어디에 있는지 파악한다.
    오늘자 업데이트 된 웹툰들의 각각 리스트 페이지, 웹툰의 제목 + 해당 웹툰의 썸네일
    
    5. 3번에서 저장한 문서를 이용해 4번에서 파악한 위치를 뽑아내는 코드를 작성한다.
    
    6. 출력한다.
    '''
    
    naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
    response = requests.get(naver_url).text
    soup = bs(response,'html.parser')
    toons = []
    li = soup.select('.img_list li')
    
    for item in li:
      toon = {"title":item.select_one('dt a').text,
              "url": item.select('dt a')[0]["href"],
              "img_url":item.select('.thumb img')[0]['src']
             }
      toons.append(toon)
      

      
    return render_template('naver_toon.html', t = toons)
    
@app.route('/daum_toon')
def daum_toon():
    
    return render_template('naver_toon.html')
  