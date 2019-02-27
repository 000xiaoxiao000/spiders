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



def save_to_mongo(result):
    '''
    保存至MongoDB
    :param result:结果
    '''
    try:
        if collection.insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    '''
    遍历页数
    '''
    for i in range(1,MAX_PAGE+1):
        index_page(i)




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
