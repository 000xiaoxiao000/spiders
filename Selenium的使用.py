#直接拿到javascript渲染结果，不用担心什么加密系统
#试验
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser=webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input=browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait=WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

#声明浏览器对象
# from selenium import webdriver
# browser=webdriver.Chrome()

#访问页面
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

#查找节点
#单个节点
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first=browser.find_element_by_id('q')         #ID
# input_second=browser.find_element_by_css_selector('#q')     #CSS选择器
# input_third=browser.find_element_by_xpath('//*[@id="q"]')      #XPath
# print(type(input_first))
# print(type(input_second))
# print(type(input_third))

#通用方法
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first=browser.find_element(By.ID,'q')
# input_second=browser.find_element(By.XPATH,'//*[@id="q"]')
# input_third=browser.find_element(By.CSS_SELECTOR,'#q')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()

#多个节点
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis=browser.find_elements_by_css_selector('.service-bd li')
# print(type(lis))
# print(lis)
# i=0
# for li in lis:
#     i+=1
#     print(i)
#     print(li)

#通用方法
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis=browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
# print(lis)

# #节点交互
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# _input=browser.find_element_by_css_selector('#q')
# _input.send_keys('短袖')
# time.sleep(1)
# _input.clear()
# _input.send_keys('皮皮虾')
# button=browser.find_element_by_css_selector('.btn-search')
# button.click()
# # #另一种方式
# # time.sleep(2)
# # _input.send_keys(Keys.ENTER)

#动作链
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# browser=webdriver.Chrome(chrome_options=chrome_options)
# url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source=browser.find_element_by_css_selector('#draggable')
# target=browser.find_element_by_css_selector('#droppable')
# actions=ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

#执行JavaScript
# from selenium import webdriver
# False
# browser=webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')     #将进度条拉倒最底下
# browser.execute_script('alert("To Bottom")')                                #显式“To Bottom”

#获取节点信息     get_attribute
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# logo=browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

#获取文本值  text
# from selenium import webdriver
# url='https://www.zhihu.com/explore'
# browser=webdriver.Chrome()
# browser.get(url)
# a=browser.find_element_by_class_name('question_link')
# print(a.text)

#获取id(id)、位置(location)、标签名(tag_name)、大小(size)
# from selenium import webdriver
# url='https://www.zhihu.com/explore'
# browser=webdriver.Chrome()
# browser.get(url)
# a=browser.find_element_by_class_name('question_link')
# print(a.id)
# print(a.location)
# print(a.tag_name)
# print(a.size)

#切换Frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser=webdriver.Chrome()
# url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo=browser.find_element_by_class_name('logo')
# except NoSuchElementException as e:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo=browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

#延时等待   确保节点加载完毕
#隐式等待
# from selenium import webdriver
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')       #使用无头模式
# browser=webdriver.Chrome(chrome_options=chrome_options)
# browser.get('https://www.zhihu.com/explore')
# browser.implicitly_wait(10)
# a=browser.find_element_by_class_name('question_link')
# print(a)
# print(a.text)

#显式等待      效果更好
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# url='https://www.taobao.com'
# browser=webdriver.Chrome()
# browser.get(url)
# wait=WebDriverWait(browser,10)
# a=wait.until(EC.presence_of_element_located((By.ID,'q')))       #presence_of_element_located节点定位元组，判断是否成功加载，若否，抛出异常
# b=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))   #element_to_be_clickable用于按钮，也就是10s内可点击
# print(a,b)
#更多用法参考：

# 前进 back和后退forward
# from selenium import webdriver
# import time
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com')
# browser.get('https://www.baidu.com')
# browser.get('https://www.zhihu.com')
# browser.back()
# time.sleep(10)
# browser.forward()
# browser.close()

#cookies
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# print(browser.get_cookies())
# print('*'*80)
# browser.add_cookie({'name':'pipixia','domain':'www.zhihu.com','value':'germery'})
# print(browser.get_cookies())
# print('*'*80)
# browser.delete_all_cookies()
# print(browser.get_cookies())

#选项卡管理
# import time
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://www.zhihu.com')

#异常处理
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException,NoSuchElementException
# browser=webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Elements')
# finally:
#     browser.close()

