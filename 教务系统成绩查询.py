import os
import PIL
import csv
import time
import pytesseract
from tkinter import *
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

#创建文件夹
if not os.path.exists('personaldata'):
    os.makedirs('personaldata')
base_url='http://jxgl.hainu.edu.cn'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser=webdriver.Chrome(chrome_options=chrome_options)
wait=WebDriverWait(browser,3)

def login_page():
    #登录页面
    browser.get(base_url)
    id=var1.get()
    password=var2.get()
    try:
        html=browser.page_source
        doc=pq(html)
        code_url=doc('#SafeCodeImg').attr('src')
        url=base_url+code_url
        result=parse_code(url)
        browser.back()
        useraccount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#userAccount')))
        userpassword = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#userPassword')))
        code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#RANDOMCODE')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnSubmit')))
        useraccount.send_keys(id)
        time.sleep(0.5)
        userpassword.send_keys(password)
        time.sleep(0.5)
        code.send_keys(result)
        time.sleep(0.5)
        submit.click()
        # get_page()
        if wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#calender_user_schedule'),'我的桌面')):
            get_page()
    except NoSuchElementException:
        print('Not Found')
    except TimeoutException:
        login_page()

def get_page():
    try:
        schedule = browser.find_elements_by_id('calender_user_schedule')
        # 课表
        print('课表')
        url_course = schedule[2].get_attribute('href')
        link = schedule[1].get_attribute('href')
        print(url_course)
        get_courselist(url_course)
        # 学习成绩
        print('成绩')
        browser.get(link)
        # time.sleep(1)
        Menu = browser.find_elements_by_css_selector('#LeftMenu1_divChildMenu ul a')
        url_score=Menu[8].get_attribute('href')
        url_english=Menu[9].get_attribute('href')
        personaldata_url = Menu[1].get_attribute('href')
        #学习成绩在第八位
        get_score(url_score)
        #四六级成绩
        get_englishscore(url_english)
        #个人信息
        get_personaldata(personaldata_url)
        time.sleep(3)
        browser.close()
    except IndexError:
        print('验证码错误')
        login_page()

def parse_code(url):
    #获取验证码截图
    # browser.set_window_size(1200, 800)        #有头模式
    browser.maximize_window()                   #headless模式
    browser.get(url)
    browser.get_screenshot_as_file('./personaldata/screenshot.png')
    image = PIL.Image.open('./personaldata/screenshot.png')
    # image = image.crop((705, 403, 780, 430))  # 有头模式模式，裁剪截图，试了好多次，得出的数据(窗口大小为1200*800)
    image=image.crop((370,290,416,310))         #headless模式
    image.save('./personaldata/code.png')
    time.sleep(1)
    #识别验证码
    image=PIL.Image.open('./personaldata/code.png')
    image=image.convert('L')
    threshold=127             #120-130比较合适
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table,'1')
    result=pytesseract.image_to_string(image)
    print('识别结果：',result)
    result=result.replace(' ','')
    result=result.replace('‘','')
    if len(result)==4:
        return result
    else:
        return False

def get_score(url):
    browser.get(url)
    time.sleep(3)
    browser.switch_to.frame('cjcx_list_frm')
    html=browser.page_source
    doc=pq(html)
    trs=doc('#dataList')
    content=trs.text().split('\n')
    content.pop(12)
    print(content)
    save_to_file(content)

def save_to_file(content):
    with open('./personaldata/score.csv','w',newline='') as csvfile:
        writer=csv.writer(csvfile)
        try:
            for n in range(30):
                a=content[12*n]
                b=content[12*n+1]
                c=content[12*n+2]
                d=content[12*n+3]
                e=content[12*n+4]
                f=content[12*n+5]
                g=content[12*n+6]
                h=content[12*n+7]
                i=content[12*n+8]
                j=content[12*n+9]
                k=content[12*n+10]
                l=content[12*n+11]
                writer.writerow([a,b,c,d,e,f,g,h,i,j,k,l])
        except IndexError:
            print('成绩单已下载完毕!')

def get_englishscore(url):
    browser.get(url)
    time.sleep(3)
    html=browser.page_source
    doc=pq(html)
    trs=doc('#dataList')
    content=trs.text().split('\n')[11:]
    print(content)
    content=str(content)
    with open('./personaldata/四六级成绩.txt','w') as f:
        f.write(content)
    print('四六级成绩已下载完毕！')

def get_personaldata(url):
    browser.get(url)
    time.sleep(3)
    html=browser.page_source
    doc=pq(html)
    trs=doc('#Form1 .Nsb_r_list.Nsb_table')
    content=trs.text().split('\n')
    print(content)
    with open('./personaldata/personaldata.csv','w',newline='') as csvfile:
        writer=csv.writer(csvfile)
        try:
            for n in range(7):
                a=content[8*n]
                b=content[8*n+1]
                c=content[8*n+2]
                d=content[8*n+3]
                e=content[8*n+4]
                f=content[8*n+5]
                g=content[8*n+6]
                h=content[8*n+7]
                writer.writerow([a,b,c,d,e,f,g,h])
        except IndexError:
            print('个人信息表已下载完毕！')
    print('个人信息表已下载完毕！')

def get_courselist(url):
    #要在有头模式下才能实现
    browser.get(url)
    time.sleep(3)
    a=browser.find_elements_by_css_selector('#LeftMenu1_divChildMenu ul a')
    link=a[2].get_attribute('href')
    browser.get(link)
    input=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Form1 input.button')))
    time.sleep(5)
    input.click()
    print('课程表已下载完毕！')
    time.sleep(1)

def open_files():
    base_url=os.path.abspath('.')
    url=base_url+'\personaldata'
    print(url)
    browser = webdriver.Chrome()
    browser.get(url)



if __name__=='__main__':
    # GUI可视化窗口
    root = Tk()
    root.title('校园网小助手')
    root.geometry("600x200")
    root.resizable(width=False, height=False)
    frm = Frame(root)
    l = Label(root, text='Made by Qianfg').pack(side=BOTTOM)
    # 搜索关键词
    frm1 = Frame(frm)
    w1 = Label(frm1, text='学号:', width=5, height=2).pack(side=LEFT)
    var1 = StringVar()
    entry1 = Entry(frm1, textvariable=var1, width=40).pack(side=LEFT)
    var1.set('')
    b1 = Button(frm1, text='登录',command=login_page).pack(side=RIGHT)
    frm1.pack(side=TOP)
    # 下载链接
    frm2 = Frame(frm)
    w2 = Label(frm2, text='密码:', width=5, height=2).pack(side=LEFT)
    var2 = StringVar()
    entry2 = Entry(frm2,show='*',textvariable=var2, width=40).pack(side=LEFT)
    var2.set('')
    b2 = Button(frm2, text='查看',command=open_files).pack(side=RIGHT)
    frm2.pack(side=TOP)

    frm.pack(pady=30)
    root.mainloop()

