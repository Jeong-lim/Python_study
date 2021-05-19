  
from bs4 import BeautifulSoup
import requests
from datetime import datetime


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

rank = 1

results = soup.findAll('span','item_title')

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1