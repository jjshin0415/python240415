import requests
from bs4 import BeautifulSoup

# Naver 검색 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# HTTP GET 요청
response = requests.get(url)
response.encoding = 'utf-8'  # 응답 인코딩 설정 (필요시)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 기사 제목 선택하기
titles = soup.select('.news .api_subject_bx .news_tit')  # 이 선택자는 페이지의 HTML 구조에 따라 조정해야 할 수 있습니다.

# 기사 제목 출력
for title in titles:
    print(title.text.strip())  
    # .text로 텍스트를 추출하고 .strip()으로 공백을 제거
