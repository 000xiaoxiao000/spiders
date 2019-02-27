#requests高级用法
# #1.文件上传
# import requests
# files={'file':open('favicon.ico','rb')}
# r=requests.post('http://httpbin.org/post',files=files)
# print(r.text)

# #2.cookies
# import requests
# r=requests.get('http://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():     #将RequestsCookieJar转化为元组
#     print(key+'='+value)

#cookie登录
# import requests
#
# headers={
#     'Cookie':'d_c0="ADDlm2fexQ2PTjl33mZxmlNU8AqDw5gDRq4=|1529397047"; _zap=d69479ec-1aee-4b7f-a9b8-ee5be36bb8a1; _xsrf=DoekFn59T48aoAZWu0eV0mbXIiMIBnuU; __utmz=51854390.1532225963.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20171220=1^3=entry_date=20171220=1; q_c1=5df0993ea982458d88160a41c6b4603d|1532324717000|1532324717000; __utma=51854390.1486148398.1532225963.1532324721.1534316521.3; tgw_l7_route=53d8274aa4a304c1aeff9b999b2aaa0a; capsion_ticket="2|1:0|10:1534323831|14:capsion_ticket|44:ZDlmNzMzZDJjNGM2NDk1YmJjYjZhZjZmYjkyNjc5ZWY=|c817a77e322a6ef07d190602412484ba6a8b292f7943f656a09e52852cc51c0a"; z_c0="2|1:0|10:1534323856|4:z_c0|92:Mi4xWklQMUJnQUFBQUFBTU9XYlo5N0ZEU1lBQUFCZ0FsVk5rRHBoWEFDMDVfRFphMVlVZ3FPbjc4THdndDUzcGpUdjJn|2a5f6cbe78d4639a5d82d8cd7678dd2fdee3e87fe943ec65272fd45cf58b7b52"; unlock_ticket="AFDCmuCd3AwmAAAAYAJVTZjzc1uChNrMJKaBwgJcjGWCLNqkAVKm3A=="',
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.39'
# }
# r=requests.get('http://www.zhihu.com',headers=headers)
# print(r.text)

#会话维持
#反例
# import requests
# requests.get('http://httpbin.org/cookies/set/name/7758258')
# r=requests.get('http://httpbin.org/cookies')
# print(r.text)
#正例
# import requests
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/name/7758258')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

#ssl证书验证
# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()   #忽略警告
# r=requests.get('https://www.12306.cn',verify=False) #忽略验证
# print(r.status_code)
#
# #捕获警告到日志
# import requests
# import logging
# logging.captureWarnings(True)
# r=requests.get('https://www.12306.cn',verify=False) #忽略验证
# print(r.status_code)

# #代理设置
# import requests
# proxies={
#     'http':'http://10.10.1.10:3128',
#     'https':'https://10.10.1.10:1080'
# }
# r=requests.get('http://www.taobao.com',proxies=proxies)
# print(r.status_code)
#
# #若使用HTTP Basic Auth
# import requests
# proxies={
#     'http':'http://user:password@10.10.1.10:3128'
# }
# r=requests.get('http://www.taobao.com',proxies=proxies)
# print(r.status_code)
#
# #使用SOCKS代理
# import requests
# proxies={
#     'http':'socks5://10.10.1.10:3128',
#     'https':'socks5://10.10.1.10:1080'
# }
# r=requests.get('http://www.taobao.com',proxies=proxies)
# print(r.status_code)

# #超时设置
# import requests
# r=requests.get('http://www.taobao.com',timeout=0.1) #0.1为链接和读取总和，也可分别指定，如timeout=(5,11,30)
# print(r.status_code)
#


