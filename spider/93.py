from selenium import webdriver

proxy='127.0.0.1:9743'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
broswer=webdriver.Chrome()
broswer.get('http://httpbin.org/get')