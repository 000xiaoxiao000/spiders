from selenium import webdriver

url='https://www.zhihu.com'
browser=webdriver.Chrome()
browser.get(url)
print(browser.get_cookies())
'''browser.add_cookie({'name':'name','value':'germey','domain':'www.zhihu.com'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())'''