from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from PIL import Image
from io import BytesIO

url = 'https://passport.weibo.cn/signin/login'
username = '15708915671'
password = 'qfg2871445718'

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)
browser.get(url)
# browser.maximize_window()
browser.set_window_size(1200, 800)
Username = wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
Password = wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
submit = wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
Username.send_keys(username)
Password.send_keys(password)
submit.click()
try:
    img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
except TimeoutException:
    print('未出现验证码')
time.sleep(2)
location = img.location
print(location)
size = img.size
print(size)
# 缩放比例125%，每个参数都*1.25        重点！！！
top, bottom, left, right = location['y'] * 1.25, location['y'] * 1.25 + size['height'] * 1.25, location['x'] * 1.25, \
                           location['x'] * 1.25 + size['width'] * 1.25
print('验证码位置', top, bottom, left, right)
print(tuple((left, top, right, bottom)))
# screenshot=browser.get_screenshot_as_png()
# screenshot=Image.open(BytesIO(screenshot))
screenshot = browser.get_screenshot_as_png()
screenshot = Image.open(BytesIO(screenshot))
captcha = screenshot.crop((left, top, right, bottom))
captcha.show()
