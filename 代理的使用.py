#代理的设置
#urllib

# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
# proxy='127.0.0.1:10086'
# proxy_handler=ProxyHandler({
#     'http':'http://'+proxy,
#     'https':'https://'+proxy
# })
# opener=build_opener(proxy_handler)
# try:
#     response=opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print('Error:',e.args)
#认证代理  把proxy值变更即可
# proxy='username:password@127.0.0.1:10086'

#SOCKS5类型
# import socks
# import socket
# from urllib import request
# from urllib.error import URLError
# socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',10086)
# socket.socket=socks.socksocket
# try:
#     response=request.urlopen('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

#requests
# import requests
# proxy='127.0.0.1:10086'
# proxies={
#     'http':'http://'+proxy,
#     'https':'https://'+proxy
# }
# try:
#     response=requests.get('http://httpbin.org/get')
#     print(response.text)
# except requests.ConnectionError as e:
# # except requests.exceptions.ConnectionError as e:
#     print('Error',e.args)

#SOCKS5类型
# import requests
# proxy='127.0.0.1:10086'
# proxies={
#     'http':'socks5://'+proxy,
#     'https':'socks5://'+proxy
# }
# try:
#     response=requests.get('http://httpbin.org/get',proxies=proxies)
#     print(response.text)
# except requests.ConnectionError as e:
#     print('Error:',e.args)

#全局代理
# import requests
# import socks
# import socket
# socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',10086)
# socket.socket=socks.socksocket
# try:
#     response=requests.get('http://httpbin.org/get')
#     print(response.text)
# except requests.ConnectionError as e:
#     print('Error:',e.args)
#
#Selenium
from selenium import webdriver
# proxy='127.0.0.1:10086'
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://'+proxy)
# browser=webdriver.Chrome(chrome_options=chrome_options)
# browser.get('http://httpbin.org/get')

