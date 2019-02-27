from selenium import webdriver
#获取淘宝左侧导航条条目
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
lis=browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()