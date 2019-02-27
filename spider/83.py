from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(browser,50)
KEYWORD='iPad'

def index_page(page):
    print('正在爬取第%s页' % page)
    try:
        url='https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page>1:
            input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form>input')))
            input.clear()
            input.send_keys(page)
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.m-page .btn')))
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active>span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

from pyquery import PyQuery as pq
def get_products():
    html=browser.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    print(type(items))
    for item in items:
        product={
            'image':'http:'+item.find('.img').attr('data-src'),
            'price':item.find('.price').text().replace('\n',''),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

import pymongo
MONGO_URL='localhost'
MONGO_DB='taobao'
MONGO_COLLECTION='iPad'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

MAX_PAGE=5
def main():
    for i in range(1,MAX_PAGE+1):
        index_page(i)

if __name__=='__main__':
    main()
