from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse

import time

keyword = input()

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

# 인코딩 이슈 발생시
# parsed = parse.quote_plus(keyword)
# url = f'http://www.instagram.com/explore/tags/{parsed}/'

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('chromedriver', options=options)

# driver.implicitly_wait(10)

driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
hashtag_count = soup.find('span', {'class': 'g47SY'})

print(hashtag_count.text)

driver.close()