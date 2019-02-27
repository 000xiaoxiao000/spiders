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

KEYWORD=''

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
broswer=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(broswer,20)

def index_page(page):
    '''
    抓取索引页
    :param page:页码
    '''
    number=str((int(page)-1)*15)
    print('正在爬取第%s页' % page)
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

#数据库存储
MONGO_URL='localhost'
MONGO_DB='CNKI'
MONGO_COLLECTION=KEYWORD
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
def save_to_mongo(result):
    '''
    保存至MongoDB
    :param result:结果
    '''
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

def main(MAX_PAGE=5):
    '''
    遍历页数
    '''
    for i in range(1,MAX_PAGE+1):
        index_page(i)



def gui():
    root=Tk()
    root.title('CNKI文献检索')
    root.geometry("600x200")
    root.resizable(width=False,height=False)
    frm=Frame(root)
    l=Label(root,text='Made by Qianfg').pack(side=BOTTOM)

    frm1=Frame(frm)
    w1=Label(frm1,text='关键词:',width=5,height=2).pack(side=LEFT)
    var1=StringVar()
    entry1=Entry(frm1,textvariable=var1,width=40).pack(side=LEFT)
    var1.set('123456789')
    b1=Button(frm1,text='检索').pack(side=RIGHT)
    frm1.pack(side=TOP)

    frm2=Frame(frm)
    w2=Label(frm2,text='链接:',width=5,height=2).pack(side=LEFT)
    var2=StringVar()
    entry2=Entry(frm2,textvariable=var2,width=40).pack(side=LEFT)
    var2.set('123456789')
    b2=Button(frm2,text='下载',command=main).pack(side=RIGHT)
    frm2.pack(side=TOP)

    frm3=Frame(frm)
    w3=Label(frm3,text='页数:',width=5,height=2).pack(side=LEFT)
    var3=StringVar()
    entry3=Entry(frm3,textvariable=var3,width=10).pack(side=LEFT)
    var3.set('5')
    frm3.pack(side=LEFT)

    frm.pack(pady=30)
    root.mainloop()
    MAX_PAGE = int(var3.get())
    print(MAX_PAGE)