from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

EMAIL='287541326@qq.com'
PASSWORD='qfg2871445718'
#初始化
class CrackGeetest():
    def __init__(self):
        self.url='https://account.geetest.com/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.email=EMAIL
        self.password=PASSWORD
#模拟点击
def get_geetest_button(self):
    button=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'geetest_radar_tip')))
    return button
button=get_geetest_button()
button.click()
#识别缺口
def get_position(self):
    img=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
    time.sleep(2)
    location=img.location
    size=img.size
    top,bottom,lest,right=location['']


