from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pyquery import PyQuery as pq
import pymongo
keyword='电脑'
chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['product']
collection = db['computer']
url = 'https://s.taobao.com/search?q=' + quote(keyword)
def get_page(page):
    try:
        browser.get(url)
        if page > 1:
            input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager .m-page .input')))
            input.clear()
            input.send_keys(page)
            submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form>span.btn.J_Submit')))        #同一个节点span.btn.J_Submit，CSS选择器要紧挨一起，而不是span .btn.J_Submit
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager  li.item.active > span'),str(page)))       #某个节点文本包含某文字
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .grid .item')))
        get_products()
    except NoSuchElementException:
        get_page(page)
        print('Not Found')
def get_products():
    html=browser.page_source
    doc=pq(html)
    items=doc('.m-itemlist .grid .items .item').items()       #items()构造生成器
    for item in items:
        product={
            'name':item.find('.title').text().replace('\n',''),
            'price':item.find('.price').text().replace('\n',''),
            'deal':item.find('.deal-cnt').text(),
            'shop':item.find('.shopname').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(product):
    try:
        if collection.insert(product):
            print('success')
    except:
        print('failed')

if __name__=='__main__':
    for i in range(1,10):
        get_page(i)
