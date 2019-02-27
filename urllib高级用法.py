# #验证
# from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# from urllib.error import URLError
# username=''
# password=''
# url='https://cloud.tencent.com/login'
#
# p=HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler=HTTPBasicAuthHandler(p)
# opener=build_opener(auth_handler)
#
# try:
#     result=opener.open(url)
#     html=result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)
#
# #代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
# proxy_handler=ProxyHandler({
#     'http':'http://127.0.0.1:9743',
#     'https':'https://127.0.0.1:9743'
# })
# opener=build_opener(proxy_handler)
# try:
#     response=opener.open('https://www.baidu.com')
#     print(response.read().decode('UTF-8'))
# except URLError as e:
#     print(e.reason)

# #Cookies
# import http.cookiejar,urllib.request
# cookie=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)

# #文本保存
import http.cookiejar,urllib.request
# filename='cookies.txt'
# cookie=http.cookiejar.MozillaCookieJar(filename)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# #获取cookie并利用
# cookie=http.cookiejar.MozillaCookieJar()
# cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))