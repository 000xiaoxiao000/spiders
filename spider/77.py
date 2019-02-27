from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
#url='https://www.zhihu.com/explore'
#隐式等待
'''browser.implicitly_wait(10)
browser.get(url)
input=browser.find_element_by_css_selector('.zu-top-add-question')
print(input)'''
#显式等待
url='https://www.taobao.com'
wait=WebDriverWait(browser,20)
input=wait.until(EC.presence_of_element_located((By.ID,'q')))
button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.bth-search')))
print(input,button)