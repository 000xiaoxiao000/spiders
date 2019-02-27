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
from qianfg import index_page,get_data,save_to_mongo,main,login,get_url

ACCOUNT = 'zr8334'
PASSWORD = 'asdhe019'

# 爬取数据
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
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
if var1.get()!='':
    KEYWORD = var1.get()
if var2.get()!='':
    title = var2.get()
if var3.get()!='':
    MAX_PAGE = int(var3.get())
URL = get_url(title)
# 数据库存储
MONGO_URL = 'localhost'
MONGO_DB = 'CNKI'
MONGO_COLLECTION = KEYWORD
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]