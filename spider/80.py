import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
#选项卡管理
browser=webdriver.Chrome(chrome_options=option)
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[2])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.zhihu.com')

