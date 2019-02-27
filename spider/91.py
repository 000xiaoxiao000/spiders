from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pymongo

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
broswer=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(broswer,20)

ACCOUNT='zr8334'
PASSWORD='asdhe019'

KEYWORD='拟茎点霉属'

MONGO_URL='localhost'
MONGO_DB='CNKI'
MONGO_COLLECTION=KEYWORD
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
collection=db[MONGO_COLLECTION]


def get_url(title):
    '''
    获取url
    '''
    try:
        result=collection.find_one({'title':title})
        print(result)
        return result['download']
    except TypeError:
        print('没有找到，请重新输入')


def login(url):
    '''
    登录下载
    :param url:
    '''
    try:
        broswer.get(url)
        input_account=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#TextBoxUserName')))
        input_passwd=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#TextBoxPwd')))
        Login=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#Button1')))
        #Login2为IP登录,适用于校园网
        #Logi2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Button2 .btn2')))
        #Login2.click()
        input_account.clear()
        input_account.send_keys(ACCOUNT)
        input_passwd.clear()
        input_passwd.send_keys(PASSWORD)
        Login.click()
    except TimeoutException:
        print('网络请求超时')
        login(URL)

if __name__=='__main__':
    title = '拟茎点霉属及其病害研究进展'
    URL=get_url(title)
    login(URL)
