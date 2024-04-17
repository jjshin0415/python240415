import requests
from bs4 import BeautifulSoup
import time

def crawl_blog(search_keyword, max_pages):
    # 기본 URL 설정
    base_url = "https://search.naver.com/search.naver"
    
    # 전체 결과를 저장할 리스트
    results = []

    # 최대 페이지 수만큼 반복
    for page in range(1, max_pages + 1):
        # 쿼리 파라미터 설정
        params = {
            'where': 'post',
            'query': search_keyword,
            'start': (page - 1) * 10 + 1
        }
        
        # 페이지 요청
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 각 블로그 포스트 정보 추출
        blog_posts = soup.select('.api_txt_lines.total_tit')

        for post in blog_posts:
            title = post.text
            link = post['href']

            # 블로그 상세 페이지 요청
            post_response = requests.get(link)
            post_soup = BeautifulSoup(post_response.text, 'html.parser')

            # 블로그명과 포스팅 날짜 추출
            blog_name = post_soup.select_one('.nick').text
            post_date = post_soup.select_one('.se_publishDate.pcol2').text

            results.append({
                '블로그명': blog_name,
                '블로그주소': link,
                '제목': title,
                '포스팅날짜': post_date
            })
        
        # 안전한 크롤링을 위해 각 페이지 요청 사이에 잠시 대기
        time.sleep(1)

    return results

# 사용자 입력
search_keyword = input("검색어를 입력하세요: ")

# 결과를 받아 출력
results = crawl_blog(search_keyword, 100)
for result in results:
    print(result)
