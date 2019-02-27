from selenium import webdriver
chrome_options=webdriver.chrome_options()
chrome_options.add_arguments('--headless')
chrome_options.add_arguments('--no-sandbox')
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com')
print(browser.page_source)
