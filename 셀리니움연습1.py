#셀리니움연습1.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#크롬 드라이버 실행
driver = webdriver.Chrome()

#URL 주소 ( 구글 로그아웃 상태로 실행)
driver.get("https://www.google.co.kr") 
#3초 대기
time.sleep(3)

#searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")

#id로 검색 
searchBox = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
searchBox.send_keys("맥북")

searchBox.send_keys(Keys.ENTER)
time.sleep(10)

#<textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="검색" value="" jsaction="paste:puy29d;" aria-label="검색" aria-autocomplete="both" aria-expanded="false" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwj6q_HQ08iFAxXTkq8BHeTqAIcQ39UDCAY"></textarea>