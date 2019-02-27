from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input=browser.find_element_by_id('q')
input.send_keys('枕头')
time.sleep(5)
input.clear()
input.send_keys('iPad')
button=browser.find_element_by_css_selector('.search-bd .search-panel .search-button')
button.click()
