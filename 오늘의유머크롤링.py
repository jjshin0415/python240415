#오늘의 유머 크롤링
# coding:utf-8
# 정적인 웹사이트 
from bs4 import BeautifulSoup

#파이썬 내장 lib
import urllib.request

#정규표현식
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 저장
f = open("todayhumor.txt","wt",encoding="utf-8")
for n in range(1,11):
        #오늘의 유머 베스트 오브 베스트 
        url ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        # <td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;no=474681&amp;s_no=474681&amp;page=1" target="_top">시골 병원 경고문</a>
        # </td>

        for item in list:
            title = item.find("a").text.strip()
            print(title)

            # # 키워드 검색
            # if re.search("아이패드",  title):
            #    print(title)
            #    f.write(f"{title}\n")

f.close()
