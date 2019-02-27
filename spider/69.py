from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
browser=webdriver.Chrome(chrome_options=option)
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()