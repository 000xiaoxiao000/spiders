from selenium import webdriver
import time

url1='https://www.baidu.com'
url2="https://www.taobao.com"
url3='https://www.zhihu.com'

browser=webdriver.Chrome()
browser.get(url1)
browser.get(url2)
browser.get(url3)
browser.back()
time.sleep(1)
browser.forward()
browser.close()
