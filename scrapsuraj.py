from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver.v2 as uc
import re
import pprint
driver = uc.Chrome(executable_path=r'chromedriver.exe')
url = "https://www.freethink.com/articles?paging="
final_list = []
for page in range(1,4):
    driver.get(url+str(page)+'#more-stories')
    time.sleep(3)
    html = driver.page_source
    time.sleep(5)
    soup = BeautifulSoup(html, 'html.parser')

lists = soup.find_all('div', class_="mb-10")

for list in lists:
    title = list.find('a', class_="loop-item__title").text
    link=list.find('a', class_="loop-item__title", attrs={'href': re.compile("^https://")})
    image=list.find('img', attrs={'src': re.compile("^https://")})
    info={'title':title,'news_page_link':link.get('href'),'image_link':image.get('src')}
    final_list.append(info)

pprint.pprint(final_list)
