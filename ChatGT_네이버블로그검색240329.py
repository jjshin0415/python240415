import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)

#<a href="https://blog.naver.com/pareko" class="sub_txt sub_name" target="_blank" onclick="return goOtherCR(this, 'a=rvw*b.writer&amp;r=2&amp;i=90000003_0000000000000033ECA5C9EE&amp;u='+urlencode(this.href))">순돌아범</a>

soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 301):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    #제목
    # <a nocr="1" href="https://blog.naver.com/meen703/223388020128" class="QS0gep6K3wmBGxMdfuA3 fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035525141.90000003_000000000000003402F6ADA0'" data-cb-trigger="true"><span class="WNE6DfqawXbjKLCLcd4a"><mark>맥북 에어</mark> M2 13인치 지금 사도 괜찮을까</span></a>
    #<span class="WNE6DfqawXbjKLCLcd4a">내돈내산 애플 <mark>맥북에어</mark> M2 [교육할인] 3</span>
    #블로그주소
    #<a nocr="1" href="https://blog.naver.com/meen703" class="QS0gep6K3wmBGxMdfuA3 fds-info-inner-text" target="_blank"><span class="WNE6DfqawXbjKLCLcd4a">최동구의 알고 싶은 IT 정보</span></a>
    #날짜
    #<span class="fds-info-sub-inner-text WNE6DfqawXbjKLCLcd4a">4일 전</span>
    posts = soup.find_all('div', {'class':'fds-ugc-block-mod-list grY7ARzqEvD6JYNGqTAD'})
    for post in posts:
        try:
            blog_address_elem = post.find("a", 
                attrs={"class":"QS0gep6K3wmBGxMdfuA3 fds-info-inner-text"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("a", 
                            attrs={"class":"QS0gep6K3wmBGxMdfuA3 fds-info-inner-text"}) 
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        

        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text WNE6DfqawXbjKLCLcd4a'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find('a',
            {'class':'QS0gep6K3wmBGxMdfuA3 fds-comps-right-image-text-title'})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address, blog_address_title, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)