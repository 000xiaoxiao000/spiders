#!/usr/bin/env python3
# _*_ coding='utf-8' _*_

import time
import pymongo
from tkinter import *
from selenium import webdriver
from urllib.parse import urlencode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def index_page(page):
    '''
    抓取索引页
    :param page:页码
    '''
    number=str((int(page)-1)*15)
    print('正在爬取第%s页' % page)
    KEYWORD=var1.get()
    params={
        'q':KEYWORD,
        'rank':'relevant',
        'cluster':'all',
        'val':'',
        'p':number
    }
    try:
        url = 'http://search.cnki.net/search.aspx?' + urlencode(params)
        broswer.get(url)
        html=broswer.find_element_by_css_selector('#page strong').text
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#page strong'),str(page)))
        get_data()
    except NoSuchElementException:
        print('资料比较匮乏，请减少页数')
    except TimeoutException:
        print('网络请求超时')
        time.sleep(1)
        index_page(page)


def get_data():
    '''
    获取页面信息
    :return:
    '''
    items = broswer.find_elements_by_css_selector('.wz_tab')
    for item in items:
        title=item.find_element_by_css_selector('a').text
        print(title)
        abstract = item.find_element_by_css_selector('.text').text
        links = item.find_elements_by_css_selector('a')
        link = links[0].get_attribute('href')
        download = links[1].get_attribute('href')
        from_=item.find_element_by_css_selector('.year-count [title]').text
        count = item.find_element_by_css_selector('.year-count .count').text
        data={
            'title':title,
            'abstract':abstract,
            'link':link,
            'download':download,
            'from':from_,
            'count':count
        }
        print(data)
        save_to_mongo(data)


def save_to_mongo(result):
    '''
    保存至MongoDB
    :param result:结果
    '''
    MONGO_URL = 'localhost'
    MONGO_DB = 'CNKI'
    KEYWORD=var1.get()
    MONGO_COLLECTION = KEYWORD
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    try:
        if collection.insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    '''
    遍历页数
    '''
    MAX_PAGE=int(var3.get())
    for i in range(1,MAX_PAGE+1):
        index_page(i)


def login():
    '''
    登录下载
    :param url:
    '''
    url=var2.get()
    print(url)
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
        login()


#CNKI下载账号
ACCOUNT = 'zr8334'
PASSWORD = 'asdhe019'
#ACCOUNT='15708915671'
#PASSWORD='123456'

# 爬取数据
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
broswer = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(broswer, 20)


# GUI可视化窗口
root = Tk()
root.title('CNKI文献检索')
root.geometry("600x200")
root.resizable(width=False, height=False)
frm = Frame(root)
l = Label(root, text='Made by Qianfg').pack(side=BOTTOM)
# 搜索关键词
frm1 = Frame(frm)
w1 = Label(frm1, text='关键词:', width=5, height=2).pack(side=LEFT)
var1 = StringVar()
entry1 = Entry(frm1, textvariable=var1, width=40).pack(side=LEFT)
var1.set('')
b1 = Button(frm1, text='检索',command=main).pack(side=RIGHT)
frm1.pack(side=TOP)
# 下载链接
frm2 = Frame(frm)
w2 = Label(frm2, text='链接:', width=5, height=2).pack(side=LEFT)
var2 = StringVar()
entry2 = Entry(frm2, textvariable=var2, width=40).pack(side=LEFT)
var2.set('')
b2 = Button(frm2, text='下载',command=login).pack(side=RIGHT)
frm2.pack(side=TOP)
# 页数
frm3 = Frame(frm)
w3 = Label(frm3, text='页数:', width=5, height=2).pack(side=LEFT)
var3 = StringVar()
entry3 = Entry(frm3, textvariable=var3, width=5).pack(side=LEFT)
var3.set('5')
frm3.pack(side=LEFT)

frm.pack(pady=30)
root.mainloop()